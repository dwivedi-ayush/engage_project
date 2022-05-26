
from sort import sort_with_index_preserved

def find_unique_and_scored(list_matrix,exclusion_list=[]):
    '''
        takes a matrix of list and returns unique and occuranced based 
        scored and sorted items as a list that are not in the exclusion list if provided
        internally uses merge sort

    '''
    temp=set()
    for i in list_matrix:
        if(i != None):
            for j in i:
                temp.add(j)
    temp=list(temp)
    scores=[]
    idx=[]
    count=0
    for i in temp:
        score=0
        idx.append(count)
        count+=1
        for j in list_matrix:
            if(i in j and i not in exclusion_list):
                score+=10-j.index(i)
        scores.append(score)        
    scores,idx=sort_with_index_preserved(scores,idx)
    return idx,temp 