#from periphery import PWM

# pip install python-periphery
# use PWM chip 0, channel 0 --> PWM1 Pin 32


class stamp:
    
    def __init__(self):
        #self.__pwm = PWM(0, 0)
        self.__filename = "dutycycle.txt"

    def init(self):
        # self.__pwm.frequency = 1e3             # set frequency to 1kHz, Voltage: 3.3V
        # self.__pwm.duty_cycle = 0              # ground the stamp after intialising
        # self.__pwm.enable()
        pass

    def control(self, duty):
        file = open(self.__filename, 'w')
        file.write(str(duty))
        file.close()

        # self.__pwm.duty_cycle = duty / 100   # extend stamp to required height

    def up(self):
        file = open(self.__filename, 'r+')
        current_duty = int(file.read())

        if current_duty < 100:
            current_duty += 1
            file.truncate(0)
            file.seek(0)
            file.write(str(current_duty))

        file.close()
        # self.__pwm.duty_cycle = current_duty / 100

    def down(self):
        file = open(self.__filename, 'r+')
        current_duty = int(file.read())

        if current_duty > 0:
            current_duty -= 1
            file.truncate(0)
            file.seek(0)
            file.write(str(current_duty))

        file.close()
        # self.__pwm.duty_cycle = current_duty / 100

    def get_duty(self):
        file = open(self.__filename, 'r')
        duty = file.read()
        file.close()
        return duty

    def end(self):
        self.control(0)                        # ground the stamp before shutting down
        #self.__pwm.close()


class lin_motor:                                # placeholder for linear motor driver
    def init(self):
        pass
