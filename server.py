from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hj43kj5hlhhl5lh64l'
last_filename = ''


@app.route('/')
def text():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    sp = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(sp)


@app.route('/promotion_image')
def image():
    return render_template('promotion_image.html', filename='img/mars.png')


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def austr_selection():
    if request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('class'))
        for i in range(1, 9):
            print(request.form.get('work' + str(i)))
        print(request.form.get('sex'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        flash('Форма отправлена')
    return render_template('austr_selection.html')


@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name.lower() == 'меркурий':
        h2 = 'Это самая маленькая и самая близкая к Солнцу планета.'
        inf1 = 'Поверхность: пустынный пейзаж, состоящий из кратеров и трещин.'
        inf2 = 'Температура может достигать 427 °C, а ночью опускаться до -175 °C.'
        inf3 = 'Слабое магнитное поле.'
        inf4 = '1 меркурианский день: 176 земных дней'

    elif planet_name.lower() == 'венера':
        h2 = 'Является второй планетой от Солнца.'
        inf1 = 'Давление на поверхности в 92 раза превышает земное.'
        inf2 = 'Средняя температура на планете – 463 °C'
        inf3 = 'У планеты не прослеживается магнитное поле.'
        inf4 = 'Основным веществом в Венере является кремний.'

    elif planet_name.lower() == 'земля':
        h2 = 'Третья планета от Солнца.'
        inf1 = 'Поверхность планеты состоит из суши и Мирового океана.'
        inf2 = 'Единственным спутником Земли является Луна.'
        inf3 = 'Практически полностью отсутствуют кратеры.'
        inf4 = 'Является самой крупной среди планет, составляющих земную группу.'

    elif planet_name.lower() == 'марс':
        h2 = 'Четвёртая по удалённости от Солнца.'
        inf1 = 'Это планета земного типа, с твердой поверхностью.'
        inf2 = 'Наличие атмосферы.'
        inf3 = 'Средняя температура на планете – 27 °C'
        inf4 = 'На поверхности Марса вода присутствует в виде льда, но в атмосфере есть небольшое количество пара.'

    elif planet_name.lower() == 'юпитер':
        h2 = 'Пятая по удалённости от Солнца.'
        inf1 = 'Крупнейшая планета Солнечной системы. Является газовым гигантом.'
        inf2 = 'Из-за высокой силы притяжения ускорение свободного падения равно 24,8 м/с.'
        inf3 = 'На поверхности гиганта преобладает отрицательная температура, которая может достигать до -170 градусов.'
        inf4 = 'Юпитер имеет 79 спутников, что является самым большим показателем среди планет Солнечной системы.'

    elif planet_name.lower() == 'сатурн':
        h2 = 'Шестая по удалённости от Солнца.'
        inf1 = 'Это газовый гигант, состоящий преимущественно из водорода и гелия.'
        inf2 = 'Сатурн обладает самыми заметными кольцами среди всех планет Солнечной системы. Они состоят в основном из частиц льда,' \
               ' космического мусора и пыли.'
        inf3 = 'Вокруг планеты вращается 62 основных спутника.'
        inf4 = 'Сатурн излучает в пространство большое количество радиации.'

    elif planet_name.lower() == 'уран':
        h2 = 'Седьмая по удалённости от Солнца.'
        inf1 = 'Он самый легкий среди планет-гигантов, ведь основную его часть составляет лед.'
        inf2 = 'Сила притяжения меньше земной всего на 10 %.'
        inf3 = 'У планеты Уран существует 27 естественных спутников.'
        inf4 = 'Уран - самая холодная планета Солнечной системы. На поверхности температура воздуха может составлять -224 °C.'

    elif planet_name.lower() == 'нептун':
        h2 = 'Восьмая и самая дальняя от Солнца планета Солнечной системы.'
        inf1 = 'Нептун имеет синий окрас. Это из-за большого количества метана, содержащегося в атмосфере.'
        inf2 = 'По планете гуляют ураганы, скорость которых достигает 2400 км/ч.'
        inf3 = 'Несмотря на то, что Нептун находится далеко от Солнца, планета является очень горячей. ' \
               'Ее поверхность раскаляется до нескольких тысяч градусов Цельсия,' \
               ' и ученые до сих пор не могут объяснить, откуда берется такое количество тепла.'
        inf4 = 'На данный момент известно 14 спутников Нептуна.'
    else:
        return 'Проверьте правильность написания названия планеты'

    return render_template('choice.html', planet_name=planet_name.capitalize(), h2=h2, inf1=inf1, inf2=inf2, inf3=inf3,
                           inf4=inf4)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('rating.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_image', methods=['POST', 'GET'])
def load_im():
    global last_filename
    if request.method == 'POST':
        file = request.files['file']
        last_filename = '/users_img/' + file.filename
        file.save('static/users_img/' + file.filename)
    return render_template('load_im.html', filename=last_filename)

@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

