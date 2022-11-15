from machine import Pin, I2C, PWM, ADC
from ssd1306 import SSD1306_I2C
from time import sleep
from math import log

WIDTH =128
HEIGHT= 64

MAX_PWM = 65534
MAX_RGB = 255

BETA = 3950
KELVIN_CONSTANT = 273.15

#setup
sda = Pin(6, Pin.PULL_UP)
scl = Pin(7, Pin.PULL_UP)

i2c=I2C(1,scl=scl,sda=sda,freq=200000)

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

MC_LED_B = Pin(20, Pin.OUT)
MC_LED_G = Pin(19, Pin.OUT)
MC_LED_R = Pin(18, Pin.OUT)

FOX_LED_R_B = PWM(Pin(0))
FOX_LED_R_G = PWM(Pin(2))
FOX_LED_R_R = PWM(Pin(1))

FOX_LED_L_B = PWM(Pin(29))
FOX_LED_L_G = PWM(Pin(27))
FOX_LED_L_R = PWM(Pin(28))

thermistor_pin = ADC (26)

push_button = Pin(23, Pin.IN)

def setup():
    MC_LED_B.value(1)
    MC_LED_G.value(1)
    MC_LED_R.value(1)

    FOX_LED_R_B.duty_u16(MAX_PWM)
    FOX_LED_R_G.duty_u16(MAX_PWM)
    FOX_LED_R_R.duty_u16(MAX_PWM)

    FOX_LED_L_B.duty_u16(MAX_PWM)
    FOX_LED_L_G.duty_u16(MAX_PWM)
    FOX_LED_L_R.duty_u16(MAX_PWM)
    
def setText(text):
    oled.fill(0)
    oled.text("Temp:", 0, 0)
    oled.text(text, 0, 20)
    oled.text("Grad", 20, 20)
    oled.show()
    
# 0 = Left, 1 = Right. Red, Green, Blue Values from 0 to 255
def setLED(ID, Red, Green, Blue):
    PWM_Blue = int((MAX_RGB - Blue) / MAX_RGB * MAX_PWM)
    PWM_Green = int((MAX_RGB - Green) / MAX_RGB * MAX_PWM)
    PWM_Red = int((MAX_RGB - Red) / MAX_RGB * MAX_PWM)
    
    if ID == 0:
        FOX_LED_L_B.duty_u16(PWM_Blue)
        FOX_LED_L_G.duty_u16(PWM_Green)
        FOX_LED_L_R.duty_u16(PWM_Red)
    if ID == 1:
        FOX_LED_R_B.duty_u16(PWM_Blue)
        FOX_LED_R_G.duty_u16(PWM_Green)
        FOX_LED_R_R.duty_u16(PWM_Red)
    
def adc_to_celsius (x):
    return (1 / (log (1/(65535/x - 1))/BETA + 1/298.15) - KELVIN_CONSTANT)

setup()

setLED(0, 0, 20, 20)
setLED(1, 0, 20, 20)

setText("Hedgehog")

while True:
    thermistor_value = thermistor_pin.read_u16()
    setText(str(round(adc_to_celsius(thermistor_value))))
    logic_state = push_button.value()
    if logic_state == True:
        setLED(0, 200, 20, 20)
    else:
        setLED(0, 0, 200, 20) 
    
    sleep (0.1)
    
    
