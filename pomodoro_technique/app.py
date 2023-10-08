from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pomodoro():
    return render_template('pomodoro.html')


if __name__ == '__main__':
    app.run(debug=True)
