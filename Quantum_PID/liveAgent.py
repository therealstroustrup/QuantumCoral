from SpectreMqtt import SpectreMqtt

import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.device import Device

import json

import serial
import sys
import argparse
import time
import netifaces
import copy
import subprocess


configuration = spectre_api_client.Configuration(
    host = "https://smarttexserver.projekte.fh-hagenberg.at/icapi"
)
spectreApiClient = spectre_api_client.ApiClient(configuration)


# Class for storing serial parameters and the Serial class itself from pySerial
class SerialPort:
    Port: serial.Serial

    def __init__(self):
        self.Port = None
        self.Baud = 115200
        self.Databits = 8
        self.Parity = serial.PARITY_NONE
        self.Stopbits = 1.0


def newMissionCallback(mission):
    subprocess.call(["python", "callbacks/NewMission.py", json.dumps(mission)])
    print(mission)


def newLiveCommandCallback(mission):
    subprocess.call(["python", "callbacks/LiveMissionCommand.py", json.dumps(mission)])
    print(mission)


class LiveAgent:
    def __init__(self, defaultParameters: SerialPort, parameters: "dict[str, SerialPort]", dummy: bool=False):
        self.__defaultParameters = defaultParameters
        self.__parameters = parameters
        self.__dummy = dummy
    def onLiveMissionCommand(self, command):
        if "deviceId" in command:   # Fetch device from database
            if command["deviceId"] is not None:
                # Fetch device from database
                try:
                    apiInstance = default_api.DefaultApi(spectreApiClient)
                    device = apiInstance.get_device_by_id(command["deviceId"])
                except TypeError:
                    # If the ID doesn't exist in the database, a `TypeError` is raised
                    print(f'Device ID {command["deviceId"]} not found in database')
                    return
            # Create port name
            if sys.platform.startswith('linux'):
                port = f"/dev/ttyUSB{device.port}"
            elif sys.platform.startswith('win32'):
                port = f"COM{device.port}"
            else:
                print("Unsupported platform", file=sys.stdout)
                return

            # Try to open port and send command
            if self.__dummy:
                # In dummy mode the command is printed to the command line without writing to serial
                print(f'{port}: "{command["textCommand"]}')
            else:
                ser = self.__parameters.get(port)

                # Copy default paramters, if port does not exist
                if ser is None:
                    ser = copy.copy(self.__defaultParameters)
                    self.__parameters[port] = ser

                # Open serial port, if custom configuration or just created
                if ser.Port is None:
                    ser.Port = serial.Serial(port, ser.Baud, ser.Databits, ser.Parity, ser.Stopbits)
                    if ser.Port.isOpen():
                        ser.Port.close()

                print(f'Sending "{command["textCommand"]}" to {port} ...')

                ser.Port.open()
                ser.Port.write(bytes(command["textCommand"], 'ascii'))
                ser.Port.close()
        else:
            print("No device in message", file=sys.stderr)
            # Use handle in subprocess

            subprocess.call(["python3", "callbacks/LiveMissionCommand.py", command['befehl']])
            print(command['befehl'])
            return


def parse_args(args: argparse.Namespace):
    validDatabits = range(5, 8+1)
    validParity = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]
    validStopbits = [serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO]
    defaultParameters = SerialPort()
    parameters = {}

    # Parse default parameters
    if args.baudrate is not None:
        defaultParameters.Baud = args.baudrate

    if args.databits is not None:
        if args.databits in validDatabits:
            defaultParameters.Databits = args.databits
        else:
            raise argparse.ArgumentTypeError("Invalid value for databits.")

    if args.parity is not None:
        parity = args.parity[0]
        parity = parity.upper()

        if parity in validParity:
            defaultParameters.Parity = parity
        else:
            argparse.ArgumentTypeError("Invalid value for parity.")

    if args.stopbits is not None:
        if args.stopbits in validStopbits:
            defaultParameters.Stopbits = args.stopbits
        else:
            argparse.ArgumentTypeError("Invalid value for stopbits.")

    # Parse custom ports
    config: str
    i = 0
    for config in args.device:
        portName, params, *_ = config.split(":")
        if len(_) > 0:
            argparse.ArgumentTypeError("Wrong syntax for device.")
        if portName is None or len(portName) < 1:
            argparse.ArgumentTypeError("Please state a port for each device.")

        baud, databits, parity, stopbits, *_ = params.split(",")
        if len(_) > 0:
            argparse.ArgumentTypeError("Wrong syntax for device.")

        if databits not in validDatabits:
            argparse.ArgumentTypeError(f"Invalid value for databits for device {i}.")

        if parity not in validParity:
            argparse.ArgumentTypeError(f"Invalid value for parity for device {i}.")

        if stopbits not in validStopbits:
            argparse.ArgumentTypeError(f"Invalid value for stopbits for device {i}.")

        serialPort = SerialPort()
        serialPort.Baud = baud
        serialPort.Databits = databits
        serialPort.Stopbits = stopbits
        parameters[portName] = serialPort

        i += 1

    return defaultParameters, parameters, args.dummy


def main():
    parser = argparse.ArgumentParser(description="Waits for commands for preassure test device",
        epilog="Arguments -b, -p and -s set the default paramters, which are used for devices for which no explicit configuration is configured for.")
    parser.add_argument("-b", "--baudrate", type=int,
        help="Default baud rate of the serial connection. Default: 115200")
    parser.add_argument("-d", "--databits", type=int,
        help="Default number of data bits. Possible values: 5-8. Default: 8")
    parser.add_argument("-p", "--parity", type=str,
        help="Default parity to be used for serial communication. Possible values: 'none', 'even' and 'odd'. Default: 'none'")
    parser.add_argument("-s", "--stopbits", type=float,
        help="Default number of stop bits for serial connection. Possible values: 1, 1.5, 2. Default: 1")
    parser.add_argument("device", nargs='*',
        help="Specify different paramters for one specific device. Specify as <port>:<baud>,<databits>,<parity>,<stopbits>. Example: COM3:115200,8,N,1.")
    parser.add_argument("--dummy", action="store_true",
        help="Switch. Enables dummy mode of this script. Instead of writing commands to the serial ports, the script prints the message to stdout including the port which the message would have been sent to.")

    args = parser.parse_args()
    #print(args)

    try:
        defaultParamters, parameters, dummy = parse_args(args)
    except argparse.ArgumentTypeError as err:
        parser.error(err.args[0])

    agent = LiveAgent(defaultParamters, parameters, dummy)

    # Get mac address of default interface
    defaultInterface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    mac = netifaces.ifaddresses(defaultInterface)[netifaces.AF_LINK][0]['addr']
    print(f'Using mac address: "{mac}"')

    # Get own spy (to subscibe to the right MQTT topic)
    apiInstance = default_api.DefaultApi(spectreApiClient)
    spyList = apiInstance.get_spies(mac=mac)
    print(spyList)

    spy = 0
    # If spy is not found, create a new one in the database
    if len(spyList.spies) == 0:
        print("Did not find myself in database. Creating new spy ...")
        spy = Spy(name="New live agent", mac=mac, location="Hagenberg", status="Active")
        idObj = apiInstance.add_spy(spy)
        spy.id = idObj.id

        print(F"New spy ID: {spy.id}")
    else:
        spy = spyList.spies[0]
        print(f"Found own spy in database. ID: {spy.id}")

    spectreClient = SpectreMqtt(int(spy.id))
    spectreClient.sendHeartbeat("Active")

    spectreClient.liveMissionCommandCallback = newLiveCommandCallback
    spectreClient.liveMissionStopCallback = spectreClient.sendHeartbeat("Active")
    spectreClient.liveMissionStartCallback = spectreClient.sendHeartbeat("Active")
    spectreClient.newMissionCallback = newMissionCallback

    spectreClient.loopForever()


if __name__ == "__main__":
    main()
