from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/i')
def intro():
    return 'Divya Maganti is currently learning python to obtain a decent programming career after she graduate' \
           ' college.'


@app.route('/b')
def body():
    return 'Divya Maganti is currently in high school and is aiming to attend either Rutgers University - New' \
           'Brunswick, NYU, Stevens Institute of Technology or NJIT.'


@app.route('/success')
def ending():
    return ''


@app.route('/reverse')
def reverse():
    word = request.args.get('word')
    # slicing
    new_word = word[::-1]
    return new_word


if __name__ == '__main__':
    app.run()
