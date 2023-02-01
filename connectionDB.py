import pymongo
import self as self
from pymongo import MongoClient
from Listfile import CommonList
# from s1 import Ui_Form

# if __name__ == "__main__":




    # collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})
#
def addItem():
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    print("Connection Successful")
    db = client['modifiedDB']
    collections = db['newData']




    for item in CommonList.reqData:
            print(item)
            for it in item:
                collections.insert_one({'name': item["name"], 'code': item["code"]})

addItem()




    # collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})

    # dictionary = {'name': 'ankita', 'age': '21', 'company': 'cars24'}
    # collections.insert_one(dictionary)
    # for item in CommonList.reqData:
    #     print(item)
    #     for it in item:
    #         collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})

            # insertThese = [
            #     {'name': item["self.name.text()"]}, {'code': item["self.passcode.text()"]}]

    # collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})
