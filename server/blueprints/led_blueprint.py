from flask import Blueprint, redirect, render_template, url_for
from model.led import Led

bp_led = Blueprint('led', __name__, url_prefix='/led')

Led.initialisation()
redLed = Led(16)
blueLed = Led(14)


@bp_led.route('/on/<int:color>')
def led_on(color):

    if color == 1:
        redLed.on()
    elif color == 2:
        blueLed.on()

    return redirect(url_for('index'))


@bp_led.route('/off/<int:color>')
def led_off(color):
    if color == 1:
        redLed.off()
    elif color == 2:
        blueLed.off()
    
    return redirect(url_for('index'))
