import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from sort import sort_with_index_preserved

def predict_using_sklearn_surprise(top_10_list,all_people_top_10,verbose=True):
    '''
        this is the sibling algorithm to custom_algo
        it returns new_list given the current_list and other 
        peoples preferences in the field (movies or cast)
        it uses sklearn surprise liberary for that
    '''

    unique_genres=[]
    
    item=[]
    user=[]
    rating=[]
    user_name=1
    for i in all_people_top_10:
        count=0
        for j in i:
            if(j not in unique_genres):
                unique_genres.append(j)
            item.append(j)
            user.append(user_name)
            rating.append(10-count)
            count+=1
        user_name+=1   

    # each person's cast/genre_list is sorted hence the first element has the highest
    # priority hance it is easy to provide the rating for each element
    # each user has its item and each item has its rating
    # total size = n(user) * n(item per list) ; n denotes "number of"

    ratings_dict = {
        "item": item,
        "user": user,
        "rating": rating,
    }

    df = pd.DataFrame(ratings_dict)
    reader = Reader(rating_scale=(1, 10))

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
    for i in unique_genres:
        prediction_score.append(algo.predict('', i).est)
    score,recommended_genre=sort_with_index_preserved(prediction_score,unique_genres)
    new_genre_list=[]
    count=0
    for i in recommended_genre:
        if(count==5):
            break
        if(i not in top_10_list[:5]):
            new_genre_list.append(i)
        count+=1    
    if(verbose):    
        print("top item recommended (library): ",new_genre_list)     
    return new_genre_list