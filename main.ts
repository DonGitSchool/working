input.onButtonPressed(Button.A, function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
    if (ESP8266_IoT.wifiState(true)) {
        ESP8266_IoT.connectWifi("Fakr", "asd")
    } else {
        ESP8266_IoT.connectWifi("ZorraNet", "ZorranRokz.!")
    }
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString(serial.readUntil(serial.delimiters(Delimiters.NewLine)))
})
OLED.init(64, 128)
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
    ESP8266_IoT.connectThingSpeak()
    ESP8266_IoT.setData(
    "V348E7R21KYZS9CJ",
    357,
    1,
    0
    )
    ESP8266_IoT.uploadData()
    basic.pause(50000)
})
