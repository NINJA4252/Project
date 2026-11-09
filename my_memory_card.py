from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton,QHBoxLayout
from random import shuffle, randint

class Question():
    def __init__(self, question, right, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right = right
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Самый практичный танк Великой Отечественной Войны', 'Т-34', 'Ис-2', 'Су-100П', 'Асу-85'))
questions_list.append(Question('В каком году был создан Майнкрафт', '2009', '2012', '2010', '2018'))
questions_list.append(Question('В каком году был создан Роблокс', '2009', '2012', '2020', '2011'))
questions_list.append(Question('Столица Италии', 'Рим', 'Венеция', 'Сицилия', 'Вена'))
questions_list.append(Question('Год начала Второй Мировой Войны', '1939', '1941', '1945', '1937'))
def show_cor(res):
    t_1.setText(res)
    show_res()

def check_answer():
    if answers[0].isChecked():
        show_cor('Правильно')
        main_wind.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_cor('Неправильно')

def next_question():
    main_wind.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    as_kk(q)

    
def show_res():
    RadioGB.hide()
    RadioGB_2.show()
    but.setText('Следующий вопрос')
    print(f'Статистика:\n Всего вопросов: {main_wind.total}\n Правильных ответов: {main_wind.score}')
    
def show_ques():
    RadioGB_2.hide()
    RadioGB.show()
    but.setText('Ответить')
    #группа кнопок в переменной RadioGroup
    RadioGroup.setExclusive(False)
    rbt_1.setChecked(False)
    rbt_2.setChecked(False) 
    rbt_3.setChecked(False) 
    rbt_4.setChecked(False)
    RadioGroup.setExclusive(True)

def str_test():
    if but.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def as_kk(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    lab.setText(q.question)
    t_2.setText(q.right)
    show_ques()


app = QApplication([])
main_wind = QWidget()
main_wind.setWindowTitle('Memory Card')
main_wind.resize(500, 400)  # выставила размер окна /ширина,высота/

############################

RadioGB = QGroupBox('Варианты ответов')
lab = QLabel('Какой национальности не существует?')
but = QPushButton('Ответить')
rbt_1 = QRadioButton('Энцы')
rbt_2 = QRadioButton('Смурфы')
rbt_3 = QRadioButton('Чулымцы')
rbt_4 = QRadioButton('Алеуты')
####
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbt_1)
RadioGroup.addButton(rbt_2)
RadioGroup.addButton(rbt_3)
RadioGroup.addButton(rbt_4)
####
answers = [rbt_1, rbt_2, rbt_3, rbt_4]
line_h1 = QHBoxLayout()
line_v2 = QVBoxLayout()
line_v3 = QVBoxLayout()

line_v2.addWidget(rbt_1, alignment = Qt.AlignCenter)
line_v2.addWidget(rbt_2, alignment = Qt.AlignCenter)
line_v3.addWidget(rbt_3, alignment = Qt.AlignCenter)
line_v3.addWidget(rbt_4, alignment = Qt.AlignCenter)

line_h1.addLayout(line_v2)
line_h1.addLayout(line_v3)

RadioGB.setLayout(line_h1)


######################

RadioGB_2 = QGroupBox('Результат теста')
#labe = QLabel('Самый сложный вопрос в мире!')
#but_1 = QPushButton('Следующий вопрос')
t_1 = QLabel('Правильно/Неправильно')
t_2 = QLabel('Правильный ответ')

line_v1 = QVBoxLayout()
main_line = QVBoxLayout()

line_v1.addWidget(t_1, alignment = Qt.AlignLeft)
line_v1.addWidget(t_2, alignment = Qt.AlignCenter)

RadioGB_2.setLayout(line_v1)
RadioGB_2.hide()
main_line.addWidget(lab, alignment = Qt.AlignCenter)
main_line.addStretch(1)
main_line.addWidget(RadioGB) #, alignment = Qt.AlignCenter
main_line.addStretch(1)
main_line.addWidget(RadioGB_2) #, alignment = Qt.AlignCenter
main_line.addStretch(1)
main_line.addWidget(but, alignment = Qt.AlignCenter) 
main_wind.setLayout(main_line)
main_line.addStretch(1)

main_wind.setLayout(main_line)
but.clicked.connect(str_test)
main_wind.score = 0
main_wind.total = 0

main_wind.show()
app.exec_()


#создай приложение для запоминания информации