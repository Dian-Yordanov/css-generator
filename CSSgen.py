from __future__ import print_function
import json
from collections import namedtuple

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def main():

    x = -1
    y = 0
    with open('stylish-05-09-2017wintendo.json') as data_file:
        # data = data_file.read()
        data = json.load(data_file)
        # data['id'] = 134  # <--- add `id` value.
        for dataIndexer in data:
            x = x + 1

            if("Xelnect's dark style (inspired)(global)" in dataIndexer['name']):
                y=x

        print(data[y]['name'])


    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()
