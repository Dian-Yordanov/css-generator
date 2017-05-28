from __future__ import print_function
import os
import webbrowser
import json
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/api/foo/', methods=['GET'])
def foo():
    bar = request.args.to_dict()
    getCssFromJson(bar)
    return 'success', 200

@app.route('/webpageexample/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route('/')
def controol(name=None):
    return render_template('webcontrol.html', name=name)


def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())


# def unicodefy(String):
#     return unicode(String).encode('utf-8')


def getCssFromJson(bar):
    print(bar)

    bar = str(bar).replace("\'", "\"")
    print(bar)

    data = json.loads(bar)

    print(data['a'])
    # data = json.dumps(bar)
    # print(data)



    # for dataIndexer in bar['a']:
    #     # x = x + 1
    #     print(dataIndexer)



    # if(bar[1] is 'getCssFromJson'):
    #     print 'getCssFromJson'
    #     os.system('python CSSgen.py')
    #



# @app.route("/")
# def hello1():
#     return "Hello Wordsfsdfdsld!"

if __name__ == "__main__":

    # run("CSSgen.py")



    app.static_folder = 'static'

    url = 'http://127.0.0.1:5000/'
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    os.system('WID=`xdotool search "Google Chrome" | head -1`; xdotool windowactivate --sync $WID')

    app.run()


