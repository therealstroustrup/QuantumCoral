from SpectreMqtt import SpectreMqtt

def callback(mission):
    print(mission)

def SpectreMqttClient():
    # Quantum is 124
    spectreClient = SpectreMqtt(124)
    spectreClient.sendHeartbeat("Active")

    spectreClient.newMissionCallback = callback
    spectreClient.liveMissionStartCallback = callback
    spectreClient.liveMissionStopCallback = callback
    spectreClient.liveMissionCommandCallback = callback

    spectreClient.loopForever()

if __name__ == "__main__":
    SpectreMqttClient()
