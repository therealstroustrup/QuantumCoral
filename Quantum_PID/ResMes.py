##########################################################
# Author:   Roland Lux, Sebastian Mück
# Date :    18.10.2021
# File:     Quantum_Res_Mess.py
# Desc:     Main File for the communication between
#           the Coral Board and the PCB.
#
#           For further information of the used protocoll
#           look into the <com_protocoll_path> file
##########################################################

import socket
import serial
import select

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Anmeldung
# Init + Channels(mind. 3)
# Start (Werte werden gesendet)
# Stop

# RENAMED Frame to Global

class Global(object):
    # msg to expect after a successfull command --------------------------------------
    ResetDoneMsg = "060500414203"
    InitDoneMsg = "060500424103"
    StartDoneMsg = "060500434003"
    StopDoneMsg = "040461074008"

    # Packet for Reset ---------------------------------------------------------------
    Reset_packet = bytearray()
    Reset_packet.append(0x02)
    Reset_packet.append(0x05)
    Reset_packet.append(0x00)
    Reset_packet.append(0x41)
    Reset_packet.append(0x46)
    Reset_packet.append(0x03)

    # Init msgs ----------------------------------------------------------------------

    # Packet to Init 1 Channel
    #0x02-05-03-42-00-01-02-45-03
    Init_packet1 = bytearray()
    Init_packet1.append(0x02)
    Init_packet1.append(0x05)
    Init_packet1.append(0x03)
    Init_packet1.append(0x42)
    Init_packet1.append(0x00)
    Init_packet1.append(0x01)
    Init_packet1.append(0x02)
    Init_packet1.append(0x45)
    Init_packet1.append(0x03)

    # Packet to Init 2 Channels
    #0x02-05-03-42-00-03-02-47-03
    Init_packet2 = bytearray()
    Init_packet2.append(0x02)
    Init_packet2.append(0x05)
    Init_packet2.append(0x03)
    Init_packet2.append(0x42)
    Init_packet2.append(0x00)
    Init_packet2.append(0x03)
    Init_packet2.append(0x02)
    Init_packet2.append(0x47)
    Init_packet2.append(0x03)

    # Packet to Init 3 Channels richtig
    #0x02-05-03-42-00-07-02-43-03
    Init_packet3 = bytearray()
    Init_packet3.append(0x02)
    Init_packet3.append(0x05)
    Init_packet3.append(0x03)
    Init_packet3.append(0x42)
    Init_packet3.append(0x00)
    Init_packet3.append(0x07)
    Init_packet3.append(0x02)
    Init_packet3.append(0x43)
    Init_packet3.append(0x03)

    # Packet to Init 4 Channels richtig
    #00x02-05-03-42-00-0F-02-4B-03
    Init_packet4 = bytearray()
    Init_packet4.append(0x02)
    Init_packet4.append(0x05)
    Init_packet4.append(0x03)
    Init_packet4.append(0x42)
    Init_packet4.append(0x00)
    Init_packet4.append(0x0F)
    Init_packet4.append(0x02)
    Init_packet4.append(0x4B)
    Init_packet4.append(0x03)

    # Packet to Init 5 Channels
    #0x02-05-03-42-00-1F-02-5B-03
    Init_packet5 = bytearray()
    Init_packet5.append(0x02)
    Init_packet5.append(0x05)
    Init_packet5.append(0x03)
    Init_packet5.append(0x42)
    Init_packet5.append(0x00)
    Init_packet5.append(0x1F)
    Init_packet5.append(0x02)
    Init_packet5.append(0x5B)
    Init_packet5.append(0x03)

    # Packet to Init 6 Channels
    #0x02-05-03-42-00-3F-02-7B-03
    Init_packet6 = bytearray()
    Init_packet6.append(0x02)
    Init_packet6.append(0x05)
    Init_packet6.append(0x03)
    Init_packet6.append(0x42)
    Init_packet6.append(0x00)
    Init_packet6.append(0x3F)
    Init_packet6.append(0x02)
    Init_packet6.append(0x7B)
    Init_packet6.append(0x03)

    # Init Array (put NrOfADC - 1 to get the correct InitPaclet)
    Init_packet = [Init_packet1, Init_packet2, Init_packet3, Init_packet4, Init_packet5, Init_packet6]

    # ------------------------------------------------------------------------------

    # Packet to start Messuring Values ---------------------------------------------
    Start_packet = bytearray()
    Start_packet.append(0x02)
    Start_packet.append(0x05)
    Start_packet.append(0x00)
    Start_packet.append(0x43)
    Start_packet.append(0x44)
    Start_packet.append(0x03)

    # Packet to stop Messuring Values ----------------------------------------------
    Stop_packet = bytearray()
    Stop_packet.append(0x02)
    Stop_packet.append(0x05)
    Stop_packet.append(0x00)
    Stop_packet.append(0x44)
    Stop_packet.append(0x43)
    Stop_packet.append(0x03)

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
    mCtrlType = 0
    mHeaderVersion = 0
    mHeaderReq = 0
    mHeader = 0
    mDataLen = 0x00
    mCmd = 0x00
    mData = [0x00] * 64
    mCS = 0x00
    mETX = "03"
    
    adcToInit = 0
    #######################

class Protocoll:
    def __init__(self):
        self.cR_Sense = 100000.0  # 100kOhm resistor
        self.cFactor2Pow23 = 8388608.0
        self.first = True
        self.State = 0
        self.Cnt = 0
        self.calcCS = 0
        self.Running = True
        self.Data = [0.0] * 6

    # Calc the Resistor Value ------------------------------------------------------------
    def AnalyseFrame(self):
        #print(Global.mCmd)
        if Global.mCmd.hex() == "61":  # -> 'a'
            # Channel is stored in Global.Data[0]
            VoltageVal = Global.mData[1] * 65536 + Global.mData[2] * 256 + Global.mData[3]
            Resistance = self.cR_Sense * (1 * (self.cFactor2Pow23 - 1.0) / VoltageVal - 1.0)

            # store Resistance in datastruct @ Channel
            self.Data[Global.mData[0]] = Resistance
        else:
            print("No Streaming Data")
            Server.send(Global.ErrorMsg)
        return 0

    # Statemachine to get the Data from UART ---------------------------------------------
    def readByte(self, rxByte):
        if self.first or rxByte == '':  # retMsg
            self.first = False
            self.State = 0
            return False, self.Data

        # State Machine ---------------
        # print(rxByte, end=' ')
        if self.State == 0:  # eControl
            # print("Control: ", end=' ')
            self.calcCS = 0
            self.Cnt = 0
            Global.mCtrlType = rxByte
            self.State += 1

        elif self.State == 1:  # eHeader
            Global.mHeaderVersion = (rxByte[0] & 0xFE)
            Global.mHeaderReq = (rxByte[0] & 0x01)
            Global.mHeader = rxByte
            # print("Header: ", end=' ')
            self.State += 1

        elif self.State == 2:  # eLen
            Global.mDataLen = rxByte
            # print("Len: ", end=' ')
            self.State += 1

        elif self.State == 3:  # eCmd
            Global.mCmd = rxByte
            # print("Cmd: ", end=' ')
            # skip Data State when Len = 0
            if Global.mDataLen == 0:
                self.State += 2
            else:
                self.State += 1

        elif self.State == 4:  # eData
            Global.mData[self.Cnt] = rxByte[0]
            #print("Data[" + str(self.Cnt) + "]:", end=' ')
            self.Cnt += 1
            if self.Cnt >= Global.mDataLen[0]:
                self.State += 1
                self.Cnt = 0

            self.calcCS ^= rxByte[0]

        elif self.State == 5:  # eCS
            # TODO: Add XOR for CS check to all states up to this one

            # if self.calcCS == rxByte:
            #    self.State += 1
            # CS always right :)
            # print("CS: ", end=' ')
            self.State += 1

        elif self.State == 6:  # eEtx
            if Global.mETX == rxByte.hex():
                self.AnalyseFrame()
                # print(Global.mData[0] == Global.adcToInit - 1)
                if Global.mData[0] == (Global.adcToInit - 1):
                    self.State = 0
                    return True, self.Data
                # print("Etx: ", end=' ')
            self.State = 0
        else:
            self.State = 0

        # print(str(rxByte))
        return False, self.Data

class UDPServer:

    def __init__(self):
        # Example Data to test
        self.data = [0.0] * 6
        # address
        self.address = 0

    def send(self, StringToSend):
        if(StringToSend != ""):
            UDPServerSocket.sendto(str.encode(StringToSend), self.address)

    def receive(self):
        byteAddressPair = UDPServerSocket.recvfrom(bufferSize)
        stringReceived = byteAddressPair[0].decode("utf-8")
        #print(stringReceived)
        return stringReceived

    # Init function
    def init(self, msg):
        print("Init")

        # convert string to int value
        Global.adcToInit = int(msg)
        # check if number of ADC's to init is correct
        if Global.adcToInit < 0 or Global.adcToInit > 6:
            Global.adcToInit = 6 # 6 max numbers of ADCs

        ser.flushInput()        
        ser.write(Global.Init_packet[Global.adcToInit - 1])
        while True:
            retMsg = ser.readline()
            hexMsg = retMsg.hex()
            #print(hexMsg)

            if hexMsg == Global.InitDoneMsg:
                print("Init Done")
                self.send(Global.InitOK)
                break           
            print("Not Done yet")

    def start(self):
        # start loop
        while True:
            command = self.receive()
            if command == Global.StartCmd:
                print("Start")  # ---------------------------------------------------

                ser.write(Global.Start_packet)
                while True:
                    retMsg = ser.readline()
                    hexMsg = retMsg.hex()
                    #print(hexMsg)

                    if hexMsg == Global.StartDoneMsg:
                        print("Start Done")
                        self.send(Global.StartOK)
                        break                       
                    print("Not Done yet")
                break
            else:
                self.send(Global.ErrorMsg)

    # stop function
    def stop(self):
        ser.write(Global.Stop_packet)
        print("stopped!!!")      

        self.send(Global.StopOK)

    # ------------------------------------------------------------------

    # main function
    def Communicate(self):
        # initialisation loop
        while True:
            # get cmd and edit it
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            command = bytesAddressPair[0]
            command = command.decode("utf-8")          
            self.address = bytesAddressPair[1]

            # split command to get amount of channels to init
            spCmd = command.split(" ")
            if len(spCmd) > 1 and spCmd[0] == Global.InitCmd:
                # initialize ADCs
                self.init(spCmd[1])
                break
            else:
                self.send(Global.ErrorMsg)

        # start the Board
        self.start()

        # init for status flags
        get = False
        Send = False

        # Sends Data on request -----------------------------------------------------
        UDPServerSocket.setblocking(False)
        while True:
            # Send all Channels at once if main wants it
            if Send == True and get == True:
                # format Data and send
                dataString = str(data[0]) + ';' + str(data[1]) + ';' + str(data[2]) + ';' + str(data[3]) + ';' + str(data[4]) + ';' + str(data[5])
                #print(dataString)
                self.send(dataString)
                get = False

            # read Byte and build a cmd
            retMsg = ser.read()
            Send, data = Protocoll.readByte(proto, retMsg)
            #print(Send)

            # check if there is a request
            r,w,e = select.select([UDPServerSocket], [], [], 0)
            if len(r) == 0: # when r has size 0 no data is available
                #print(Send)
                continue

            command = self.receive()
            if command == Global.StopCmd:
                print("stop")
                break
            if command == Global.GetCmd:
                get = True
            r[0] = 0
            
                      
        UDPServerSocket.setblocking(True)
        self.stop()

if __name__ == "__main__":
    # Create Port Connection
    ser = serial.Serial(port='COM3', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1)
    ser.flushInput()

    # Create a datagram socket / Bind to address and ip
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))

    Server = UDPServer()
    proto = Protocoll()

    print("Reset!!")  # -------------------------------------------------
    ser.write(Global.Reset_packet)
    while True:
        retMsg = ser.readline()
        hexMsg = retMsg.hex()
        #print(hexMsg)

        # check if done
        if hexMsg != Global.ResetDoneMsg:
            print("Reset Done")
            break   
        print("Not Done yet")

    # main loop ---------------------------------------------------------
    while True:
        proto.__init__()
        Server.Communicate()
