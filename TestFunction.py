import json
import urllib2

# def printIterationArray(array):
#     for item in array:
#         item.encode('utf-8')
#         print item

def main():

    target_url = 'https://pastebin.com/raw/dWzUx0rP'
    dataFromURL = urllib2.urlopen(target_url)

    data = json.load(dataFromURL)

    x = 0
    # dataIndexArray1 = []
    # dataIndexArray2 = []
    dataIndexArray3 = []
    for dataIndexer1 in data:
        # dataIndexArray1.append(dataIndexer1)
        dataIndexArray3.append("tagHeadUsedforSorting"+dataIndexer1)
        for dataIndexer2 in data[dataIndexer1]:
            # dataIndexArray2.append(dataIndexer2)
            dataIndexArray3.append("tagTailUsedforSorting"+dataIndexer1+dataIndexer2)
        x = x + 1

    # print x
    # printIterationArray(dataIndexArray1)
    # printIterationArray(dataIndexArray2)
    # print dataIndexArray1
    # print dataIndexArray2
    # print dataIndexArray3

    dataDif1 =[]
    dataDif2 = []
    finalArray = []
    for item in dataIndexArray3:
        if "tagHeadUsedforSorting" in item:
            headitem = item.replace('tagHeadUsedforSorting', '')
            print headitem
        if "tagTailUsedforSorting" in item:
            tailitem = item.replace('tagTailUsedforSorting', '').replace(headitem, '')
            # tailitem = item.replace(headitem, '')
            print tailitem
            finalArray.append(headitem + " " +tailitem)
    print finalArray

if __name__ == '__main__':
    main()
