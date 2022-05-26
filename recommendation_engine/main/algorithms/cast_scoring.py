from custom_algo import predict_using_custom_algo
from threading import Thread
from emsamble_result import ensamble
from algo_2 import predict_using_sklearn_surprise

def algo1(cast_preferred,all_people_top_cast,cast):
    # it basically uses custom_algo to predict new casts people would like and scores them
    cast_score=0
    predicted_cast=predict_using_custom_algo(cast_preferred,all_people_top_cast,5,False)
    predicted_cast.extend(cast_preferred)
    for preferred_cast in predicted_cast:
        if(preferred_cast in cast):
            cast_score+=1
    cast_score/=len(predicted_cast)
    return cast_score

def algo2(cast_preferred,all_people_top_cast,cast):
    # it  uses sklearn surprise liberary to predict new casts people would like and scores them

    cast_score=0
    predicted_cast=predict_using_sklearn_surprise(cast_preferred,all_people_top_cast,False)
    predicted_cast.extend(cast_preferred)
    for preferred_cast in predicted_cast:
        if(preferred_cast in cast):
            cast_score+=1
    cast_score/=len(predicted_cast)
    return cast_score
      

def score_cast(cast_preferred,all_people_top_cast,cast):
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

    # add all the alorithms that will predict the new genere to the thread list
    thread_list.append(ThreadWithReturnValue(target=algo1, args=(cast_preferred,all_people_top_cast,cast)))
    thread_list.append(ThreadWithReturnValue(target=algo2, args=(cast_preferred,all_people_top_cast,cast)))


    for threads in thread_list:
        threads.start()

    result_list = []
    for threads in thread_list:
        result_list.append(threads.join())
        # print(result_list)

    # the average of all result is returned
    return sum(result_list) / len(result_list)