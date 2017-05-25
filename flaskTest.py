from flask import Flask
import os
import webbrowser
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/api/foo/', methods=['GET'])
def foo():
    bar = request.args.to_dict()
    print bar
    return 'success', 200

@app.route('/hello/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route('/')
def controol(name=None):
    return render_template('webcontrol.html', name=name)


# @app.route("/")
# def hello1():
#     return "Hello Wordsfsdfdsld!"

if __name__ == "__main__":
    app.static_folder = 'static'

    url = 'http://127.0.0.1:5000/hello/'
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    os.system('WID=`xdotool search "Google Chrome" | head -1`; xdotool windowactivate --sync $WID')

    app.run()


