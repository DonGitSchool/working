def on_button_pressed_a():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    if ESP8266_IoT.wifi_state(True):
        ESP8266_IoT.connect_wifi("Fakr", "asd")
    else:
        ESP8266_IoT.connect_wifi("ZorraNet", "ZorranRokz.!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("" + str((pins.analog_read_pin(AnalogPin.P0))))
    strip.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_data_received():
    basic.show_string(serial.read_until(serial.delimiters(Delimiters.NEW_LINE)))
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

temp = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("ZorraNet", "ZorranRokz.!")
RTC_DS1307.date_time(2022, 2, 22, 16, 15, 30)

def on_forever():
    if temp <= 20:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif temp >= 21 and temp <= 30:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif temp >= 31 and temp <= 40:
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    elif temp >= 41 and temp <= 50:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    elif temp >= 51 and temp <= 60:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
basic.forever(on_forever)

def on_forever2():
    global temp
    temp = (pins.analog_read_pin(AnalogPin.P1) - 273.15) * 1.4 + 32
    basic.pause(5000)
basic.forever(on_forever2)
