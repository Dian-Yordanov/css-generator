from __future__ import print_function
import os
import webbrowser
import os.path
import json
from flask import Flask, request
from flask import render_template
from flask import Flask, send_from_directory

app = Flask(__name__)
filenames = []

@app.route('/api/foo/', methods=['GET'])
def foo():

    bar = request.args.to_dict()
    deciceWhichFunctionToRun(bar)
    return 'success', 200

@app.route('/webpageexample/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route('/')
def controol(name=None):
    return render_template('webcontrol.html', name=name)


# set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


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

    bar = str(bar).replace("\'", "\"")
    data = json.loads(bar)

    print(data['a'])

    if (data['a'] == 'Blackon'):

        booleanSetter(BlackCss,'BlackCss', True)
        booleanSetter(WhiteCss,'WhiteCss', False)
        booleanSetter(CustomCSS, 'customCSS', False)

    if (data['a'] == 'Blackoff'):

        booleanSetter(BlackCss, 'BlackCss', False)

    if (data['a'] == 'Whiteon'):

        booleanSetter(WhiteCss, 'WhiteCss', True)
        booleanSetter(BlackCss, 'BlackCss', False)
        booleanSetter(CustomCSS, 'customCSS', False)

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

        # oppositeColourB = 'colourBusedForReplacing'

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

    with open("pythonStaticBooleans/WhiteCss", "r") as f:
        WhiteCss = f.read()

        if (WhiteCss == "True"):
            filenames.append("BracketsHtmlAndCss/dataWhite.css")

        if ("BracketsHtmlAndCss/dataWhite.css" in filenames):
            if (WhiteCss == "False"):
                filenames.remove("BracketsHtmlAndCss/dataWhite.css")

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


    print(BlackCss, WhiteCss, PointerCss, specificCss, CustomCSS)
    print(filenames)

    with open('/media/dianlinux/LinuxExt4/pythonglobalcssgeneratorforstylish/static/data.css', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def resetCss():

    BlackCss = False

    if (os.path.exists('pythonStaticBooleans/BlackCss')):
        os.remove('pythonStaticBooleans/BlackCss')
    with open('pythonStaticBooleans/BlackCss', 'a') as the_file:
        the_file.write(str(BlackCss))

    WhiteCss = False

    if (os.path.exists('pythonStaticBooleans/WhiteCss')):
        os.remove('pythonStaticBooleans/WhiteCss')
    with open('pythonStaticBooleans/WhiteCss', 'a') as the_file:
        the_file.write(str(WhiteCss))

    PointerCss = False

    if (os.path.exists('pythonStaticBooleans/PointerCss')):
        os.remove('pythonStaticBooleans/PointerCss')
    with open('pythonStaticBooleans/PointerCss', 'a') as the_file:
        the_file.write(str(PointerCss))

    specificCss = False

    if (os.path.exists('pythonStaticBooleans/specificCss')):
        os.remove('pythonStaticBooleans/specificCss')
    with open('pythonStaticBooleans/specificCss', 'a') as the_file:
        the_file.write(str(specificCss))


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


