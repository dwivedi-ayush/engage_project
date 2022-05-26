from genre_based_recommendation_algo_1 import genre_based_recommendation_algo_1
from genre_based_recommendation_algo_2 import genre_based_recommendation_algo_2
from genre_based_recommendation_algo_3 import genre_based_recommendation_algo_3
from threading import Thread
from emsamble_result import ensamble
def recommend_movie_based_on_genre(movie_genre_dict,new_top_10_genre_list,movies,top_10_genre,all_people_top_10):
    
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

    # here 3 algorithms are used to recommend movies based on genre
    # 1 uses a custom made algorithm (see the documentation for more details)
    thread_list.append(ThreadWithReturnValue(target=genre_based_recommendation_algo_1, args=(movie_genre_dict,new_top_10_genre_list)))
    # 2 uses sklaern surprise library for movie-closest_people scoring 
    thread_list.append(ThreadWithReturnValue(target=genre_based_recommendation_algo_2, args=(movies,top_10_genre,all_people_top_10)))
    # 3 uses sklearn surprise library for movie-top_genre scoring
    thread_list.append(ThreadWithReturnValue(target=genre_based_recommendation_algo_3, args=(movies,top_10_genre,all_people_top_10)))


    for threads in thread_list:
        threads.start()

    result_list = []
    for threads in thread_list:
        result_list.append(threads.join())
        # print(result_list)

    recommended_movies=ensamble(result_list,20)
    return recommended_movies

    


