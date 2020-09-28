from rpi_ws281x import PixelStrip, Color
import time

COLUMN = 32
ROW = 8

# LED strip configuration:
LED_COUNT = ROW*COLUMN  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    LED_FREQ_HZ,
    LED_DMA,
    LED_INVERT,
    LED_BRIGHTNESS,
    LED_CHANNEL,
)


def xy_to_arrayIndex(x, y):
    if x % 2 == 0:
        return (x * 8) + y
    else:
        return (x * 8) + (8 - y - 1)


# Main program logic follows:
if __name__ == "__main__":
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # step 1 - light single LED
    strip.setPixelColor(xy_to_arrayIndex(0, 0), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(1, 1), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(2, 2), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(3, 3), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(4, 4), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(5, 5), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(6, 6), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)
    strip.setPixelColor(xy_to_arrayIndex(7, 7), Color(100, 0, 0))
    strip.show()
    time.sleep(50/1000)

    # step 2 - loop all
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(100, 0, 0))
        strip.show()
        time.sleep(50 / 1000)

    # clean all
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))

    strip.show()
