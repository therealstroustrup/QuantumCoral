from periphery import PWM
import time

pwm = PWM(0, 0)  # use PWM chip 0, channel 0 --> PWM1 Pin 32


def init():
    pwm.frequency = 1e3  # set frequency to 1kHz, Voltage: 3.3V
    pwm.duty_cycle(0)  # ground the stamp after intialising
    pwm.enable()


def control(duty):
    pwm.duty_cycle(duty)  # extend stamp to required height


def end():
    control(0)  # ground the stamp before shutting down
    pwm.close()


if __name__ == "__main__":
    init()
    time.sleep(5)
    control(50)
    time.sleep(5)
    control(25)
    time.sleep(5)
    control(75)
    time.sleep(5)
    control(10)
    time.sleep(5)
    control(100)
    time.sleep(5)
    end()




