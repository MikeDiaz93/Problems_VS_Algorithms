# Problem  2: "Search in a Rotated Sorted Array" 


## Objective: 


You are given a sorted array which is rotated at some random pivot point. You are given a target value to search. If found in the array return its index, otherwise return -1.

## Approach

Once we find the pivot to find the 2 ordered sublist then we do the binary search in each sublist to find the value if it exist. 


## Data Structure used:


Lists. 



## Efficiency :

    Time complexity:
        
        * O(nlogn) - > Because it always makes binary search. 

    Space complexity:
    
        * O(1) -> Because all the time we have the  list given as input. 
