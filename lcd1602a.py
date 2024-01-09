"""Implements a HD44780 character LCD connected via ESP32 GPIO pins."""

from machine import Pin
from esp32_gpio_lcd import GpioLcd
from utime import sleep_ms, ticks_ms

# Wiring used for this example:
#
#  1 - Vss (aka Ground) - Connect to one of the ground pins on you board.
#  2 - VDD - I connected to VIN which is 5 volts when your board is powered via USB
#  3 - VE (Contrast voltage) - I'll discuss this below
#  4 - RS (Register Select) connect to D15 (as per call to GpioLcd)
#  5 - RW (Read/Write) - connect to ground
#  6 - EN (Enable) connect to D2 (as per call to GpioLcd)
#  7 - D0 - connect to D26 (as per call to GpioLcd)
#  8 - D1 - connect to D25 (as per call to GpioLcd)
#  9 - D2 - connect to D33 (as per call to GpioLcd)
# 10 - D3 - connect to D32 (as per call to GpioLcd)
# 11 - D4 - connect to D4 (as per call to GpioLcd)
# 12 - D5 - connect to D23 (as per call to GpioLcd)
# 13 - D6 - connect to D22 (as per call to GpioLcd)
# 14 - D7 - connect to D5 (as per call to GpioLcd)
# 15 - A (BackLight Anode) - Connect to VIN
# 16 - K (Backlight Cathode) - Connect to Ground
#
# On 14-pin LCDs, there is no backlight, so pins 15 & 16 don't exist.
#
# The Contrast line (pin 3) typically connects to the center tap of a
# 10K potentiometer, and the other 2 legs of the 10K potentiometer are
# connected to pins 1 and 2 (Ground and VDD)
#
# The wiring diagram on the following page shows a typical "base" wiring:
# http://www.instructables.com/id/How-to-drive-a-character-LCD-displays-using-DIP-sw/step2/HD44780-pinout/
# Add to that the EN, RS, and D4-D7 lines.


def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    lcd = GpioLcd(rs_pin=Pin(15),
                  enable_pin=Pin(2),
                  d0_pin=Pin(26),
                  d1_pin=Pin(25),
                  d2_pin=Pin(33),
                  d3_pin=Pin(32),
                  d4_pin=Pin(4),
                  d5_pin=Pin(23),
                  d6_pin=Pin(22),
                  d7_pin=Pin(5),
                  num_lines=2, num_columns=16)

    lcd.clear()
    lcd.putstr("Hello world")
    sleep_ms(1000)
    lcd.clear()
    lcd.putstr("*** Welcome to CN ***")
    sleep_ms(1000)
    lcd.clear()
    lcd.putstr("I love Shanghai")
    sleep_ms(3000)
    lcd.clear()

    count = 0
    while True:
        lcd.move_to(0, 0)
        lcd.putstr("show number:")
        lcd.putstr("%10d" % (ticks_ms() // 1000))  # 改变%7d的数字就可以调节显示位置
        sleep_ms(1000)
        count += 1

test_main()
