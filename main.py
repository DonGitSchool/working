def on_button_pressed_a():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def WTF():
    global temp
    strip.set_brightness(20)
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P1, True, False, True)
    dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
    basic.pause(1000)
    temp = dht11_dht22.read_data(dataType.TEMPERATURE)
    basic.show_string("" + str(temp))
    if temp <= 20:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
    elif temp > 80 and temp <= 90:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.RED))
    elif temp > 90 and temp <= 100:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.RED))
    elif temp > 40 and temp <= 50:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
    elif temp > 50 and temp <= 60:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.RED))
    elif temp > 60 and temp <= 70:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.RED))
    elif temp > 70 and temp <= 80:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    strip.show()
def joinnet():
    ESP8266_IoT.connect_wifi("ZorraNet", "ZorranRokz.!")
    basic.pause(1000)

def on_button_pressed_b():
    WTF()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_data_received():
    basic.show_string(serial.read_until(serial.delimiters(Delimiters.NEW_LINE)))
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

temp = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("ZorraNet", "ZorranRokz.!")
strip.set_brightness(20)

def on_every_interval():
    global temp
    strip.set_brightness(20)
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P1, True, False, True)
    dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
    basic.pause(1000)
    temp = dht11_dht22.read_data(dataType.TEMPERATURE)
    basic.show_string("" + str(temp))
    if temp <= 20:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
    elif temp > 80 and temp <= 90:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.RED))
    elif temp > 90 and temp <= 100:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.RED))
    elif temp > 40 and temp <= 50:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
    elif temp > 50 and temp <= 60:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.RED))
    elif temp > 60 and temp <= 70:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.RED))
    elif temp > 70 and temp <= 80:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    strip.show()

loops.every_interval(5000, on_every_interval)
