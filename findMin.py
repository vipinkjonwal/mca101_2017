myList=[11,5,0,10,18,3,7,6]
def minimum(myList,beginIndex,endIndex,index=0):
    '''
    Objective       : To find the index of minimum element in list.
    Input Variables :
            myList  : List defined as global variable.
        beginIndex  : Beginning index from the list.
        endIndex    : End index of the list upto minimum is needed to be computed.
            index   : DEFAULT 0, used to store the value of index of minimum element.
    Return Value    : index of minimum element in the list.        
    '''
    #Approach       : Use recursion to find the index pf minimum element.
    if (beginIndex!=endIndex):
        if(myList[beginIndex]<myList[endIndex]):
            minElement=myList[beginIndex]
            index=beginIndex
            endIndex-=1
            return minimum(myList,beginIndex,endIndex,index)
        else:
            minElement=myList[endIndex]
            index=endIndex
            beginIndex+=1
            return minimum(myList,beginIndex,endIndex,index)
    else:
        return beginIndex 
#Test Case 1
print(minimum(myList,0,5))
#Output : 2

#Test Case 2
print(minimum(myList,3,7))
#Output : 5

#Test Case 3
print(minimum(myList,5,5))
#Output : 5
