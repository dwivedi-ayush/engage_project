from recommendation import recommend
import pymongo
from pymongo import MongoClient

import sys
def with_keys(d, keys):
    return {x: d[x] for x in d if x in keys}
def __main__():
    # username=sys.argv[1]
    client=MongoClient("mongodb+srv://root:1234@cluster0.2eufj.mongodb.net/?retryWrites=true&w=majority")
    db=client["test"]
    result=list(db.movies.find())
    new_result=[]
    for movie in result:
        new_result.append(with_keys(movie,["title","genre_ids"]))
    
    # result=[without_keys(result,[])]
    print(new_result)
    return new_result

if __name__ == "__main__":
    __main__()    