from __future__ import print_function
import os
import random
import string
import webbrowser
import os.path
import json
import fileinput
from os import listdir



from flask import Flask, current_app
from flask import Response

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from os.path import isfile, join

from flask import Flask, send_file

from io import BytesIO

from flask import Flask





app = Flask(__name__)





filenames = []

fileNamesOfStartingFields = ['BlackCss', 'CustomCSS','DarkMinimalisticScrollbar','embededModifications',
                             'facebookSpecificModifications','PointerCss','redditSpecificModifications',
                             'specificCss','WhiteCss','YouTubeCustomColors']
dirCss = '/media/dianlinux/LinuxExt4/pythonglobalcssgeneratorforstylish/BracketsHtmlAndCss/'

@app.route('/api/foo/', methods=['GET'])
def foo():

    bar = request.args.to_dict()
    deciceWhichFunctionToRun(bar)
    resp = Response("")
    return resp

@app.route('/webpageexample/')
def hello(name=None):
    return render_template('guardianHtml.html', name=name)

@app.route('/')
def controol(name=None):
    return render_template('webcontrol.html', name=name)

@app.route('/htmlPages')
def hello_world():
    return current_app.send_static_file('htmlPages.html')

@app.route('/bootstrap/<path:path>')
def static_file(path):
    return send_from_directory('bootstrap', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/BracketsHtmlAndCss/<path:path>')
def dfdsfdsfds(path):
    return send_from_directory('BracketsHtmlAndCss', path)

@app.route('/static/<path:path>')
def dddd(path):
    return send_from_directory('static', path)

@app.route('/check_selected', methods=['GET','POST'])
def check_selected():
    jsdata = request.form['javascript_data']
    saveCSSLocally(jsdata)
    return 'yes'


@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    saveCSSLocally(jsdata)
    return jsdata

@app.route('/ddd')
def index():
    return send_file(BytesIO('Hello from Dan Jfsdfsdfsdacob and Stephane Wirtel !'.encode()),
                     attachment_filename="testing.txt",
                     as_attachment=True)

@app.route('/api2', methods=['GET','POST'])
def getNameFromPost():
    jsdata = request.form['javascript_data']
    print(jsdata)
    deciceWhichFunctionToRunPostedDataToAPI2(jsdata.split("|||SPLITTER|||")[0],jsdata.split("|||SPLITTER|||")[1])
    return 'yes'

@app.route('/hello')
def hello_world2(user=None):
    user = user or 'Shalabh'
    user1 = 'Shalaasasadasdasdasabh'
    return render_template('test.html', user=user,user1=user1)

def saveCSSLocally(jsdata):
    firstLine = jsdata.split('\n', 1)[0].replace("|||", "")
    print(firstLine)

    # print('ggggggggggggggggg')
    i = jsdata.index('\n')
    secondLine = jsdata[i+1:]

    print(secondLine)

    if (os.path.exists(firstLine)):
        os.remove(firstLine)
    with open(firstLine, 'a') as the_file:
        the_file.write(secondLine)

    # print(jsdata)

def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())

def booleanSetter(boolean, strboolean, value):

    boolean = value
    # print('pythonStaticBooleans/'+ strboolean)

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

    if(readDatafromJsonFile(data['a'].replace("on", "").replace("off", ""))['boolean']):
        deciceWhichFunctionToRunForRandomJsonData(data['a'], readDatafromJsonFile(data['a'].replace("on", "").replace("off", "")))

    else:
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

def deciceWhichFunctionToRunForRandomJsonData(dataa, jsonObject):

    jsonObject['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'] = None

    if (dataa == jsonObject['jsonObject']['SpanClassId']+'on'):

        booleanSetter(jsonObject['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'], dataa.replace("on", "").replace("off", ""), True)

    if (dataa == jsonObject['jsonObject']['SpanClassId']+'off'):

        booleanSetter(jsonObject['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'], dataa.replace("on", "").replace("off", ""), False)

def DoTheWithOpenForTheArrayOfCssCustomFiles():

    # I think it should be a cycle of all the booleans and it may be just better to redo the whole system
    # with open("pythonStaticBooleans/PointerCss", "r") as f:
    #     PointerCss = f.read()
    #
    #     if (PointerCss == "True"):
    #         filenames.append("BracketsHtmlAndCss/pointer.css")
    #
    #     if ("BracketsHtmlAndCss/pointer.css" in filenames):
    #         if (PointerCss == "False"):
    #             filenames.remove("BracketsHtmlAndCss/pointer.css")

    onlyfiles = [f for f in listdir('pythonStaticBooleans/') if isfile(join('pythonStaticBooleans/', f))]
    jsonObjectFetched = []
    list3 = [x for x in onlyfiles if x not in fileNamesOfStartingFields]

    # print(onlyfiles)
    # print(fileNamesOfStartingFields)
    # print(list3)

    for indexedBoolean in list3:

        jsonObjectFetched = readDatafromJsonFile(indexedBoolean)
        # print(jsonObjectFetched)
        # print(indexedBoolean)

        with open("pythonStaticBooleans/"+indexedBoolean, "r") as f:
            jsonObjectFetched['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'] = f.read()

            if (jsonObjectFetched['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'] == "True"):
                if not os.path.exists("BracketsHtmlAndCss/"+indexedBoolean+".css"):
                    os.mknod("BracketsHtmlAndCss/"+indexedBoolean+".css")
                filenames.append("BracketsHtmlAndCss/"+indexedBoolean+".css")

            if ("BracketsHtmlAndCss/"+indexedBoolean+".css" in filenames):
                if (jsonObjectFetched['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'] == "False"):
                    filenames.remove("BracketsHtmlAndCss/"+indexedBoolean+".css")

        print(jsonObjectFetched['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'])


            # onlyfiles = [f for f in listdir('pythonStaticBooleans/') if isfile(join('pythonStaticBooleans/', f))]

    # varToString = json.dumps(jsonObject['jsonObject']['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'])
    #
    # # print(jsonObject['index'])
    # # print(jsonObject['jsonObject'])
    #
    # print(varToString)
    # print(dataa)

    # return  'bb'

def deciceWhichFunctionToRunPostedDataToAPI2(typeOfData,nameOfField):

    if (typeOfData == 'AddNewCssFunction'):

        changeHtmlDynamically('AddNewCssFunction',nameOfField)

    if (typeOfData == 'RemoveNewCssFunction'):

        changeHtmlDynamically('RemoveNewCssFunction',nameOfField)

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

    DoTheWithOpenForTheArrayOfCssCustomFiles()

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

    onlyfiles = [f for f in listdir('pythonStaticBooleans/') if isfile(join('pythonStaticBooleans/', f))]
    jsonObjectFetched = []
    list3 = [x for x in onlyfiles if x not in fileNamesOfStartingFields]

    for indexedBoolean in list3:
        print(indexedBoolean)

        if (os.path.exists("BracketsHtmlAndCss/"+indexedBoolean+".css")):
            os.remove("BracketsHtmlAndCss/"+indexedBoolean+".css")
        if (os.path.exists('pythonStaticBooleans/'+indexedBoolean)):
            os.remove('pythonStaticBooleans/'+indexedBoolean)

def readDatafromJsonFile(SpanClassIdGiven):
    # print(SpanClassIdGiven)

    fileNameAndLocation = 'static/jsonDataForFields.json'

    # nameOfField = 34
    #
    # stringS= ''
    # with open(fileNameAndLocation) as f: stringS = f.read()
    # print(stringS)

    booleanToReturn = None
    indexInt = 0

    with open(fileNameAndLocation) as data_file:
        data = json.load(data_file)

    for dataIndexer in data:

        if(dataIndexer['SpanClassId']==SpanClassIdGiven):
            booleanToReturn = True
            break
        indexInt = indexInt + 1


    data1 = {}
    data1['boolean'] = booleanToReturn
    data1['index'] = indexInt
    try:
        data1['jsonObject'] = data[indexInt]
    except IndexError:
        data1['jsonObject'] = 'null'


    # print(data[indexInt]['ip_address'])
    # print(data[indexInt]['id'])
    # print(data1['boolean'])

    return data1

def id_generator(size=15, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def getAndSaveJsonDataToLocalFileInOrderToBuildCssFields(nameOfField):

    fileNameAndLocation = 'static/jsonDataForFields.json'

    # data = {}
    # data['SpanClassId'] = id_generator()
    # data['InputId'] = id_generator()
    # data['CallFunctionForThisButton'] = id_generator()
    # data['SpecificNameForThisFunction'] = id_generator()
    # data['nameOfCssConstructor'] = nameOfField
    #
    # # json_data = json.dumps(data)
    # json_data = json.dumps(data)

    feeds =[]
    if is_non_zero_file(fileNameAndLocation):
        with open(fileNameAndLocation, mode='r', encoding='utf-8') as feedsjson:
            feeds = json.load(feedsjson)
    else:
        pass
    with open(fileNameAndLocation, mode='w', encoding='utf-8') as feedsjson:
        entry = {'SpanClassId': id_generator(),
                 'InputId': id_generator(),
                 'CallFunctionForThisButton': id_generator(),
                 'CssFileNameForUseWithDeciceWhichFunctionToRunFunction': id_generator(),
                 'nameOfCssConstructor': nameOfField}


        feeds.append(entry)
        json.dump(feeds, feedsjson)

    # print(id_generator())
    # print(id_generator())
    # print(id_generator())

    # print(entry)

    return entry

def readFileAndReturnA1LineStringOfIT(nameOfFile,nameOfField):

    # takes nameOfField and returns a json object with SpanClassId='hhh',InputId='hbhbh', CallFunctionForThisButton ='buttonFunctionfff', SpecificNameForThisFunction='ddd')
    # readDatafromJsonFile(nameOfField)

    jsonObject = getAndSaveJsonDataToLocalFileInOrderToBuildCssFields(nameOfField)

    # print(jsonObject['SpanClassId'])
    # print(jsonObject['InputId'])
    # print(jsonObject['CallFunctionForThisButton'])
    # print(jsonObject['SpecificNameForThisFunction'])
    # print(jsonObject['nameOfCssConstructor'])

    print(jsonObject['SpanClassId'])


    myfile = render_template(nameOfFile,
                             nameOfCssConstructor=nameOfField,
                             SpanClassId=jsonObject['SpanClassId'],
                             InputId=jsonObject['InputId'],
                             CallFunctionForThisButton =jsonObject['CallFunctionForThisButton'],
                             CssFileNameForUseWithDeciceWhichFunctionToRunFunction=jsonObject['CssFileNameForUseWithDeciceWhichFunctionToRunFunction'])

    # print(myfile)

    # with open(nameOfFile, 'r') as myfile:
    data=myfile.replace('\n', '')
    return data


def changeHtmlDynamically(CssFunction, nameOfField):

    textToInput = readFileAndReturnA1LineStringOfIT('htmlFileTemplateForDivs.html', nameOfField)
    if (CssFunction == 'AddNewCssFunction'):
        with open('templates/webcontrol.html', 'r') as f, open("templates/newfile",'w') as f1:
           for line in f:
               if 'IBTL1' in line:
                  f1.write(textToInput+"\n")  # Move f1.write(line) above, to write above instead
               f1.write(line)
        os.remove('templates/webcontrol.html')  # For windows only
        os.rename("templates/newfile", 'templates/webcontrol.html')  # Rename the new file

    if (CssFunction == 'RemoveNewCssFunction'):
        # with open('templates/webcontrol.html', 'r') as f:
        f = open("templates/webcontrol.html","r+")
        done = 0
        d = f.readlines()
        f.seek(0)
        listToBeAppended = []
        for i in reversed(d):
            # print(i)

            if 'THISSTRINGMAKESTHISLINEDELETABLE' not in i:
                listToBeAppended.append(i)

            else:
                if done == 0:
                    done = 1
                    continue
                else:
                    # if textToInput not in i:
                    listToBeAppended.append(i)

        listToBeAppended = reversed(listToBeAppended)
        for ii in listToBeAppended:
            f.write(ii)


        f.truncate()
        f.close()

if __name__ == "__main__":

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.static_folder = 'static'

    url = 'http://127.0.0.1:5000/'
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    os.system('WID=`xdotool search "Google Chrome" | head -1`; xdotool windowactivate --sync $WID')

    app.run()


