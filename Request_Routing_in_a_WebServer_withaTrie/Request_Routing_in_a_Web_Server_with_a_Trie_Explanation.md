# Problem 7: "Request Routing in a Web Server with a Trie"



## Autocomplete with Tries Explanation


## Objective:

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.


## Approach:

It is like the Autocomplete with Tries Explanation problem, we implemented in the insert method, an iterarion for every word in the path, but if this is not in the children , insert this into the aux; and for the find method, iterate the word in path and if this is not in the children, return none found else change the word children to the aux variable and finally return the aux handler, if handle equals none, returns not found. 


## Data Structure used: 

Lists


## Efficiency :


### Roter Trie Node Class

#### Insert method 

    Time complexity:
        
        * O(n) -> Because we just add one element to the dictionary.

    Space complexity:
    
        * O(n) -> Because we just save one new element. 

 
### Route Trie Class

#### Insert method 

    Time complexity:
        
        * O(n) -> About the number of words in the path. The time complexity is lineal because iterate each p of the path.

    Space complexity:
    
        * O(n) -> Because we safe all the p's in the path. 

    

#### Find method 

     Time complexity:
        
        * O(n) -> About the number of words in the path. The time complexity is lineal because iterate each p of the path.

    Space complexity:
    
        * O(n) -> Because we safe all the p's in the path. 



### Router Class

####  Add handler method 

     Time complexity:
        
        * O(n) -> Because we just call the insert method of RouterTrie Class. 

    Space complexity:
    
        * O(n) -> Because we just call the insert method of RouterTrie Class. 


####  Look ip method 

     Time complexity:
        
        * O(n) -> Because we just call the find method of RouterTrie Class.

    Space complexity:
    
        * O(n) -> Because we just call the find method of RouterTrie Class.
        
        
####  split path method 

     Time complexity:
        
        * O(n) -> Because we iterate each char of the string, and when we find the char '/' we just divide the path and then continue.  

    Space complexity:
    
        * O(n) -> Because we just save all the strings in an array. 


