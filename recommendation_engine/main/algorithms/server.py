from recommendation import recommend
import json
import pymongo
from pymongo import MongoClient
# from bson.objectid import ObjectId
import sys

username=sys.argv[1]
# # person_id=ObjectId(sys.argv[1])

# person_id=ObjectId("628cdb807841396bd8be0c14")

client=MongoClient("mongodb+srv://root:1234@cluster0.2eufj.mongodb.net/?retryWrites=true&w=majority")
db=client["test"]
result=list(db.users.find())


all_people_top_10=[]
all_people_top_cast=[]
person_info_db=dict()

#finding the person that we want to target
for people in result:
    if(people["username"]==username):
        print("name: ",people["username"])
        person_info_db=people
        break

#collecting the data for collaborative(hybrid) filtering
for people in result:
    all_people_top_10.append(people["topGenre"])
    all_people_top_cast.append(people["topCast"])


all_people_dictionary_data=dict()

top_10_genre_list=person_info_db["topGenre"]

#current info can be simulated by changing the following dictionary
current_info = {"weather_currently": "rainy", "time_currently": "night", "day_currently": "saturday"}

#getting the movie details
result=list(db.movies.find())

movies=dict()
count=0
for movie in result:
    
    count+=1
    genre=movie["genre_ids"]
    language=movie["original_language"]
    year=movie['release_date']
    year=year[:4]
    cast=movie["cast"]
    length=movie["length"]
    temp=dict()
    temp["genre"]=genre
    temp["language"]=language
    temp["year"]=year
    temp["cast"]=cast
    temp["length"]=length
    movies[movie["title"]]=temp

for movie in movies:
    movies[movie]["extreme_tags"]=dict()                       

#to manually simulate a real world senerio with weather-movie preferences, etc
person_info={
    'average_year': '2002.3', 
    'average_watchtime': '128.6', 
    'exclusion_list': ['death', 'sex'], 
    'weather_dictionary': {'rainy': ['romantic'], 'sunny': ['superhero'], 'snowy': ['comedy']}, 
    'time_dictionary': {'morning': ['comedy'], 'afternoon': ['superhero'], 'evening': ['action'], 'night': ['romantic']},
    'day_dictionary': {'saturday': ['action'], 'sunday': ['romantic'], 'monday': ['comedy'], 'tuesday': ['superhero'], 'wednesday': ['horror'], 'thursday': ['fantasy'], 'friday': ['sci-fi']}}
person_info["genre_prefered"]=person_info_db["topGenre"]
person_info["cast_prefered"]=person_info_db["topCast"]
person_info["language_prefered"]=person_info_db["languages"]

#this functions simple returns the final result (imported from recommendation.py)
recommended_movies=recommend(all_people_top_10,all_people_top_cast,all_people_dictionary_data,movies,current_info,person_info)
print("\n\n\nFinal result: ",recommended_movies)

#updating the recommended movie list for the user (top 10 movies)
db.users.update_one({"username":username},{"$set":{"recommendedMovies":recommended_movies[:10]}})


