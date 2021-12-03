import time
import queue
import datetime
from timeloop import Timeloop
from datetime import timedelta
import numpy as np
import scipy.io as spio     # Used in ReadTimerange for export as .mat
from influxdb import InfluxDBClient  # works in InfluxDB 1.8, does not work with tokens, requires user and password store
import dateutil
import pandas as pd
#from influxdb_client import InfluxDBClient # works in InfluxDB 2.0, different write access, needs to be adjusted
import os
import csv


class Writer:
    def __init__(self, Database, Measurement):
        Writer._myDatabase = Database
        Writer._myMeasurement = Measurement
        Writer._myStreamIntervall = 0
        #Writer._myClient = InfluxDBClient(url='https://smarttexserver.projekte.fh-hagenberg.at:8086', token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwZWN0cmUiLCJleHAiOjE2NzA4NDY0MDB9.TqmrfOVzf4zjDWGt0NZS2tcpDNZjhiQ_J19a3Dvz-4Y", org="Embedded Systems Lab")
        Writer._myClient = InfluxDBClient(host='smarttexserver.projekte.fh-hagenberg.at', port=8086, username='spectre', password='!Q@DLe6FaD7w', ssl=True, verify_ssl=True)
        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwZWN0cmUiLCJleHAiOjE2NzA4NDY0MDB9.TqmrfOVzf4zjDWGt0NZS2tcpDNZjhiQ_J19a3Dvz-4Y
        #https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwZWN0cmUiLCJleHAiOjE2NzA4NDY0MDB9.TqmrfOVzf4zjDWGt0NZS2tcpDNZjhiQ_J19a3Dvz-4Y

        Writer._myClient.create_database(Writer._myDatabase)
        print("Python: Writer connected.")

        Writer._data = queue.Queue()
        Writer._labels = []
        Writer._myID = 0

    # Configuration Functions
    @staticmethod
    def Database(Database):
        Writer._myDatabase = Database
    @staticmethod
    def Database():
        return Writer._myDatabase
    @staticmethod
    def ID(id):
        Writer._myID = id
    @staticmethod
    def AddLabel(Label):
        Writer._labels.append(Label)

    @staticmethod
    def WaitForTransmission(Delay):
        while Writer.Buffer() != 0:
            print("Python: Waiting for ", Writer.Buffer(), " Datapoints.")
            time.sleep(Delay);

    @staticmethod
    def SendBuffers(times, signals):
        startTime = round(time.time() * 1000);
        pos = 0
        for idx in times['time']:
            Values = signals['signals'][:,pos];
            times.WriteTime(Values, startTime + idx * 1000)
            pos = pos + 1;

    @staticmethod
    def ReadLabels(file):
        with open('tmp/fromMatlab/labels.txt') as f:
            labels = f.readlines()
            labels = [x.strip() for x in labels]
        for label in labels:
            Writer._labels.append(label)

    @staticmethod
    def GetLabels():
        Labelstring = ""
        for x in range(len(Writer._labels)):
            Labelstring += Writer._labels[x] + "={" + Writer._labels[x] + "},"
            #print(Writer._labels[x], end = ' ')
        #print("")
        return Labelstring[:-1]
    # Configuration Functions
    @staticmethod
    def Buffer():
        return len(Writer._data.queue)

    # Write Vector of datapoints to list - uses local timestamp
    @staticmethod
    def Write(Points):
        if (len(Writer._labels) != len(Points)):
            raise Exception('Number of points ({}) and labels ({}) do not match.'.format(len(Points), len(Writer._labels)))
            return
        else:
            StartString = Writer._myFrontLabels.format(measurement=Writer._myMeasurement, id=Writer._myID)
            EndString = Writer._myBackLabels.format(timestamp=int(time.time() * 1000))

            DataString = ""
            for x in range(len(Writer._labels)-1):
                DataString += Writer._labels[x] + "=" + str(Points[x]) + ","
            DataString += Writer._labels[len(Writer._labels)-1] + "=" + str(Points[len(Writer._labels)-1])

            Writer._data.put(StartString + DataString + EndString)

    # Write Vector of datapoints to list
    @staticmethod
    def WriteTime(Points, Time):
        if (len(Writer._labels) != len(Points)):
            raise Exception('Number of points ({}) and labels ({}) do not match.'.format(len(Points), len(Writer._labels)))
            return
        else:
            StartString = Writer._myFrontLabels.format(measurement=Writer._myMeasurement, id=Writer._myID)
            EndString = Writer._myBackLabels.format(timestamp=int(Time))

            DataString = ""
            for x in range(len(Writer._labels)-1):
                DataString += Writer._labels[x] + "=" + str(Points[x]) + ","
            DataString += Writer._labels[len(Writer._labels)-1] + "=" + str(Points[len(Writer._labels)-1])

            Writer._data.put(StartString + DataString + EndString)

    # Start periodical transmission of sensor data
    @staticmethod
    def Start(StreamIntervall):
        Writer._myStreamIntervall = StreamIntervall
        Writer._myFrontLabels = "{measurement},id={id} "
        Writer._myCenterLabels = Writer.GetLabels()
        Writer._myBackLabels =  " {timestamp}"

        Writer._myLabels = Writer._myFrontLabels + Writer._myCenterLabels + Writer._myBackLabels
        Writer._tl = Timeloop()
        @Writer._tl.job(interval=timedelta(seconds=Writer._myStreamIntervall))
        def write_to_influx():
            databuff = [Writer._data.get() for _ in range(Writer._data.qsize())]
            Writer._myClient.write_points(databuff, database=Writer._myDatabase, time_precision='ms', batch_size=len(databuff), protocol='line')
        Writer._tl.start(block=False)

class Reader:
    def __init__(self, Database, Measurement):
        Reader._myDatabase = Database
        Reader._myMeasurement = Measurement
        Reader._myStreamIntervall = 0
        Reader._myCallbackFunc = 0
        Reader._myClient = InfluxDBClient(host='smarttexserver.projekte.fh-hagenberg.at', port=8086, username='spectre', password='!Q@DLe6FaD7w', ssl=True, verify_ssl=True)
        Reader._myClient.switch_database(Reader._myDatabase)
        print("Python: Reader connected.")

        Reader._data = queue.Queue()
        Reader._labels = []
        Reader._myID = 0

    # Configuration Functions
    @staticmethod
    def Database(Database):
        Reader._myDatabase = Database
    @staticmethod
    def Database():
        return Reader._myDatabase
    @staticmethod
    def ID(id):
        Reader._myID = id
    @staticmethod
    def AddLabel(Label):
        Reader._labels.append(Label)
    @staticmethod
    def GetLabels():
        Labelstring = ""
        for x in range(len(Reader._labels)):
            Labelstring += Reader._labels[x] + "={" + Reader._labels[x] + "},"
            #print(Reader._labels[x], end = ' ')
        #print("")
        return Labelstring[:-1]
    @staticmethod
    def ReadDuration(Label, Duration):
        groupBy = '1ms'
        getcurrentTime = round(time.time() * 1000)
        StartTime = round(time.time() * 1000)
        StopTime = StartTime + Duration
        #QueryString = "SELECT mean(\"" + Label + "\") FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + StartTime +  " AND time <= " + EndTime + ' GROUP BY time(' + groupBy + ') fill(null);'
        QueryString = "SELECT \"" + Label + "\" FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + str(StartTime) +  "ms AND time <= " + str(StopTime) + "ms"
        results = Reader._myClient.query(QueryString)
        points = results.raw

        Series = points['series'][0]['values']
        arr = np.array(Series)
        Time = np.delete(arr,1,1)
        Time = np.concatenate(Time)

        Value = np.delete(arr,0,1)
        Value = np.concatenate(Value)
        Value.astype(float)

        # Callback
        Reader._myCallbackFunc(Time, Value)

    @staticmethod
    def ReadTimerange(Start, Stop, LabelList):
        groupBy = '1ms'
        #getcurrentTime = round(time.time() * 1000)
        #StartTime = round(time.time() * 1000) - Duration
        #StopTime = StartTime + Duration
        if not os.path.exists('tmp/fromPython'):
            os.makedirs('tmp/fromPython')
        for Label in LabelList:
            QueryString = "SELECT \"" + Label + "\" FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + str(Start) +  "ms AND time <= " + str(Stop) + "ms"
            results = Reader._myClient.query(QueryString)
            points = results.raw

            if (points['series'].__len__() == 0):
                print("Python: Timerange or labels returned no results.")
                return

            Series = points['series'][0]['values']
            arr = np.array(Series)
            Time = np.delete(arr,1,1)
            Time = np.concatenate(Time)

            Value = np.delete(arr,0,1)
            Value = np.concatenate(Value)
            Value.astype(float)

            fTime = np.zeros(len(Time), dtype=float)
            for idx, Timestring in enumerate(Time):
                fTime[idx] = (time.mktime(dateutil.parser.parse(Timestring).timetuple())+(dateutil.parser.parse(Timestring).microsecond)/1000000)
            MyMatrix = [fTime, Value.astype(np.float)]
            Label = Label.replace("(", "_");
            Label = Label.replace(")", "");
            mdic = {'Matrix' : MyMatrix,'label': Label}
            Name = str("tmp/fromPython/" + Label + ".mat")
            spio.savemat(Name, mdic)

    @staticmethod
    def ReadTimerangeIntoCSV(Start, Stop, LabelList):
        groupBy = '1ms'
        #getcurrentTime = round(time.time() * 1000)
        #StartTime = round(time.time() * 1000) - Duration
        #StopTime = StartTime + Duration
        for Label in LabelList:
            QueryString = "SELECT \"" + Label + "\" FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + str(Start) +  "ms AND time <= " + str(Stop) + "ms"
            results = Reader._myClient.query(QueryString)
            points = results.raw

            if (points['series'].__len__() == 0):
                print("Python: Timerange or labels returned no results.")
                return

            Series = points['series'][0]['values']
            arr = np.array(Series)
            Time = np.delete(arr,1,1)
            Time = np.concatenate(Time)

            Value = np.delete(arr,0,1)
            Value = np.concatenate(Value)
            Value.astype(float)

            fTime = np.zeros(len(Time), dtype=float)
            for idx, Timestring in enumerate(Time):
                fTime[idx] = (time.mktime(dateutil.parser.parse(Timestring).timetuple())+(dateutil.parser.parse(Timestring).microsecond)/1000000)

            MyMatrix = [fTime, Value.astype(np.float)]
            MyMatrix = np.transpose(MyMatrix)
            Label = Label.replace("(", "_");
            Label = Label.replace(")", "");
            mdic = {'Matrix' : MyMatrix,'label': Label}

            Name = str(Label + ".mat")
            np.savetxt(str(Label + ".csv"), MyMatrix[:], delimiter="; ")
            spio.savemat(Name, mdic)


    @staticmethod
    def ReadLabelsList(LabelList, Duration):
        groupBy = '1ms'
        getcurrentTime = round(time.time() * 1000)
        StartTime = round(time.time() * 1000) - Duration
        StopTime = StartTime + Duration
        for Label in LabelList:
            QueryString = "SELECT \"" + Label + "\" FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + str(StartTime) +  "ms AND time <= " + str(StopTime) + "ms"
            results = Reader._myClient.query(QueryString)
            points = results.raw

            if (points['series'].__len__() == 0):
                print("Python: Timerange or labels returned no results.")
                return

            Series = points['series'][0]['values']
            arr = np.array(Series)
            Time = np.delete(arr,1,1)
            Time = np.concatenate(Time)

            Value = np.delete(arr,0,1)
            Value = np.concatenate(Value)
            Value.astype(float)

            # Callback
            Reader._myCallbackFunc(Label, Time, Value)

    @staticmethod
    def Read(Label, StartTime, EndTime):
        groupBy = '1ms'
        #QueryString = "SELECT mean(\"" + Label + "\") FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + StartTime +  " AND time <= " + EndTime + ' GROUP BY time(' + groupBy + ') fill(null);'
        QueryString = "SELECT \"" + Label + "\" FROM \"autogen\".\"" + Reader._myMeasurement + "\" WHERE time >= " + StartTime +  " AND time <= " + EndTime
        results = Reader._myClient.query(QueryString)
        points = results.raw

        Series = points['series'][0]['values']
        arr = np.array(Series)
        Time = np.delete(arr,1,1)
        Time = np.concatenate(Time)

        Value = np.delete(arr,0,1)
        Value = np.concatenate(Value)
        Value.astype(float)

        # Callback
        Reader._myCallbackFunc(Label, Time, Value)

    @staticmethod
    def RegisterCallback(functionHandle):
    	Reader._myCallbackFunc = functionHandle
    # Start periodical transmission of sensor data
    @staticmethod
    def Start(StreamIntervall):
        Writer._myStreamIntervall = StreamIntervall
        if (Reader._myCallbackFunc != 0):
            Reader._myFrontLabels = "{measurement},id={id} "
            Reader._myCenterLabels = Reader.GetLabels()
            Reader._myBackLabels =  " {timestamp}"

            Reader._myLabels = Reader._myFrontLabels + Reader._myCenterLabels + Reader._myBackLabels
            Reader._tl = Timeloop()

            InfluxTime1 = 1612550000  # 20:45 - ms
            InfluxTime2 = 1612559000  # 21:00 - ms
            CurrentTime = int(time.time() * 1000)

            @Reader._tl.job(interval=timedelta(seconds=Reader._myStreamIntervall))
            def read_from_influx():
                # Do reading
                #time >= '2015-08-18T00:00:00Z' AND time <= '2015-08-18T00:30:00Z'
                Start = datetime.datetime.fromtimestamp(InfluxTime1)
                End = datetime.datetime.fromtimestamp(InfluxTime2)

                Start = Start.strftime("%Y-%m-%dT%H:%M:%SZ")
                End = End.strftime("%Y-%m-%dT%H:%M:%SZ")

                QueryString = "SELECT \"CPU\" FROM \"autogen\".\"PerformancePC\" WHERE time >= '" + Start +  "' AND time <= '" + End + "'"
                #QueryString += str(datetime.datetime.fromtimestamp(InfluxTime1/1000)).replace(' ','T')
                #QueryString += "Z'"
                #QueryString += " AND time <= '"
                #QueryString += str(datetime.datetime.fromtimestamp(InfluxTime2/1000)).replace(' ','T')
                #QueryString += "Z'"

                #CurrentTime = time.time()
                #Lower = datetime.datetime.fromtimestamp(InfluxTime1)
                #Delta1 = CurrentTime - Lower

                #CurrentTime = time.time()
                #Upper = datetime.datetime.fromtimestamp(InfluxTime2)
                #Delta2 = CurrentTime - Upper

                #QueryString = 'SELECT "CPU" FROM "autogen"."PerformancePC" WHERE time < now() - ' + Delta1.total_seconds() + ' AND time > now() - 4h'

                results = Reader._myClient.query(QueryString)
                points = results.raw

                Series = points['series'][0]['values']
                arr = np.array(Series)
                Time = np.delete(arr,1,1)
                Time = np.concatenate(Time)

                Value = np.delete(arr,0,1)
                Value = np.concatenate(Value)
                Value.astype(float)
                Value = Value[1:1000]

                # Callback
                Reader._myCallbackFunc(Time, Value)

            Reader._tl.start(block=False)
