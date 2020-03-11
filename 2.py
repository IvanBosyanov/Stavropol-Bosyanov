from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.',
                      'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.',
                      'И начнем с Марса!',
                      'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title></title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    lib = {'title': 'Марс',
           'surname': 'Watny',
           'name': 'Mark',
           'education': 'выше среднего',
           'profession': 'штурман марсохода',
           'sex': 'male',
           'motivation': 'Всегда мечтал застрять на Марсе!',
           'ready': True}
    return render_template('index.html', **lib)


if __name__ == '__main__':
    app.run(port=8080, host='127.1.0.1')
