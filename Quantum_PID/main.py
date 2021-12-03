from time import time
from time import sleep
import socket
import serial
import subprocess
import struct
import motordriver
from SmartTexServer import Writer
import shutil
import os
from datetime import datetime
from enum import Enum

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Commands ############
InitCmd = "init"
StartCmd = "start"
GetCmd = "get"
StopCmd = "stop"
# Messages ############
InitOK = "initok"
StopOK = "stopok"
StartOK = "startok"
ErrorMsg = "error"
#######################


class MissionMode(Enum):
    FORCE = 1
    POSITION = 2


class UDPClient:
    def __init__(self):
        self.mode = 0
        self.reps = 0
        self.submissions = []

    def set_params(self, mode, rep, submissions):
        self.mode = mode
        self.reps = rep
        self.submissions = submissions

    def send(self, StringToSend):
        if StringToSend != "":
            UDPClientSocket.sendto(str.encode(StringToSend), serverAddressPort)

    def receive(self):
        byteAddressPair = UDPClientSocket.recvfrom(bufferSize)
        stringReceived = byteAddressPair[0].decode("utf-8")
        # print(stringReceived)
        return stringReceived

    # main function
    def ProcessMission(self):
        # if the command was 'start' the loop stops and cmd gets sent
        self.send(StartCmd)
        if self.receive() != StartOK:
            print("Start went wrong")
            return

        for i in range(int(self.reps)):  # num of repeats
            for j in range(len(self.submissions)):  # num of submissions

                # -- check submode -----------------
                if self.mode == MissionMode.POSITION:
                    do_control = system.do_position_control
                elif self.mode == MissionMode.FORCE:
                    if not self.submissions[j][4][1]:
                        do_control = system.do_simple_force_control
                    else:
                        do_control = system.do_continuous_force_control
                else:
                    # TODO: return with error
                    return 0

                for k in range(int(self.submissions[j][3][1])):  # num of submission repeats
                    start_time = time()

                    while True:
                        # ----- check emergency Button -----
                        sensor.readButtons()
                        if not (sensor.getButton(0)):
                            print("buttons is lost")
                            self.StopError()
                            # TODO: return due to emergency
                            return 0

                        if time() - start_time >= int(self.submissions[j][1][1]):
                            # step to next submission when duration expires
                            break

                        # --- Receiving resistance Values ---
                        if not Mes.getRes():
                            print("ResMes is lost")
                            self.StopError()
                            # TODO: return with error
                            return 0

                        # -- get Force Values --------------
                        # sensor.getForce()  # get newest force values

                        # ------ Controller ----------------
                        desired = int(self.submissions[j][0][1])
                        do_control(desired)
                        # sleep(1)   # test delay

                        # --- Update DB --------------------
                        data.send_values(motor.get_position())
                        # sleep(1)   # test delay

        self.StopMission()
        return Mes.ChannelData

    def StopMission(self):
        # Mission end
        self.send(StopCmd)
        msg = self.receive()
        if msg != StopOK:
            print("MesStop is lost")

        print("mission done")
        handler.move_file(handler.success_folder)
        print("move success")

    def StopError(self):
        # Mission end
        self.send(StopCmd)
        msg = self.receive()
        if msg != StopOK:
            print("MesStop is lost")

        print("mission aborted")
        handler.move_file(handler.error_folder)
        print("move success")


class DataBase:
    def __init__(self):
        self.MyWriter = Writer("Quantum", "Testsetup")
        self.samples = 10

    def init(self):
        self.MyWriter.AddLabel("Forcesensor_1")
        self.MyWriter.AddLabel("Forcesensor_2")

        self.MyWriter.AddLabel("ADC_1")
        self.MyWriter.AddLabel("ADC_2")
        self.MyWriter.AddLabel("ADC_3")
        self.MyWriter.AddLabel("ADC_4")
        self.MyWriter.AddLabel("ADC_5")
        self.MyWriter.AddLabel("ADC_6")

        self.MyWriter.AddLabel("Temperature_1")
        self.MyWriter.AddLabel("Temperature_2")

        self.MyWriter.AddLabel("Motorposition_1")
        self.MyWriter.AddLabel("Motorposition_2")
        self.MyWriter.AddLabel("Motorposition_3")

        self.MyWriter.Start(self.samples)

    def set_samples(self, num_of_samples):
        self.samples = num_of_samples

    def send_values(self, position):
        print("Sending Values to DB...")  # TestPrint
        stamp_postion = stp.get_duty()
        points = [sensor.lcBig, sensor.lcSmall,     # Forcesensors
                  Mes.ChannelData[0], Mes.ChannelData[1], Mes.ChannelData[2],
                  Mes.ChannelData[3], Mes.ChannelData[4], Mes.ChannelData[5],  # ADC-Channels
                  0, 0,   # TODO: Environment Sensors
                  0, stamp_postion, 0]   # TODO: Motorpositions

        self.MyWriter.WriteTime(points, round(time() * 1000))


class Mission:
    def __init__(self):
        self.mission_params = []
        self.mode = 0

    def update_param_list(self, params, mode):
        self.mission_params = params
        self.mode = mode
        print("Params updated!")

    def distribute_params(self):
        control.set_params(int(self.mission_params[0][0][1]), int(self.mission_params[0][1][1]), int(self.mission_params[0][2][1]))
        motor.set_speed(int(self.mission_params[0][3][1]))
        data.set_samples(int(self.mission_params[0][4][1]))
        system.set_tolerance(int(self.mission_params[0][5][1]))
        Comlink.set_params(self.mode, int(self.mission_params[0][6][1]), self.mission_params[1:])


class Sensor:
    def __init__(self):
        self.buttons = [0.0] * 9
        self.lcBig = 0.0
        self.lcSmall = 0.0
        # print(self.buttons)

    def readButtons(self):
        # print("Buttons: ", end='')
        ser.write(bytearray('v', 'ascii'))
        # read all 9 buttons (pressed: 0xFF/ released: 0x00)
        self.buttons = ser.read(9)
        # print(self.buttons)
    
    def getButton(self, i):
        return self.buttons[i]

    def getForce(self):
        # print("Force: ", end='')
        # Big Loadcell
        ser.write(bytearray('b', 'ascii'))
        # buffer1 = [''] * 4
        buffer1 = ser.read(4)
        self.lcBig = struct.unpack("f", buffer1)[0]
        # print(self.lcBig, end=',')

        # Small loadcell
        ser.write(bytearray('s', 'ascii'))
        # buffer2 = [''] * 4
        buffer2 = ser.read(4)
        self.lcSmall = struct.unpack("f", buffer2)[0]
        # print(self.lcSmall)


class MotorControl:
    def __init__(self):
        self.steps_per_newton = 1  # TODO: evaluate how many steps per newtown should be sent
        self.position_in_steps = 0
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed

    def convert_to_steps(self, output_value, actual_value):
        # convert force value to number of steps
        force_change = output_value - actual_value
        return self.steps_per_newton * force_change

    def send_steps(self, num_of_steps):
        # TODO: send number of steps to motor with desired speed
        self.position_in_steps += num_of_steps

    def get_position(self):
        return self.position_in_steps


class PID:
    def __init__(self, error_prior=0, integral_prior=0):
        self.error_prior = error_prior
        self.integral_prior = integral_prior
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.bias = 0  # optional: makes sure that output is not 0

    def set_params(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def get_output(self, desired_value, actual_value):
        error = desired_value - actual_value  # calculate absolute error
        integral = self.integral_prior + error * system.iteration_time  # calculate integral term
        derivative = (error - self.error_prior) / system.iteration_time  # calculate derivative term

        self.error_prior = error
        self.integral_prior = integral

        return self.kp * error + self.ki * integral + self.kd * derivative + self.bias  # calculate output


class Measuring:
    def __init__(self):
        self.current_value = 0
        self.num_of_channels = 0
        self.ChannelData = [0.0] * 6

    def initMes(self, numOfChannels):
        # TODO: Get Number of channels to initialize
        self.num_of_channels = numOfChannels  # Get_channels_to_init()
        # build Command
        init_command = InitCmd + " " + str(self.num_of_channels)
        Comlink.send(init_command)
        if Comlink.receive() != InitOK:  # TestPrint
            print("MesInit is lost")
            return        
        # print("Initialisation Done")

    def getData(self, sData):
        # split all Data at ";" and make a list
        Data = sData.split(";")
        # add data to the right spot in the list
        # print(Data)
        for i, s in enumerate(Data):
            Mes.ChannelData[i] = float(s)

    def getRes(self) -> bool:
        Comlink.send(GetCmd)
        msg = Comlink.receive()  # problem
        if msg == ErrorMsg:
            return False
        self.getData(msg)
        return True


class ControlSystem:
    def __init__(self, iteration_time=1):
        self.iteration_time = iteration_time
        self.tolerance = 0

    def set_tolerance(self, tol):
        self.tolerance = tol

    def do_position_control(self, desired):
        # send certain amount of steps to motor with desired speed
        motor.send_steps(desired)
        # TODO (optional): wait until distance has been reached or send each step seperately

        data.send_values(motor.get_position())

    def do_simple_force_control(self, desired):
        # control until desired force has been reached
        if (Mes.current_value < (desired - self.tolerance)) | \
                (Mes.current_value > (desired + self.tolerance)):
            new_value = control.get_output(desired, Mes.current_value)
            motor.send_steps(motor.convert_to_steps(new_value, Mes.current_value))
        else:
            data.send_values(motor.get_position())

    def do_continuous_force_control(self, desired):
        new_value = control.get_output(desired, Mes.current_value)
        print("Neuer Wert: " + str(new_value))
        motor.send_steps(motor.convert_to_steps(new_value, Mes.current_value))
        data.send_values(motor.get_position())


class FileHandler:
    def __init__(self):
        self.queue_folder = 'mission_queue/'
        self.live_folder = 'mission_live/'
        self.success_folder = 'mission_done/'
        self.error_folder = 'mission_error/'
        self.file_name = ""

    def check_live(self):
        return any(os.scandir(self.live_folder))

    def check_queue(self):
        # already live
        if self.check_live():
            return
        # no missions queued
        if not any(os.scandir(self.queue_folder)):
            return

        # get current time
        file_list = sorted(os.listdir(self.queue_folder))
        first_file = file_list[0]
        current_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.txt'

        # check if mission is planed for now
        if first_file < current_date_time:
            # TODO: mission still valid
            shutil.move(self.queue_folder + first_file, self.live_folder + first_file)

    def move_file(self, destination):
        # print(self.file_name)
        shutil.move(self.live_folder + self.file_name, destination + self.file_name)

    def parse_mission(self):
        self.file_name = os.listdir(self.live_folder)[0]

        f = open(self.live_folder + self.file_name, "r")
        content = f.read()
        f.close()

        # parse content string
        content_list = content.splitlines()
        if len(content_list) < 11:
            print("Error")
            self.move_file(self.error_folder)
            return False

        num_of_setup_params = 7

        # check for mission mode
        if content_list[num_of_setup_params].find("NEWTON") != -1:
            num_of_entries = 5
            mode = MissionMode.FORCE
            print("Sollkraft Mission")
        elif content_list[num_of_setup_params].find("POSITION") != -1:
            num_of_entries = 4
            mode = MissionMode.POSITION
            print("Position Mission")
        else:
            print("Error")
            self.move_file(self.error_folder)
            return False

        # corrupt mission File
        print(len(content_list))
        if (len(content_list) - num_of_setup_params) % num_of_entries != 0:
            print("Error")
            self.move_file(self.error_folder)
            return False

        param_list = []
        help_list = []

        # Parse cmds into data struct
        for i in range(len(content_list)):
            value_pair = content_list[i].split(' ')

            if i < num_of_setup_params:
                help_list.append(value_pair)
                if i == num_of_setup_params - 1:
                    param_list.append(help_list)
                    help_list = []
            else:
                value_pair[0] = value_pair[0][2:]
                help_list.append(value_pair)
                if (i - num_of_setup_params + 1) % num_of_entries == 0:
                    param_list.append(help_list)
                    help_list = []

        # print(param_list)
        # print(param_list[0][0][1])
        print("Parse Good")

        mission.update_param_list(param_list, mode)

        return True


if __name__ == '__main__':
    ser = serial.Serial(port='COM4', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1)
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Creating Objects
    Comlink = UDPClient()
    control = PID()
    motor = MotorControl()
    data = DataBase()
    mission = Mission()
    Mes = Measuring()
    system = ControlSystem()
    sensor = Sensor()
    handler = FileHandler()

    # Database
    data.init()

    # Stamp 
    stp = motordriver.stamp()
    stp.init()

    # start ResMes
    p = subprocess.Popen(
        ['python', 'ResMes.py'],
        shell=False,
        stdin=None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True)

    # wait for startup from nano TODO: optimize
    sleep(5)

    # Main Loop
    while True:

        # ---- wait for mission ----
        print("Wait for start: ")

        while True:
            handler.check_queue()
            sensor.readButtons()

            if sensor.buttons[0] and handler.check_live():   # TODO: add start cases
                # print("File found")
                if handler.parse_mission():
                    break

            #if sensor.buttons[1]:   # stamp Up
                # stp.up()
             #   pass
        
        # ---- Initialisation ------
        # flush UART buffer
        ser.flushInput()

        # Reset UDPClient Variables
        Comlink.__init__()

        mission.distribute_params()

        # Get Dataset (Force over Time!!) from File
        # data.update_dataset()

        # Initialize ADC's
        Mes.initMes(1)

        # ------ Start Mission -------
        # (sending and controllig values)
        res = Comlink.ProcessMission()
