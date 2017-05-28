from __future__ import print_function
import os
import webbrowser
import os.path
import json
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

# BlackCss = False
# WhiteCss = False
# PointerCss = False
# specificCss = False

# BlackCss
# WhiteCss
# PointerCss
# specificCss

@app.route('/api/foo/', methods=['GET'])
def foo():

    # global BlackCss
    # global WhiteCss
    # global PointerCss
    # global specificCss

    bar = request.args.to_dict()
    deciceWhichFunctionToRun(bar)
    return 'success', 200

@app.route('/webpageexample/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route('/')
def controol(name=None):
    return render_template('webcontrol.html', name=name)

# @app.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)

# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                      endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)

def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())


# def unicodefy(String):
#     return unicode(String).encode('utf-8')

def deciceWhichFunctionToRun(bar):

    # global BlackCss = False
    # global WhiteCss = False
    # global PointerCss = False
    # global specificCss = False

    # global BlackCss
    # global WhiteCss
    # global PointerCss
    # global specificCss

    BlackCss = None
    WhiteCss = None
    PointerCss = None
    specificCss = None

    bar = str(bar).replace("\'", "\"")
    data = json.loads(bar)

    print(data['a'])

    if (data['a'] == 'Blackon'):
        BlackCss = True

        # fn = input('pythonStaticBooleans/BlackCss')

        if (os.path.exists('pythonStaticBooleans/BlackCss')):
            os.remove('pythonStaticBooleans/BlackCss')
        with open('pythonStaticBooleans/BlackCss', 'a') as the_file:
            the_file.write(str(BlackCss))
    # ...
    # the_file.write('Hello\n')

    if (data['a'] == 'Blackoff'):
        BlackCss = False

        if (os.path.exists('pythonStaticBooleans/BlackCss')):
            os.remove('pythonStaticBooleans/BlackCss')
        with open('pythonStaticBooleans/BlackCss', 'a') as the_file:
            the_file.write(str(BlackCss))

    if (data['a'] == 'Whiteon'):
        WhiteCss = True

        if (os.path.exists('pythonStaticBooleans/WhiteCss')):
            os.remove('pythonStaticBooleans/WhiteCss')
        with open('pythonStaticBooleans/WhiteCss', 'a') as the_file:
            the_file.write(str(WhiteCss))

    if (data['a'] == 'Whiteoff'):
        WhiteCss = False

        if (os.path.exists('pythonStaticBooleans/WhiteCss')):
            os.remove('pythonStaticBooleans/WhiteCss')
        with open('pythonStaticBooleans/WhiteCss', 'a') as the_file:
            the_file.write(str(WhiteCss))

    if (data['a'] == 'Pointeron'):
        PointerCss = True

        if (os.path.exists('pythonStaticBooleans/PointerCss')):
            os.remove('pythonStaticBooleans/PointerCss')
        with open('pythonStaticBooleans/PointerCss', 'a') as the_file:
            the_file.write(str(PointerCss))

    if (data['a'] == 'Pointeroff'):
        PointerCss = False

        if (os.path.exists('pythonStaticBooleans/PointerCss')):
            os.remove('pythonStaticBooleans/PointerCss')
        with open('pythonStaticBooleans/PointerCss', 'a') as the_file:
            the_file.write(str(PointerCss))

    if (data['a'] == 'specificon'):
        specificCss = True

        if (os.path.exists('pythonStaticBooleans/specificCss')):
            os.remove('pythonStaticBooleans/specificCss')
        with open('pythonStaticBooleans/specificCss', 'a') as the_file:
            the_file.write(str(specificCss))

    if (data['a'] == 'specificoff'):
        specificCss = False

        if (os.path.exists('pythonStaticBooleans/specificCss')):
            os.remove('pythonStaticBooleans/specificCss')
        with open('pythonStaticBooleans/specificCss', 'a') as the_file:
            the_file.write(str(specificCss))


    if (data['a'] == 'getCssFromJson'):
        # print('data' + " " + data['a'])
        getCssFromJson()
    if (data['a'] == 'generateCss'):
        # print('data' + " " + data['a'])
        generateCss(BlackCss, WhiteCss, PointerCss, specificCss)
    if (data['a'] == 'resetCss'):
        # print('data' + " " + data['a'])
        resetCss()

    # print('data' + " " + data['a'])

def getCssFromJson():
    os.system('python CSSgen.py')

def generateCss(BlackCss, WhiteCss, PointerCss, specificCss):
    print('generateCss')

    if (os.path.exists('static/data.css')):
        os.remove('static/data.css')

    filenames = []

    with open('pythonStaticBooleans/BlackCss', 'r') as f:
        BlackCss = f.read()

    if (BlackCss == True):
        filenames.append('BracketsHtmlAndCss/dataDark.css')

    if('BracketsHtmlAndCss/dataDark.css' in filenames):
        if (BlackCss == False):
            filenames.remove('BracketsHtmlAndCss/dataDark.css')

    with open('pythonStaticBooleans/WhiteCss', 'r') as f:
        WhiteCss = f.read()

    if (WhiteCss == True):
        filenames.append('BracketsHtmlAndCss/dataWhite.css')

    if('BracketsHtmlAndCss/dataDark.css' in filenames):
        if (WhiteCss == False):
            filenames.remove('BracketsHtmlAndCss/dataWhite.css')

    with open('pythonStaticBooleans/PointerCss', 'r') as f:
        PointerCss = f.read()

    if (PointerCss == True):
        filenames.append('BracketsHtmlAndCss/pointer.css')

    if('BracketsHtmlAndCss/dataDark.css' in filenames):
        if (PointerCss == False):
            filenames.remove('BracketsHtmlAndCss/pointer.css')

    with open('pythonStaticBooleans/specificCss', 'r') as f:
        specificCss = f.read()

    if (specificCss == True):
        filenames.append('BracketsHtmlAndCss/webSiteSpecific.css')

    if('BracketsHtmlAndCss/dataDark.css' in filenames):
        if (specificCss == False):
            filenames.remove('BracketsHtmlAndCss/webSiteSpecific.css')

    # 'BracketsHtmlAndCss/dataDark.css', 'BracketsHtmlAndCss/webSiteSpecific.css'

    print(BlackCss, WhiteCss, PointerCss, specificCss)
    print(filenames)

    with open('/media/dianlinux/LinuxExt4/pythonglobalcssgeneratorforstylish/static/data.css', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def resetCss():
    print('resetCss')
    
    if (os.path.exists('static/data.css')):
        os.remove('static/data.css')

# @app.route("/")
# def hello1():
#     return "Hello Wordsfsdfdsld!"

if __name__ == "__main__":

    # run("CSSgen.py")


    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.static_folder = 'static'

    url = 'http://127.0.0.1:5000/'
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    os.system('WID=`xdotool search "Google Chrome" | head -1`; xdotool windowactivate --sync $WID')

    app.run()


