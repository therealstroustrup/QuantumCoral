from periphery import PWM

# Open PWM chip 0, channel 10
pwm = PWM(0, 0)

# Set frequency to 1 kHz
pwm.frequency = 1e3
# Set duty cycle to 75%
pwm.duty_cycle = 1

pwm.enable()

while True:
   continue 

pwm.close()
