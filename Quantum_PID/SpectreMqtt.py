import paho.mqtt.client as mqtt
import json

TopicHeartbeat = "spies/{id}/heartbeat"
TopicPing = "spies/{id}/ping"
TopicNewMission = "spies/{id}/missions/new"
TopicLiveMissionStart = "spy/{id}/missions/live/start"
TopicLiveMissionStop = "spy/{id}/missions/live/stop"
TopicLiveMissionCommand = "spy/{id}/missions/live/command"

class SpectreMqtt:
    """
    Client to interact with Spectre MQTT Broker

    Args:
        spyId: ID of the current spy

    Attributes:
        newMissionCallback: Callback function to be called, when a new mission is received
            Paramters of callback:
                Mission as Dictionary
        liveMissionStartCallback: Callback function to be called, when a live mission is started
            Paramters of callback:
                Mission ID
        liveMissionStopCallback: Callback function to be called, when a live mission is stopped
            Paramters of callback:
                Mission ID
        liveMissionCommandCallback: Callback function to be called, when a new command is received for a live mission
            Parameters of callback:
                Command as Dictonary

    Misc:
    Structure of Mission:
    {
        "id":	        integer($int64)
        "name":	        string
        "description":	string
        "scheduled":	string($date-time)
        "dashboardUrl":	string
        "live":	        boolean
        "status":	    stringEnum: [ "Pending", "Initializing", "Running", "Success", "Error" ]
        "spy":	        integer($int64)
        "firmware":	    integer($int64)
        "dataseries":	integer($int64)
        "user": 	    integer($int64)
        "textile":	    integer($int64)
    }
    Structure of Command:
    {
        "id":	        integer($int64)
        "textCommand":	string
        "delayMs":	    integer
        "device":	    integer($int64)
        "mission":	    integer($int64)
    }
    """

    def __init__(self, spyId: int):
        # Populate misc private variables
        self.__topicHeartbeat = TopicHeartbeat.format(id=spyId)
        self.__topicPing = TopicPing.format(id=spyId)
        self.__topicNewMission = TopicNewMission.format(id=spyId)
        self.__topicLiveMissionStart = TopicLiveMissionStart.format(id=spyId)
        self.__topicLiveMissionStop = TopicLiveMissionStop.format(id=spyId)
        self.__topicLiveMissionCommand = TopicLiveMissionCommand.format(id=spyId)
        self.__lastStatus = "Offline"

        # Init client
        self.__client = mqtt.Client()
        self.__client.connect("smarttexserver.projekte.fh-hagenberg.at", port=3000)
        self.__client.on_message = self.__onMessage

        # Subscribe
        self.__addCallback(self.__topicPing, self.__onPing)
        self.__addCallback(self.__topicNewMission, self.__onNewMission)
        self.__addCallback(self.__topicLiveMissionStart, self.__onLiveMissionStart)
        self.__addCallback(self.__topicLiveMissionStop, self.__onLiveMissionStop)
        self.__addCallback(self.__topicLiveMissionCommand, self.__onLiveMissionCommand)

        # Callback functions
        self.newMissionCallback = None
        self.liveMissionStartCallback = None
        self.liveMissionStopCallback = None
        self.liveMissionCommandCallback = None

    def sendHeartbeat(self, status: str):
        """
        Sends heartbeat to the MQTT broker

        status: Current status of the spy. Possible values: "Inactive", "Active", "Offline", "Error", "Live"
        """
        self.__lastStatus = status

        message = { "status": status }
        self.__client.publish(self.__topicHeartbeat, payload=json.dumps(message))

    def loopForever(self):
        """
        Starts loop to handle MQTT network traffic. This call is synchronous, thus it blocks the calling thread.
        """

        self.__client.loop_forever()

    def loop(self, timeout=1):
        """
        Starts loop to handle MQTT network traffic.
        This call returns after <timeout> seconds and must be called regularly to process incoming traffic.

        timeout: Timeout in seconds after which the call returns
        """

        self.__client.loop(timeout)

    def loopStart(self):
        """
        Starts loop to handle MQTT network traffic in a separate thread.
        """

        self.__client.loop_start()

    def loopStop(self):
        """
        Stops the thread, which has been started with loopStart()
        """

        self.__client.loop_stop()

    def __onMessage(self, client, userdata, msg: mqtt.MQTTMessage):
        print(f"{msg.topic}: {msg.payload}")

    def __onPing(self, client, userdata, msg: mqtt.MQTTMessage):
        print(f"Ping received: {msg.payload}")
        self.sendHeartbeat(self.__lastStatus)

    def __onNewMission(self, client, userdata, msg: mqtt.MQTTMessage):
        if callable(self.newMissionCallback):
            mission = json.loads(msg.payload)
            self.newMissionCallback(mission)

    def __onLiveMissionStart(self, client, userdata, msg: mqtt.MQTTMessage):
        if callable(self.liveMissionStartCallback):
            idObj = json.loads(msg.payload)
            self.liveMissionStartCallback(idObj["id"])

    def __onLiveMissionStop(self, client, userdata, msg: mqtt.MQTTMessage):
        if callable(self.liveMissionStopCallback):
            idObj = json.loads(msg.payload)
            self.liveMissionStopCallback(idObj["id"])

    def __onLiveMissionCommand(self, client, userdata, msg: mqtt.MQTTMessage):
        if callable(self.liveMissionCommandCallback):
            idObj = json.loads(msg.payload)
            self.liveMissionCommandCallback(idObj)

    def __addCallback(self, subscriptionName, callback):
        if not callable(callback):
            raise ValueError("callback must be a function")

        self.__client.message_callback_add(subscriptionName, callback)
        self.__client.subscribe(subscriptionName)

    def __removeCallback(self, subscriptionName):
        self.__client.unsubscribe(subscriptionName)
        self.__client.message_callback_remove(subscriptionName)
