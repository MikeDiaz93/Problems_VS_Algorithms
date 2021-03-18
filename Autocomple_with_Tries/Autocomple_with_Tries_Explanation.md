# Problem 5:  "Autocomplete with Tries Explanation" 


## Objective:

We need to create a working trie for storing strings (2 classes are given). but we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie.

## Approach:

We implemented in the insert method, iterarte for every char in the word, but if this is not in the children , insert this into the au; and for the find method, iterate the char in suffixes and if this is not in the children, return none else change the char in the aux variable and finally return the aux variable. 

## Data Structure used: 

Lists


## Efficiency :
    
### Trie Class

#### Insert method 

    Time complexity:
    
        * O(n) -> About the number of characters in the word. The time complexity is lineal because iterate each char of the word.

    Space complexity:
    
        * O(n) -> Because we safe all the characters of the word.  

    
#### find method 

Time complexity:
    
    Time complexity:
    
        * O(n) -> Because we are in the parent child and then we go to the "n" character of the word.

    
    Space complexity:
    
        * O(n) -> Becuase we are looking for all the words.

    

### Class TrieNode Class

#### Insert method 

    Time complexity:
    
        * O(1) -> Because at the end we just add it to the dictionary.

    Space complexity:
    
        * O(1) -> Because we just save an element in the node.  

#### Suffix method 

    Time complexity:
    
        * O(n) -> Because n is the number of words we have in the trie. 

    Space complexity:
    
        * O(n) -> Because we just save n elements in the stack. 

