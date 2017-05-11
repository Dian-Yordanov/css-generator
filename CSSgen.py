# from __future__ import print_function
import json
# from collections import namedtuple

# try:
#     from types import SimpleNamespace as Namespace
# except ImportError:
#     # Python 2.x fallback
#     from argparse import Namespace
from __init__ import format_css

# def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
# def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def returnCSSFromFileAndName(File,Name):
    css = ""

    x = -1
    x1 = -1
    y = 0
    y1 = 0
    with open(File) as data_file:
        data = json.load(data_file)
        for dataIndexer in data:
            x = x + 1

            # for string in dataIndexer:
            #     print(string)

            # print(str(dataIndexer)+"\n")
            if (Name in dataIndexer['name']):
                y = x
                # z=""
                # for string in dataIndexer:
                #     # print(string + "=" + str(dataIndexer[string]))
                #     if 'sections' in string:
                #         for string2 in str(dataIndexer[string]):
                #             # print string2
                #             # print string2
                #             # if 'code' in string2:
                #             z=z+string2
                #                 # print string2
                #         #     # print(string2 + "=" + str(string))
                #         # print(z)
        # print data[y]['sections']['code']
        for dataIndexer2 in data[y]['sections']:
            x1 = x1 + 1
            # print dataIndexer2
            break
        print data[y]['sections'][x1]['code']
        css = data[y]['sections'][x1]['code']

    return css

def main():

    data = returnCSSFromFileAndName("stylish-05-09-2017.json", "Xelnect's dark style (inspired)(global)")

        # print dataIndexer2['code']
            # if ("Xelnect's dark style (inspired)(global)" in dataIndexer2['code']):
            #     y = x

        # print(data[y]['sections'])

                # print(data[y]['sections']['code'])
                # print(str(dataIndexer)+"\n")
                # if 'code' in dataIndexer:
                #     print(dataIndexer['code'])
                # elif 'name' in dataIndexer:
                #     print(dataIndexer['name'])

        # print(data[y]['code'])


    # css = "/* make input elements more awesome */ input:hover{background-color: red;}"
    # css = format_css(css)

    with open('data.css', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()
