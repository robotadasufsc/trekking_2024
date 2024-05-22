import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import time

navigator.init()
navigator.set_pwm_freq_hz(50)

navigator.set_pwm_enable(True)

x = 0.06
while x < 1:
    navigator.set_pwm_channel_duty_cycle(PwmChannel.Ch1, x)
    time.sleep(0.1)
    x += 0.001
    #print(x)
    if x > 0.15:
        x = 0.06


