def score_dictionary(genre_currently,movie_genre,all_current_genre_list=[]):
    '''
        used to score information contained as key value pairs
        returns a multiplication factor proportional to the score

        input data example:
        current weather is raing
        and in rainy times a person likes romantic movies
        so the function matches romantic with the genre of the movies
        and scores them accordingly then creates a multiplication factor by squeezing it below 1
    '''
    score=0
    for genre in genre_currently:
        if(genre in movie_genre):
                score += 1+len(all_current_genre_list)
    for genre in all_current_genre_list:
        if(genre in movie_genre):
                score += 1

                        
    normaliszed_score=(score/len(genre_currently))     
    return normaliszed_score
