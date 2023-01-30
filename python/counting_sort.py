def countingSort(arr):
    resultant = [0]*100
    
    for i in range(len(arr)):
        resultant[arr[i]] += 1
        
    return resultant

countinSort([1,1,3,4,2])
