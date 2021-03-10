# Problem 3:  "Rearrange Array Digits" 


## Objective:

Rearrange Array Elements so as to form two number such that their sum is maximum.


## Approach:

We just ordered from minimum to maximum all the numbers and then we put the first number in the first string then we put the second number in the second string and so on with each number of the list. Finally we convert the strings in numbers and returned them in a tuple. 


## Data Structure used:

Lists.


## Efficiency :

    Time complexity:
        
        * O(nlogn) -> Because ordered them takes O(nlogn) plus O(n) that takes to travel the list and return the tuple of                                 numbers. 

    Space complexity:
    
        * O(1) -> Because the functions always return a tuple. 

    