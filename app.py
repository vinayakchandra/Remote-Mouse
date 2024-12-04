from flask import Flask, render_template
from pynput.mouse import Controller, Button

app = Flask(__name__)
mouse = Controller()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/left_click', methods=['GET'])
def left_click():
    # Perform a left click
    mouse.click(Button.left)
    return "Left click performed!"


@app.route('/right_click', methods=['GET'])
def right_click():
    # Perform a right click
    mouse.click(Button.right)
    return "Right click performed!"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # Enable debugging
