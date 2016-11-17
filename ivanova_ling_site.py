from flask import Flask
from flask import url_for, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    urls = {'Анкета для пополнения словаря прилагательных': url_for('form')}

    return render_template('index.html', urls=urls)


@app.route('/form')
def form():

    arr = []
    f = open('list_of_adj.txt', 'r', encoding='utf-8')
    for line in f:
        line = line.strip()
        arr.append(line)
    f.close()
    wordsToTranslate = {}
    i = 0
    for word in arr:
        name = 'name' + str(i)
        wordsToTranslate[word] = name
        i += 1
    return render_template('copy2.html', wordsToTranslate=wordsToTranslate)

if __name__ == '__main__':
    
    app.run()
    
