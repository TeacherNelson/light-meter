input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    led.plotBarGraph(
    input.lightLevel(),
    255
    )
    if (input.lightLevel() > 150) {
        basic.showIcon(IconNames.Yes)
    }
})
