def on_button_pressed_a():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    if ESP8266_IoT.wifi_state(True):
        ESP8266_IoT.connect_wifi("Fakr", "asd")
    else:
        ESP8266_IoT.connect_wifi("ZorraNet", "ZorranRokz.!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def WTF():
    global temp
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P1, True, False, True)
    dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
    temp = dht11_dht22.read_data(dataType.TEMPERATURE)
    basic.show_string("" + str(temp))
    if temp <= 20:
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    elif temp >= 81 and temp <= 90:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif temp >= 91 and temp <= 100:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif temp >= 41 and temp <= 50:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    elif temp >= 51 and temp <= 60:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    elif temp >= 61 and temp <= 70:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif temp >= 71 and temp <= 80:
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    basic.pause(100)
    strip.show()

def on_button_pressed_b():
    WTF()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_data_received():
    basic.show_string(serial.read_until(serial.delimiters(Delimiters.NEW_LINE)))
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

count = 0
temp = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("ZorraNet", "ZorranRokz.!")

def on_forever():
    global count
    count += 1
    if count < 2:
        WTF()
    basic.pause(5000)
basic.forever(on_forever)

def on_forever2():
    basic.pause(5000)
    WTF()
    dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
    strip.show()
basic.forever(on_forever2)
