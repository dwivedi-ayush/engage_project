from unique_scored import find_unique_and_scored

def ensamble(result_list,n=5):

    '''
        it takes a 2d list
        returns a list with unique elements 
        ranked based on most common occurance
    '''
    # atleast 5 values will be returned
    if(n<5):
        n=5

    idx,temp=find_unique_and_scored(result_list)

    if(n>len(temp)):
        n=len(temp)
        
    n-=1
    top_n_calculated=[]
    count=0
    for i in idx:
        top_n_calculated.append(temp[i])
        if(count==n):
            break
        count+=1  
        
    return top_n_calculated
