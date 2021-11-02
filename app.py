from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
@app.route('/greet/<celsius>')
def greet(celsius=""):
    return "{}C = {}f".format(celsius, convert_celsius_to_fahrenheit(celsius))


def convert_celsius_to_fahrenheit(celsius):
    """convert temperature in celsius to fahrenheit"""
    fahrenheit = float(celsius) * 9 / 5 + 32
    return float(fahrenheit)


if __name__ == '__main__':
    app.run()
