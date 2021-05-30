from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():

    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<temp>')
def f(temp=""):
    return "<h1>{:.1f} degrees celsius is {:.1f} degrees fahrenheit </h1>".format(
        float(temp), float(calc_celsius_to_fahrenheit(temp)))


def calc_celsius_to_fahrenheit(temperature):
    return float(temperature) * (9 / 5) + 32


if __name__ == '__main__':
    app.run()
