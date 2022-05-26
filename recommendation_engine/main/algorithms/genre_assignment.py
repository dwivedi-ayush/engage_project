from custom_algo import predict_using_custom_algo
from algo_2 import predict_using_sklearn_surprise
from emsamble_result import ensamble
from threading import Thread

def improve_genere_list(all_people_top_10,top_10_genre_list):
    '''
        it takes current top item list and top item list of all other prople
        it uses 2 algorithms to improve the top item list
        
    '''

    class ThreadWithReturnValue(Thread):
        def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
            Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None
        def run(self):
            # print(type(self._target))
            if self._target is not None:
                self._return = self._target(*self._args,**self._kwargs)
        def join(self, *args):
            Thread.join(self, *args)
            return self._return

    thread_list=[]

    #add all the alorithms that will predict the new genere to the thread list
    thread_list.append(ThreadWithReturnValue(target=predict_using_custom_algo,args=(top_10_genre_list,all_people_top_10)))
    thread_list.append(ThreadWithReturnValue(target=predict_using_sklearn_surprise,args=(top_10_genre_list,all_people_top_10)))
    

    for threads in thread_list:
        threads.start()

    result_list=[]
    for threads in thread_list:
        result_list.append(threads.join())
        # print(result_list)


    #here we are ensambling the results of various algorithms used
    top_5_calculated=ensamble(result_list,5)
    # print("combined*******",top_5_calculated)

    new_top_10_genere_list=top_10_genre_list[:5]
    new_top_10_genere_list.extend(top_5_calculated)

    return new_top_10_genere_list
