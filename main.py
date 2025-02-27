def on_gesture_shake():
    basic.clear_screen()
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_icon(IconNames.HEART)

def on_forever():
    led.plot_bar_graph(input.light_level(), 255)
    if input.light_level() > 150:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)
