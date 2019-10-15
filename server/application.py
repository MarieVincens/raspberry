from flask import Flask, render_template

app = Flask(__name__)
from blueprints.led_blueprint import bp_led

app.register_blueprint(bp_led)

@app.route('/')
def index():
    return render_template('index.html')
