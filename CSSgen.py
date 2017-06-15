from __future__ import print_function
import json
import os


# from collections import namedtuple

# try:
#     from types import SimpleNamespace as Namespace
# except ImportError:
#     # Python 2.x fallback
#     from argparse import Namespace

from __init__ import format_css

# def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
# def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def unicodefy(String):
    return unicode(String).encode('utf-8')

def returnCSSFromFileAndName(File,Name):
    x = -1
    x1 = -1
    y = 0
    with open(File) as data_file:
        data = json.load(data_file)
        for dataIndexer in data:
            x = x + 1
            if (Name in dataIndexer['name']):
                y = x
        for dataIndexer2 in data[y]['sections']:
            x1 = x1 + 1
            break
        css = data[y]['sections'][x1]['code']
    return css

def createJsonFileFromCssAndNameAndCssValue(File,Name,CssValue):

    x = -1
    x1 = -1
    y = 0
    with open(File) as data_file:
        data = json.load(data_file)
        for dataIndexer in data:
            x = x + 1
            if (Name in dataIndexer['name']):
                y = x
        for dataIndexer2 in data[y]['sections']:
            x1 = x1 + 1
            break
        data[y]['sections'][x1]['code'] = CssValue
        jsonTobeReturned = data
    return jsonTobeReturned

def main():

    print("hello")

    data = returnCSSFromFileAndName("stylish-05-09-2017.json", "Xelnect's dark style (inspired)(global)")

    # css = "/* make input elements more awesome */ input:hover{background-color: red;}"
    # css = format_css(unicodefy(data))

    os.remove('static/data.css')
    with open('static/data.css', 'a') as the_file:
        the_file.write(unicodefy(data))

    jsonThatIsReturned = createJsonFileFromCssAndNameAndCssValue("stylish-05-09-2017.json", "Xelnect's dark style (inspired)(global)",data)

    # print(jsonThatIsReturned)

    # css = "/* make input elements more awesome */ input:hover{background-color: red;}"
    # css = format_css(css)

    with open('data.json', 'w') as f:
        json.dump(jsonThatIsReturned, f, indent=4)




    # os.system('WID=`xdotool search "Mozilla Firefox" | head -1`xdotool windowactivate --sync $WID')


if __name__ == "__main__":
    main()
