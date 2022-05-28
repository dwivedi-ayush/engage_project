from lib2to3.pgen2.pgen import generate_grammar
from recommendation import recommend
import pymongo
from pymongo import MongoClient
from sort import sort_with_index_preserved

import sys
def with_keys(d, keys):
    return {x: d[x] for x in d if x in keys}
def __main__():
    username=sys.argv[1]
    movie=sys.argv[2]
    # print("username",username)
    client=MongoClient("mongodb+srv://root:1234@cluster0.2eufj.mongodb.net/?retryWrites=true&w=majority")
    db=client["test"]
    movie=list(db.movies.find({ "title": movie }))
    person=list(db.users.find( { "username": username } ))
    movie_genre=movie[0]["genre_ids"]
    movie_cast=movie[0]["cast"]
    person_genre=person[0]["topGenre"]
    person_cast=person[0]["topCast"]
    
    genre_score=[]
    for genre in person_genre:
        genre_score.append(len(person_genre)-person_genre.index(genre))
    for genre in movie_genre:
        try:
            idx=person_genre.index(genre)
            genre_score[idx]=genre_score[idx]+3 
        except:
            genre_score.append(3) #keeping track of the recently watched movies
            person_genre.append(genre)
    genre_score,genre=sort_with_index_preserved(genre_score,person_genre)        
    # print("genre",person_genre)
    # print("genre_score",genre_score)

    db.users.update_one({"username":username},{"$set":{"topGenre":genre[:10]}})
    
    cast_score=[]
    for cast in person_cast:
        cast_score.append(len(person_cast)-person_cast.index(cast))
    for cast in movie_cast:
        try:
            idx=person_cast.index(cast)
            cast_score[idx]=cast_score[idx]+3 
        except:
            cast_score.append(3) #keeping track of the recently watched movies
            person_cast.append(cast)
    cast_score,cast=sort_with_index_preserved(cast_score,person_cast)        
    # print("cast",person_cast)
    # print("cast_score",cast_score)

    db.users.update_one({"username":username},{"$set":{"topCast":cast[:5]}})


    

if __name__ == "__main__":
    __main__()    