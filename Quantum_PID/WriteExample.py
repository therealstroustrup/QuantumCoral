import time
from SmartTexServer import Writer


def GenerateData():
    # Single Datapoints - must match labellength
    Points = [12,12,12,300,350, 32.4, 35.3, 500, 550, 600, 650, 700, 750]
    Time = round(time.time() * 1000)

    # Multiple Datapoints
    #Points = []
    #Time = []

    # Append Data to Buffer with timestamps
    MyWriter.WriteTime(Points, Time)


if __name__ == '__main__':
    Database = "Quantum"
    Measurement = "Testsetup"

    MyWriter = Writer(Database, Measurement)

    MyWriter.AddLabel("Motorposition_1")
    MyWriter.AddLabel("Motorposition_2")
    MyWriter.AddLabel("Motorposition_3")

    MyWriter.AddLabel("Forcesensor_1")
    MyWriter.AddLabel("Forcesensor_2")

    MyWriter.AddLabel("Temperature_1")
    MyWriter.AddLabel("Temperature_2")

    MyWriter.AddLabel("ADC_1")
    MyWriter.AddLabel("ADC_2")
    MyWriter.AddLabel("ADC_3")
    MyWriter.AddLabel("ADC_4")
    MyWriter.AddLabel("ADC_5")
    MyWriter.AddLabel("ADC_6")

    MyWriter.Start(10)

    while True:
        time.sleep(1)
        GenerateData()
        # print("I am still alive...")

