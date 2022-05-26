from fileinput import close
import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from sort import sort_with_index_preserved
from scipy import spatial
def genre_based_recommendation_algo_2(movies,top_10_genre,all_people_top_10):
    '''
        first we find similar person to our target person
        then we use a simple scoring method (more the genre match the better) to score each movie
        the we use those scoring to predict how would our target person would score the movies
        and we then sort them accordingly and return them

    '''
    score_matrix=[]
    count_id=0
    person_id=[]
    scores=[]
    for movie in movies:
        score=0
        movie_genres=movies[movie]["genre"]
        for genre in top_10_genre:
            if(genre in movie_genres):
                score+=1      
        scores.append(score)
    score_matrix.append(scores)
    person_id.append(count_id)
    # this is the target user rating all the movies
    count_id+=1
    for genre_list in all_people_top_10:
        
        scores=[]
        
        for movie in movies:
            movie_genres=movies[movie]["genre"]
            score=0
            for genre in genre_list:
                if(genre in movie_genres):
                    score+=1      
            scores.append(score)
        person_id.append(count_id-1)
        count_id+=1
        score_matrix.append(scores)
    # this is everyone rating all the movies
    # now we find similarity based on the ratings
    
    cosine_similarity=[]
    for i in range(len(score_matrix)):
        temp=spatial.distance.cosine(score_matrix[0],score_matrix[i])
        cosine_similarity.append(1-temp)
    cosine_similarity,person_id=sort_with_index_preserved(cosine_similarity,person_id)
    closest_all_top_10=[]
    # not 0 because 0 would be the target person itself
    for i in range(1,6):
        closest_all_top_10.append(all_people_top_10[person_id[i]])
    # found top 5 people
    
    score=0
    scores=[]
    movie_name=[]
    count=0
    person_id=[]
    unique_movies=[]
    for movie in movies:
        
        score=0
        movie_genres=movies[movie]["genre"]
        for genre in top_10_genre:
            if(genre in movie_genres):
                score+=1
        movie_name.append(movie)        
        scores.append(score)
        person_id.append(count)
        break

    ''' score one movie (as the target user) beacuse of the 
        technalicities of the liberary usage
        or else all the movies will be rated the same
        this way even if the absolute rating might be affected 
        the realtive rating remains the same
        hence after sorting it wont matter much
    '''


    # the following lines of code is the syntax for liberary usage
    for genre_list in closest_all_top_10:
        count+=1
        for movie in movies:
            if(movie not in unique_movies):
                unique_movies.append(movie)
            score=0
            movie_genres=movies[movie]["genre"]
            for genre in genre_list:
                if(genre in movie_genres):
                    score+=1
            movie_name.append(movie)        
            scores.append(score)
            person_id.append(count)

    ratings_dict = {
        "item": movie_name,
        "user": person_id,
        "rating": scores,
    }

    df = pd.DataFrame(ratings_dict)
    reader = Reader(rating_scale=(1, 10))


    data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)
    # To use item-based cosine similarity
    sim_options = {
        "name": "cosine",
        "user_based": False, 
    }

    algo = KNNWithMeans(sim_options=sim_options)
    trainingSet = data.build_full_trainset()
    algo.verbose=False

    a=algo.fit(trainingSet)
    prediction_score=[]

    for i in unique_movies:
        prediction_score.append(algo.predict(0, i).est)
        
    # after prediction we sort based on the rating predicted    
    score,recommended_movie=sort_with_index_preserved(prediction_score,unique_movies)
    

    print("\n\n\nalgo 2:",recommended_movie)
    return recommended_movie

