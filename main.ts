input.onButtonPressed(Button.A, function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
    if (ESP8266_IoT.wifiState(true)) {
        ESP8266_IoT.connectWifi("Fakr", "asd")
    } else {
        ESP8266_IoT.connectWifi("ZorraNet", "ZorranRokz.!")
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (pins.analogReadPin(AnalogPin.P1)))
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
    strip.show()
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString(serial.readUntil(serial.delimiters(Delimiters.NewLine)))
})
let temp = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("ZorraNet", "ZorranRokz.!")
RTC_DS1307.DateTime(
2022,
2,
22,
16,
15,
30
)
basic.forever(function () {
    if (temp <= 20) {
        strip.showColor(neopixel.colors(NeoPixelColors.Indigo))
        basic.pause(5000)
    } else if (temp >= 21 && temp <= 30) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        basic.pause(5000)
    } else if (temp >= 31 && temp <= 40) {
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
        basic.pause(5000)
    } else if (temp >= 41 && temp <= 50) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        basic.pause(5000)
    } else if (temp >= 51 && temp <= 60) {
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        basic.pause(5000)
    } else {
        strip.showColor(neopixel.colors(NeoPixelColors.Purple))
        basic.pause(5000)
    }
    basic.pause(5000)
})
basic.forever(function () {
    temp = (pins.analogReadPin(AnalogPin.P1) - 273.15) * 1.4 + 32
    basic.pause(5000)
})
