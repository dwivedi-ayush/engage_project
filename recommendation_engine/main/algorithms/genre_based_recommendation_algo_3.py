from fileinput import close
import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from sort import sort_with_index_preserved
from scipy import spatial
def genre_based_recommendation_algo_3(movies,top_10_genre,all_people_top_10):
    
    '''
        this algorithm starts off similar to algorithm 2 i.e. by finding closes 
        people to our target based on movie ratings but then we assign each movie
        a genre score (movie1-genre1-score1,movie1-genre2-score2,movie1-genre3-score3,...)
        then we use liberary to predict out top genre and movie score and then add them
        and sort them
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
    # this is the target user rating all the movies

    person_id.append(count_id)
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
    for i in range(1,6):
        closest_all_top_10.append(all_people_top_10[person_id[i]])
    
    '''
        from here this algorithm differs from algorithm 2 nad we will get 
        all the unique ganre from the closes people top genre
        then score the genre based on the popularity of that genre
        the more the occurance of that genre more the score
        then after each genre has its own score we will rate each movie
        rating will be genre-movie based more popular the genre more score that 
        movie-genre pair has then we will use sklearn surprise liberary and kNN to 
        predict the genre-movie pairwise score for the target users top genre and
        sort the movies accordingly
    '''


    temp_list=[]
    for genre_list in closest_all_top_10:
        for genre in genre_list:
            if (genre not in temp_list):
                temp_list.append(genre)
    score=dict()
    for genre in temp_list:
        score[genre]=1
    for genre in temp_list:
        for genre_list in closest_all_top_10:
            if(genre in genre_list):
                score[genre]+=1

    temp_score=0
    scores=[]
    movie_name=[]
    count=0
    genre_name=[]
    unique_movies=[]
    for genre in temp_list:
        count+=1
        for movie in movies:
            if(movie not in unique_movies):
                unique_movies.append(movie)
            temp_score=0
            movie_genres=movies[movie]["genre"]
            if(genre in movie_genres):
                temp_score+=score[genre]
            movie_name.append(movie)        
            scores.append(temp_score)
            genre_name.append(genre)
    ratings_dict = {
        "item": movie_name,
        "user": genre_name,
        "rating": scores,
    }    
    df = pd.DataFrame(ratings_dict)
    
    reader = Reader(rating_scale=(1, 50))

    data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)
    sim_options = {
        "name": "cosine",
        "user_based": False,  
    }
    algo = KNNWithMeans(sim_options=sim_options)
    trainingSet = data.build_full_trainset()
    algo.verbose=False
    a=algo.fit(trainingSet)
    prediction_score=[]
    movie_name=[]
    genre_name=[]
    for genre in top_10_genre:
        for movie in movies:
            prediction_score.append(algo.predict(genre, movie).est)
            movie_name.append(movie)
            genre_name.append(genre)
    movie_score=dict()
   
    for movie in movies:
        movie_score[movie]=0
    for movie in movies:            
        for i in range(len(prediction_score)):
            if(movie_name[i]==movie):
                movie_score[movie]+=prediction_score[i]

                
    score,recommended_movie=sort_with_index_preserved(list(movie_score.values()),list(movie_score.keys()))
    

    print("\n\n\nalgo3: ",recommended_movie)     
    return recommended_movie
