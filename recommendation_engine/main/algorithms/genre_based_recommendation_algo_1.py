def genre_based_recommendation_algo_1(movie_genre_dict,new_top_10_genre_list):
    '''
        this function uses the newely formed new top 10 genre list (came from custom_algo.py)
        and uses it to score the movies according to the genre priority for a person
        and then normalises it using logit function to accomodate the whole movie genre coverage factor (completeness factor here)
        
    '''
    scores = {}
    for i in movie_genre_dict:
        score = 0
        count=0

        if(len(movie_genre_dict[i])<=10):
            division_factor=len(movie_genre_dict[i])
        else:
            division_factor=10

        addition_factor=10/division_factor
        for j in movie_genre_dict[i]:
            
            if (j in new_top_10_genre_list):
                count+=1
                score += addition_factor*(1 - new_top_10_genre_list.index(j)/9)
         
        completeness_factor=count/division_factor
        scores[i] = score*(1-(2.7)**(-1*completeness_factor))
        
    # if a movie contains 5 tags and all 5 are satisfied then it should be rewarded with extra points but if a movie has 20 genres tags and 6 of them are satisfied 
    # then it should not be rewareded as much because the movie tries to cover a very broad spectrum and thats is the only reason it satisfies for all the tags
    
    
    recommended_movies_based_on_genre = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    recommended_movies_based_on_genre = list(recommended_movies_based_on_genre.keys())
    print("\n\n\nalgo 1:",recommended_movies_based_on_genre)
    return recommended_movies_based_on_genre

# 20.724608275308853   38   0.8333333333333334
# 11.560051208396862   33   0.7
# 18.358063904019343   38   0.8
# 15.598734100953934   31   0.8
# 12.523946590098141   37   0.7
# 16.398765361701578   33   0.8
# 21.016965485301043   45   0.8

# see here 33^0.7< 31^0.8 that means even though 31<33 the compleness of 
# genre tags is given more importance but what if the movie had only 1 tag