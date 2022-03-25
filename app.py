from flask import Flask, render_template, redirect, request

app = Flask(__name__)


# @app.route('/<test>/') #записывает в эту переменную
# def main(test): #это же переменная принимается данной функцией
#     test = test.upper() #внутри функц она обрабатывается
#     return render_template('index.html', my_var=test) #и ее возрващает my_var

@app.route('/')
def main():
    f = open('goods.txt', 'r', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)


@app.route('/add/', methods=["POST"])
def add():
    good = request.form["good"]
    f = open('goods.txt', 'a+', encoding='utf-8')
    f.write(good + '\n')
    f.close()
    return '''
        <h1>Инвентарь пополнен</h1>
        <a href='/'>Домой</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)