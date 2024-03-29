from flask import Flask, render_template, request

app = Flask(__name__)

# заглушка для функции получения курса валют
def get_exchange_rate(currency_from, currency_to):
    # В этой заглушке предполагается, что курс валют будет равен 1 для демонстрационных целей
    return 1.0

# конвертации валют
def convert_currency(amount, rate):
    return amount * rate

# main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        currency_from = request.form['currency_from']
        currency_to = request.form['currency_to']
        amount = float(request.form['amount'])
        rate = get_exchange_rate(currency_from, currency_to)
        converted_amount = convert_currency(amount, rate)
        return render_template('result.html', amount=amount, currency_from=currency_from, converted_amount=converted_amount, currency_to=currency_to)
    return render_template('index.html')

# result
@app.route('/convert', methods=['POST'])
def convert():
    currency_from = request.form['currency_from']
    currency_to = request.form['currency_to']
    amount = float(request.form['amount'])
    rate = get_exchange_rate(currency_from, currency_to)
    converted_amount = convert_currency(amount, rate)
    return render_template('result.html', amount=amount, currency_from=currency_from, converted_amount=converted_amount, currency_to=currency_to)

if __name__ == '__main__':
    app.run(debug=True)
