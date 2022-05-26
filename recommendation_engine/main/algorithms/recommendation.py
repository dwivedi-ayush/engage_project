from movie_recommendation import movie_recommendation_algo_1
from genre_assignment import improve_genere_list
from emsamble_result import ensamble
import json
from threading import Thread
from movie_genre_scoring import recommend_movie_based_on_genre


def recommend(all_people_top_10,all_people_top_cast,all_people_dictionary_data,movies,current_info,person_info):
    
    
    top_10_genre_list = person_info["genre_prefered"]
    new_top_10_genre_list = improve_genere_list(all_people_top_10, top_10_genre_list)
    
    movie_genre_dict = dict()
    for i in movies:
        for j in movies[i]:
            if(j == "genre"):
                movie_genre_dict[i] = movies[i][j]

    # recommend_movie_based_on_genre is imported from movie_genre_scoring.py
    recommended_movies_based_on_genre=recommend_movie_based_on_genre(movie_genre_dict,new_top_10_genre_list,movies,top_10_genre_list,all_people_top_10)

    #altering the thread class to return the resut once it is joined
    class ThreadWithReturnValue(Thread):
        def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
            Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None

        def run(self):
            # print(type(self._target))
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)

        def join(self, *args):
            Thread.join(self, *args)
            return self._return

    thread_list = []

    # now using following algorithms we can combine the result of genre based recommendation and current situitions like day,time,weather based movie recommendation
    # to add more algorithms we can simply add more threads to the list and rest will be handled by the ensamble logic
    # this current function is imported from movie_recommendation.py
    thread_list.append(ThreadWithReturnValue(target=movie_recommendation_algo_1, args=(person_info, current_info, recommended_movies_based_on_genre, movies, all_people_top_cast,all_people_dictionary_data)))


    for threads in thread_list:
        threads.start()

    result_list = []
    for threads in thread_list:
        result_list.append(threads.join())
        # print(result_list)

    # ensamble functions combines the result of various algorithms and returns the final result (even though here it is only one algorithm)
    # this function is imported from emsamble_result.py
    recommended_movies=ensamble(result_list,20)
    return recommended_movies
