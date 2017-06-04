from __future__ import print_function
import os
import webbrowser
import os.path
import json

import flask
import shutil
from flask import Flask, request
from flask import render_template
from flask import Flask, send_from_directory
from flask import Flask, current_app
from flask import Flask
from flask import Response

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

from flask import Flask, send_file

from io import BytesIO

# from flask import Flask, session

# from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)
filenames = []

dirCss = '/media/dianlinux/LinuxExt4/pythonglobalcssgeneratorforstylish/BracketsHtmlAndCss/'

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = '/upload/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

# For a given file, return whether it's an allowed type or not



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/api/foo/', methods=['GET'])
def foo():

    bar = request.args.to_dict()
    deciceWhichFunctionToRun(bar)

    # resp = flask.Response("Foo bar baz")
    # # resp.headers['Access-Control-Allow-Origin'] = '*'
    # return resp

    # @app.route("/")
    # def home():
    resp = Response("")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

    # if __name__ == "__main__":
    #     app.run()

    # deciceWhichFunctionToRun(bar)
    #
    # # response.set_data(json.dumps(d))
    #
    # return 'success', 200

@app.route('/webpageexample/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route('/')
def controol(name=None):
    return render_template('webcontrol.html', name=name)

@app.route('/htmlPages')
def hello_world():
    return current_app.send_static_file('htmlPages.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/BracketsHtmlAndCss/dataDark.css')
def dfdsfdsfds():
    return current_app.send_static_file('dataDark.css')

# Route that will process the file upload
@app.route('/upload/', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/ddd')
def index():

    function1()
    function2()

def function1():
    return send_file(BytesIO('Hello from Dan Jacob and Stephane Wirtel !'.encode()),
                     attachment_filename="testing.txt",
                     as_attachment=True)
def function2():
    shutil.move("/home/dianlinux/Downloads/testing.txt", dirCss+"/testing.txt")



    # strIO = io.BytesIO
    # strIO.write('Hello from Dan Jacob and Stephane Wirtel !')
    # strIO.seek(0)
    # return send_file(strIO,
    #                  attachment_filename="testing.txt",
    #                  as_attachment=True)


#
# @app.route('/BracketsHtmlAndCss/<path:path>')
# def send_css(path):
#     return send_from_directory('css', path)


# if __name__ == "__main__":
#     app.run()

def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())

def booleanSetter(boolean, strboolean, value):

    boolean = value
    print('pythonStaticBooleans/'+ strboolean)

    if (os.path.exists('pythonStaticBooleans/'+ strboolean)):
        os.remove('pythonStaticBooleans/'+ strboolean)
    with open('pythonStaticBooleans/'+ strboolean, 'a') as the_file:
        the_file.write(str(boolean))

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

def hilo(a, b, c):
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c

def complement(r, g, b):
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))

def oppositeColoursEngine(x):
    x = 255 - x
    return x

def oppositeColours(r, g, b):
    r = oppositeColoursEngine(r)
    g = oppositeColoursEngine(g)
    b = oppositeColoursEngine(b)
    stringX = '(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
    return stringX

def deciceWhichFunctionToRun(bar):

    BlackCss = None
    WhiteCss = None
    PointerCss = None
    specificCss = None
    CustomCSS = None
    DarkMinimalisticScrollbar = None
    YouTubeCustomColors = None
    embededModifications = None
    facebookSpecificModifications = None
    redditSpecificModifications = None

    bar = str(bar).replace("\'", "\"")
    data = json.loads(bar)

    print(data['a'])

    if (data['a'] == 'Blackon'):

        booleanSetter(BlackCss,'BlackCss', True)
        booleanSetter(WhiteCss,'WhiteCss', False)
        booleanSetter(CustomCSS, 'CustomCSS', False)

    if (data['a'] == 'Blackoff'):

        booleanSetter(BlackCss, 'BlackCss', False)

    if (data['a'] == 'Whiteon'):

        booleanSetter(WhiteCss, 'WhiteCss', True)
        booleanSetter(BlackCss, 'BlackCss', False)
        booleanSetter(CustomCSS, 'CustomCSS', False)

    if (data['a'] == 'Whiteoff'):

        booleanSetter(WhiteCss, 'WhiteCss', False)

    if (data['a'] == 'Pointeron'):

        booleanSetter(PointerCss, 'PointerCss', True)

    if (data['a'] == 'Pointeroff'):

        booleanSetter(PointerCss, 'PointerCss', False)

    if (data['a'] == 'specificon'):

        booleanSetter(specificCss, 'specificCss', True)

    if (data['a'] == 'specificoff'):

        booleanSetter(specificCss, 'specificCss', False)

    if (data['a'] == 'getCssFromJson'):
        getCssFromJson()
    if (data['a'] == 'generateCss'):
        generateCss()
    if (data['a'] == 'resetCss'):
        resetCss()

    if ('colour' in data['a']):
        colourExtractor = '#' + str(data['a']).replace("colour", "")
        rgbColour = hex_to_rgb(colourExtractor)
        rgbaColour = 'rgba' + str(rgbColour)[:-1] + ',1)'

        complementColour = 'rgba' + str(complement(rgbColour[0], rgbColour[1], rgbColour[2]))[:-1] + ',1)'
        oppositeColour = 'rgba' + str(oppositeColours(rgbColour[0], rgbColour[1], rgbColour[2]))[:-1] + ',1)'

        complementColour = complementColour.replace(" ", "")
        oppositeColour = oppositeColour.replace(" ", "")
        rgbaColour = rgbaColour.replace(" ", "")

        with open("BracketsHtmlAndCss/templateCSS.css") as f:
            lines = f.readlines()
            lines = [l for l in lines if "ROW" in l]
            with open("BracketsHtmlAndCss/dataCustom.css", "w") as f1:
                f1.writelines(lines)

        with open("BracketsHtmlAndCss/templateCSS.css", "rt") as fin:
            with open("BracketsHtmlAndCss/dataCustom.css", "wt") as fout:

                for line in fin:
                    if('Colour1ForReplacing' in line):
                        fout.write(line.replace('Colour1ForReplacing', str(rgbaColour)))

                    elif('Colour2ForReplacing' in line):
                        fout.write(line.replace('Colour2ForReplacing', str(oppositeColour)))
                    else:
                        fout.write(line)

        print(complementColour)
        print(oppositeColour)
        print(rgbaColour)

        booleanSetter(CustomCSS, 'CustomCSS', True)
        booleanSetter(BlackCss, 'BlackCss', False)
        booleanSetter(WhiteCss, 'WhiteCss', False)

    if (data['a'] == 'DarkMinimalisticScrollbaron'):

        booleanSetter(DarkMinimalisticScrollbar, 'DarkMinimalisticScrollbar', True)

    if (data['a'] == 'DarkMinimalisticScrollbaroff'):

        booleanSetter(DarkMinimalisticScrollbar, 'DarkMinimalisticScrollbar', False)

    if (data['a'] == 'YouTubeCustomColorson'):

        booleanSetter(YouTubeCustomColors, 'YouTubeCustomColors', True)

    if (data['a'] == 'YouTubeCustomColorsoff'):

        booleanSetter(YouTubeCustomColors, 'YouTubeCustomColors', False)

    if (data['a'] == 'embededModificationson'):

        booleanSetter(embededModifications, 'embededModifications', True)

    if (data['a'] == 'embededModificationsoff'):

        booleanSetter(embededModifications, 'embededModifications', False)

    if (data['a'] == 'facebookSpecificModificationson'):

        booleanSetter(facebookSpecificModifications, 'facebookSpecificModifications', True)

    if (data['a'] == 'facebookSpecificModificationsoff'):

        booleanSetter(facebookSpecificModifications, 'facebookSpecificModifications', False)

    if (data['a'] == 'redditSpecificModificationson'):

        booleanSetter(redditSpecificModifications, 'redditSpecificModifications', True)

    if (data['a'] == 'redditSpecificModificationsoff'):

        booleanSetter(redditSpecificModifications, 'redditSpecificModifications', False)


def getCssFromJson():
    os.system('python CSSgen.py')

def generateCss():
    print('generateCss')

    filenames.clear()
    if (os.path.exists('static/data.css')):
        os.remove('static/data.css')

    with open("pythonStaticBooleans/BlackCss", "r") as f:
        BlackCss = f.read()

        if (BlackCss == "True"):
            filenames.append("BracketsHtmlAndCss/dataDark.css")

        if ("BracketsHtmlAndCss/dataDark.css" in filenames):
            if (BlackCss == "False"):
                filenames.remove("BracketsHtmlAndCss/dataDark.css")

        if ("BracketsHtmlAndCss/dataCustom.css" in filenames):
                filenames.remove("BracketsHtmlAndCss/dataCustom.css")

    with open("pythonStaticBooleans/WhiteCss", "r") as f:
        WhiteCss = f.read()

        if (WhiteCss == "True"):
            filenames.append("BracketsHtmlAndCss/dataWhite.css")

        if ("BracketsHtmlAndCss/dataWhite.css" in filenames):
            if (WhiteCss == "False"):
                filenames.remove("BracketsHtmlAndCss/dataWhite.css")

        if ("BracketsHtmlAndCss/dataCustom.css" in filenames):
                filenames.remove("BracketsHtmlAndCss/dataCustom.css")

    with open("pythonStaticBooleans/PointerCss", "r") as f:
        PointerCss = f.read()

        if (PointerCss == "True"):
            filenames.append("BracketsHtmlAndCss/pointer.css")

        if ("BracketsHtmlAndCss/pointer.css" in filenames):
            if (PointerCss == "False"):
                filenames.remove("BracketsHtmlAndCss/pointer.css")

    with open("pythonStaticBooleans/specificCss", "r") as f:
        specificCss = f.read()

        if (specificCss == "True"):
            filenames.append("BracketsHtmlAndCss/webSiteSpecific.css")

        if ("BracketsHtmlAndCss/webSiteSpecific.css" in filenames):
            if (specificCss == "False"):
                filenames.remove("BracketsHtmlAndCss/webSiteSpecific.css")
                print("removed")

    with open("pythonStaticBooleans/CustomCSS", "r") as f:
        CustomCSS = f.read()

        if (CustomCSS == "True"):
            filenames.append("BracketsHtmlAndCss/dataCustom.css")

        if ("BracketsHtmlAndCss/dataCustom.css" in filenames):
            if (CustomCSS == "False"):
                filenames.remove("BracketsHtmlAndCss/dataCustom.css")

    with open("pythonStaticBooleans/DarkMinimalisticScrollbar", "r") as f:
        DarkMinimalisticScrollbar = f.read()

        if (DarkMinimalisticScrollbar == "True"):
            filenames.append("BracketsHtmlAndCss/DarkMinimalisticScrollbar.css")

        if ("BracketsHtmlAndCss/DarkMinimalisticScrollbar.css" in filenames):
            if (DarkMinimalisticScrollbar == "False"):
                filenames.remove("BracketsHtmlAndCss/DarkMinimalisticScrollbar.css")

    with open("pythonStaticBooleans/YouTubeCustomColors", "r") as f:
        YouTubeCustomColors = f.read()

        if (YouTubeCustomColors == "True"):
            filenames.append("BracketsHtmlAndCss/YouTubeCustomColors.css")

        if ("BracketsHtmlAndCss/YouTubeCustomColors.css" in filenames):
            if (YouTubeCustomColors == "False"):
                filenames.remove("BracketsHtmlAndCss/YouTubeCustomColors.css")

    with open("pythonStaticBooleans/embededModifications", "r") as f:
        embededModifications = f.read()

        if (embededModifications == "True"):
            filenames.append("BracketsHtmlAndCss/embededModifications.css")

        if ("BracketsHtmlAndCss/embededModifications.css" in filenames):
            if (embededModifications == "False"):
                filenames.remove("BracketsHtmlAndCss/embededModifications.css")

    with open("pythonStaticBooleans/facebookSpecificModifications", "r") as f:
        facebookSpecificModifications = f.read()

        if (facebookSpecificModifications == "True"):
            filenames.append("BracketsHtmlAndCss/facebookSpecificModifications.css")

        if ("BracketsHtmlAndCss/facebookSpecificModifications.css" in filenames):
            if (facebookSpecificModifications == "False"):
                filenames.remove("BracketsHtmlAndCss/facebookSpecificModifications.css")

    with open("pythonStaticBooleans/redditSpecificModifications", "r") as f:
        redditSpecificModifications = f.read()

        if (redditSpecificModifications == "True"):
            filenames.append("BracketsHtmlAndCss/redditSpecificModifications.css")

        if ("BracketsHtmlAndCss/redditSpecificModifications.css" in filenames):
            if (redditSpecificModifications == "False"):
                filenames.remove("BracketsHtmlAndCss/redditSpecificModifications.css")

    print(BlackCss, WhiteCss, PointerCss, specificCss, CustomCSS, DarkMinimalisticScrollbar, YouTubeCustomColors,
          embededModifications, facebookSpecificModifications, redditSpecificModifications)
    print(filenames)

    with open('/media/dianlinux/LinuxExt4/pythonglobalcssgeneratorforstylish/static/data.css', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def resetElement(boolean, booleanName):
    if (os.path.exists('pythonStaticBooleans/' + booleanName)):
        os.remove('pythonStaticBooleans/' + booleanName)
    with open('pythonStaticBooleans/' + booleanName, 'a') as the_file:
        the_file.write(str(boolean))

def resetCss():

    BlackCss = False
    resetElement(BlackCss, 'BlackCss')

    WhiteCss = False
    resetElement(WhiteCss, 'WhiteCss')

    PointerCss = False
    resetElement(PointerCss, 'PointerCss')

    specificCss = False
    resetElement(specificCss, 'specificCss')

    CustomCSS = False
    resetElement(CustomCSS, 'CustomCSS')

    DarkMinimalisticScrollbar = False
    resetElement(DarkMinimalisticScrollbar, 'DarkMinimalisticScrollbar')

    YouTubeCustomColors = False
    resetElement(YouTubeCustomColors, 'YouTubeCustomColors')

    embededModifications = False
    resetElement(embededModifications, 'embededModifications')

    facebookSpecificModifications = False
    resetElement(facebookSpecificModifications, 'facebookSpecificModifications')

    redditSpecificModifications = False
    resetElement(redditSpecificModifications, 'redditSpecificModifications')

    filenames.clear()
    if (os.path.exists('static/data.css')):
        os.remove('static/data.css')

if __name__ == "__main__":

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.static_folder = 'static'

    url = 'http://127.0.0.1:5000/'
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    os.system('WID=`xdotool search "Google Chrome" | head -1`; xdotool windowactivate --sync $WID')

    app.run()


