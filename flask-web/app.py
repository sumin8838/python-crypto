from flask import Flask, render_template, request

app = Flask(__name__)

# Home 페이지
@app.route('/')
def home():
    return render_template('home.html', title='Home')

# 구구단 페이지
@app.route('/multiplication', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            gugu_list = [f"{number} x {i} = {number * i}" for i in range(1, 10)]
            return render_template('multiplication.html', title='구구단', gugu_list=gugu_list, number=number)
        except ValueError:
            return render_template('multiplication.html', title='구구단', error="숫자를 입력해주세요.")
    return render_template('multiplication.html', title='구구단')

# 계산기 페이지
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operator = request.form['operator']

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "0으로 나눌 수 없습니다."
        except ValueError:
            result = "유효한 숫자를 입력해주세요."
    
    return render_template('calculator.html', title='계산기', result=result)
