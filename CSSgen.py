from __future__ import print_function
import json
from collections import namedtuple
import io
import os
import jsonpickle

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

# def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
# def obj2json(data): return json.loads(data, object_hook=_json_object_hook)

def main():



    # filename = 'data.json'

    # Use jsonpickle to transform the object into a JSON string:
    #
    # import jsonpickle
    # frozen = jsonpickle.encode(obj)
    # Use jsonpickle to recreate a Python object from a JSON string:
    #
    # thawed = jsonpickle.decode(frozen)

    with open('stylish-05-09-2017.json') as data_file:
        # data = data_file.read()
        data = json.load(data_file)
        # data['id'] = 134  # <--- add `id` value.
        data[1]['name'] = "fsdsdfsd"
        print(data[1]['name'])


    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    # with open(filename, 'r') as f:
    #     data = json.load(f)
    #     data['id'] = 134  # <--- add `id` value.

    # os.remove(filename)
    # with open(filename, 'w') as f:
    #     json.dump(data, f, indent=4)


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



    # with open('stylish-05-09-2017.json') as json_data:
    #     data = json.load(json_data)

    # frozen = jsonpickle.encode(data)
    # thawed = jsonpickle.decode(frozen)

    # thawed = jsonpickle.decode(data)
    # print(thawed)
    # print(thawed[1])

    # frozen = jsonpickle.encode(thawed)

    # data = json2obj(data)
    # print(data[1].sections[0].code)

    # frozen = jsonpickle.encode(data)


    # jsonConverted  = json.dumps(data, default=lambda o: o.__dict__)
    # jsonConverted = json.dumps(data.__dict__)
    # print(data[0])

# Use jsonpickle to transform the object into a JSON string:
#
# import jsonpickle
# frozen = jsonpickle.encode(obj)
# Use jsonpickle to recreate a Python object from a JSON string:
#
# thawed = jsonpickle.decode(frozen)



    # with io.open('data.txt', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(jsonConverted, ensure_ascii=False))

    # print(data[1].sections[0].code)

    # data[1].sections[0].code = ""
    # print(data[1].sections[0].code)

    # with open('data.txt', 'w') as outfile:
    #     json.dump(frozen, outfile)

if __name__ == '__main__':
    main()
