import subprocess
import json
from SpectreMqtt import SpectreMqtt

import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.device import Device

configuration = spectre_api_client.Configuration(
    host = "https://smarttexserver.projekte.fh-hagenberg.at/icapi"
)

spectreApiClient = spectre_api_client.ApiClient(configuration)


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def newMissionCallback(mission):
    subprocess.call(["callbacks/NewMission.py", mission], shell=True)
    print(mission)

def liveMissionStartCallback(mission):
    subprocess.call(["callbacks/LiveMissionStart.py", mission], shell=True)
    print(mission)

def liveMissionStopCallback(mission):
    subprocess.call(["callbacks/LiveMissionStop.py", mission], shell=True)
    print(mission)

def liveMissionCommandCallback(mission):
    f = open("CommandLogFile.txt", "a")
    f.write("Mission:" + mission['befehl'] + "\n")
    f.close()

    subprocess.call(["python3", "callbacks/LiveMissionCommand.py", mission['befehl']])
    print(mission)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def testSpectreMqtt():
    spectreClient = SpectreMqtt(151)
    spectreClient.sendHeartbeat("Active")

    spectreClient.newMissionCallback = newMissionCallback
    spectreClient.liveMissionStartCallback = liveMissionStartCallback
    spectreClient.liveMissionStopCallback = liveMissionStopCallback
    spectreClient.liveMissionCommandCallback = liveMissionCommandCallback

    spectreClient.loopForever()

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
if __name__ == "__main__":
    testSpectreMqtt()


