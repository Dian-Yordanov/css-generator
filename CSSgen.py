from __future__ import print_function
import json
# import simplejson as json
from collections import namedtuple
from pprint import pprint

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def main():

    # with open('credentials', 'r') as myfile:
    #     data = myfile.read()
    #
    # StringTranslator = []
    # StringTranslator = data.split('\n')
    #
    # user_agent = StringTranslator[0]
    # client_id = StringTranslator[1]
    # client_secret = StringTranslator[2]
    # username = StringTranslator[3]
    # password = StringTranslator[4]

    with open('stylish-05-09-2017.json') as data_file:
        data = data_file.read()
        # data1 = json.load(data_file)
    # pprint(data1)

        # Parse JSON into an object with attributes corresponding to dict keys.
    # x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    # x = json2obj(data)

    # print(data1)
    # print(data)

    # str1 = str(data)
    #
    # print(len(str1))
    # # str1 = str(dict1)
    # #
    # # str1 = ''.join(data)
    # str1 = str1[1:len(str1)-1]

    # # print(len(str1))
    # #
    # print(str1)

    # print(data)

    # data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

    data = json2obj(data)

    print(data[0].name)

    # print(vars(data))

    # x = json.loads(data, object_hook=lambda d: Namespace(**d))
    # print(x)

        # json.loads
        # # jsonFile = json.dumps(data, separators=(',', ':'), sort_keys=True)
        # jsonFile = json.dumps(data)
    # pprint(data)
    # print jsonFile.dumps("\"code")

    # for 'code' in {data}:

    # for k in {jsonFile}:
    #     if("code" in k):
    #         print k





    # print jsonFile

    # print "fgfgf"
    # print "fgfgf"


if __name__ == '__main__':
    main()
