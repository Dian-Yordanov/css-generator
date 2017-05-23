from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/hello/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route("/")
def hello1():
    return "Hello Wordsfsdfdsld!"

if __name__ == "__main__":
    app.static_folder = 'static'
    app.run()