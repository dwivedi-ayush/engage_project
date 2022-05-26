from sort import sort_with_index_preserved
from unique_scored import find_unique_and_scored

def predict_using_custom_algo(top_choice_list,all_people_top_choices,n=5,verbose=True):
    '''
        this is the sibling algorithm to algo_2
        it returns new_list given the current_list and other 
        peoples preferences in the field (movies or cast)
        1.first we collect the target uers top choices and
        score each other user based on the similarity of their top choices
        2.then we find the top n similar user
        3.then we take their top 5 choices (neglecting item already present in
        target users top 5 ) 
        4.then score them based on number of occurance
        5.then sort them based on the same
        and append the top 5 to the bottom five of the current list
    '''
    
    top_n=top_choice_list[0:n]
    idx=[]
    scores=[]
    count=0
    # giving each person a similarity score based on the top choices
    for item_list in all_people_top_choices:
        score=0
        idx.append(count)
        count+=1
        for item in top_n:
            if(item in item_list):
                score+=n*2-item_list.index(item)
        scores.append(score)        
    scores,idx=sort_with_index_preserved(scores,idx)       


    


    count=0
    top_people_top_choices=[]
    for i in idx:
        top_people_top_choices.append(all_people_top_choices[i])
        if(count==n-1):
            break
        count+=1    

          
    # this function returns unique items from a matrix and score them based on 
    # number of occurance in the matrix and sorted using merge sort
    idx,temp=find_unique_and_scored(all_people_top_choices,top_n)

    # temp is the list conataining the unique elements
    # idx is the list containing the indices of sorted items
    


    top_5_calculated=[]
    count=0
    for i in idx:
        top_5_calculated.append(temp[i])
        if(count==n-1):
            break
        count+=1  
    if(verbose):
        print("top new genre/cast recommended (custom algo): ",top_5_calculated)
    return top_5_calculated



