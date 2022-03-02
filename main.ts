input.onButtonPressed(Button.A, function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
})
function WTF () {
    strip.setBrightness(20)
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P1,
    true,
    false,
    true
    )
    dht11_dht22.selectTempType(tempType.fahrenheit)
    basic.pause(1000)
    temp = dht11_dht22.readData(dataType.temperature)
    basic.showString("" + temp)
    if (temp <= 20) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
    } else if (temp > 80 && temp <= 90) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(6, neopixel.colors(NeoPixelColors.Red))
    } else if (temp > 90 && temp <= 100) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(7, neopixel.colors(NeoPixelColors.Red))
    } else if (temp > 40 && temp <= 50) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
    } else if (temp > 50 && temp <= 60) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Red))
    } else if (temp > 60 && temp <= 70) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Red))
    } else if (temp > 70 && temp <= 80) {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(5, neopixel.colors(NeoPixelColors.Red))
    } else {
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    }
    basic.pause(100)
    strip.show()
}
function joinnet () {
    ESP8266_IoT.connectWifi("ZorraNet", "ZorranRokz.!")
    basic.pause(1000)
}
input.onButtonPressed(Button.B, function () {
    WTF()
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString(serial.readUntil(serial.delimiters(Delimiters.NewLine)))
})
let temp = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("ZorraNet", "ZorranRokz.!")
strip.setBrightness(20)
loops.everyInterval(5000, function () {
    basic.showString("Hello!")
})
