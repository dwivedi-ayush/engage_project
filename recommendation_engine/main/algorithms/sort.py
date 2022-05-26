'''
    merge sort algorithm that also returns the index of the sorted array so 
    that other dependencies with the same indexing can also be accessed without sorting again
'''
def merge(arr, idx, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    
    L = [0] * (n1)
    R = [0] * (n2)
    L_idx = [0] * (n1)
    R_idx = [0] * (n2)
 
    
    for i in range(0, n1):
        L[i] = arr[l + i]
        L_idx[i] = idx[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R_idx[j] = idx[m + 1 + j]
 
    
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k] = L[i]
            idx[k] = L_idx[i]
            i += 1
        else:
            arr[k] = R[j]
            idx[k] = R_idx[j]
            j += 1
        k += 1
 
    
    while i < n1:
        arr[k] = L[i]
        idx[k] = L_idx[i]
        i += 1
        k += 1
 
    
    while j < n2:
        arr[k] = R[j]
        idx[k] = R_idx[j]
        j += 1
        k += 1
 

 
 
def mergeSort(arr,idx, l, r):
    if l < r:
 
        m = l+(r-l)//2
 
        mergeSort(arr,idx, l, m)
        mergeSort(arr,idx, m+1, r)
        merge(arr,idx, l, m, r)
 
 
def sort_with_index_preserved(scores,idx):
    n=len(scores)
    mergeSort(scores,idx ,0, n-1)
    # print(scores)
    return scores,idx

