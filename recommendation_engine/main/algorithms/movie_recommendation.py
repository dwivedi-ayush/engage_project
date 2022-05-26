from sort import sort_with_index_preserved
from cast_scoring import score_cast
from extreme_tag_scoring import score_extreme_tag
from dictionary_scoring import score_dictionary
from mean_scoring import score_mean
from combine_result import combine_result


def movie_recommendation_algo_1(person_info, current_info, recommended_movies_based_on_genre, movies, all_people_top_cast,all_people_dictionary_data):
    recommended_movies = []
    multiplier = 20
    count = 1
    score = []
    idx = []
    number_of_movies = len(movies)
    for movie in recommended_movies_based_on_genre:
        if(count == 19 or count == number_of_movies):
            break
            # prevent division by 0 error

        current_score = 0
        idx.append(count - 1)

        genre = movies[movie]["genre"]
        length = movies[movie]["length"]
        cast = movies[movie]["cast"]
        year = movies[movie]["year"]
        extreme_tags = movies[movie]["extreme_tags"]

        # decide which factors matter the most and add the scores accordingly

        # 1 year
        year_diff_score = score_mean(person_info["average_year"], year, 100)
        current_score += year_diff_score * (20 - count)

        # 2 cast
        cast_score = score_cast(person_info["cast_prefered"], all_people_top_cast, cast)
        current_score += cast_score * (20 - count)

        # 3 extreme_tags
        current_score = score_extreme_tag(person_info["exclusion_list"], extreme_tags, current_score, count)

        # 4 length
        length_diff_score = score_mean(person_info["average_watchtime"], length, 100)
        current_score += length_diff_score * (20 - count)

        # 5 time
        time_score = score_dictionary(person_info["time_dictionary"][current_info["time_currently"]], movies[movie]["genre"],all_people_dictionary_data)
        current_score += time_score * (20 - count)

        # 6 weather
        weather_score = score_dictionary(person_info["weather_dictionary"][current_info["weather_currently"]], movies[movie]["genre"],all_people_dictionary_data)
        current_score += weather_score * (20 - count)

        # 7 day
        day_score = score_dictionary(person_info["day_dictionary"][current_info["day_currently"]], movies[movie]["genre"],all_people_dictionary_data)
        current_score += day_score * (20 - count)

        score.append(current_score)

        count += 1

    # this function sorts using merge sort and also returns the index of each element originally
    score, idx =sort_with_index_preserved(score, idx)

    movie_list = list(movies.keys())
    recommended_movies_based_on_pre_watching_conditions = []
    for index in idx:
        recommended_movies_based_on_pre_watching_conditions.append(movie_list[index])

    
    # combine the results giving priority to the commonly recommended movies first
    # this function is imported from combine_result.py
    recommended_movies = combine_result(recommended_movies_based_on_genre, recommended_movies_based_on_pre_watching_conditions)

    return recommended_movies
