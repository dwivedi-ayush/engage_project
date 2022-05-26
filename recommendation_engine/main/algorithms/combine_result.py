def combine_result(genre_based_list,pre_watching_conditions_based_list):
    '''

        here we combine the lists giving priority to the genre based recommendation 
        because it comes first the pre watching condition will obviously have its 
        effect like time and weather but the genre holds more merit hence we give it priority

    '''
    recommended_movies=[]
    for movie in genre_based_list:
        if(movie in pre_watching_conditions_based_list):
            recommended_movies.append(movie)
    for movie in genre_based_list:
        if(movie not in recommended_movies):
            recommended_movies.append(movie)
    for movie in pre_watching_conditions_based_list:
        if(movie not in recommended_movies):
            recommended_movies.append(movie)
    return recommended_movies