from recommendation import recommend
import json
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}
def __main__():
    username=sys.argv[1]
    client=MongoClient("mongodb+srv://root:1234@cluster0.2eufj.mongodb.net/?retryWrites=true&w=majority")
    db=client["test"]
    result=list(db.users.find( { "username": username } ))
    result=[without_keys(result[0],["_id","isAdmin","updatedAt","createdAt","__v"])]
    print(result)
    return result

if __name__ == "__main__":
    __main__()    