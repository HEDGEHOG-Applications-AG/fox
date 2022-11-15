from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from utime import sleep_ms

WIDTH =128
HEIGHT= 64

MAX_PWM = 65534
MAX_RGB = 255

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
    
def screen_contents():
    oled.fill(1)

    oled.show()
    
# 0 = Left, 1 = Right
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

setup()

C_MAX = 40

SLEEP_T = 10

R = 40
G = 0
B = 0

while(1):
    #100
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        R = R - 1
        G = G + 1
        sleep_ms(SLEEP_T)
    #010    
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        R = R + 1
        sleep_ms(SLEEP_T)
    #110    
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        R = R - 1
        G = G - 1
        B = B + 1
        sleep_ms(SLEEP_T)
    #001    
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        R = R + 1
        sleep_ms(SLEEP_T)
    #101    
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        R = R - 1
        G = G + 1
        sleep_ms(SLEEP_T)
    #011    
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        R = R + 1
        sleep_ms(SLEEP_T)
    #111    
    for i in range(C_MAX):
        setLED(0, R, G, B)
        setLED(1, C_MAX - R, C_MAX - G, C_MAX - B)
        G = G - 1
        B = B - 1
        sleep_ms(SLEEP_T)
        
