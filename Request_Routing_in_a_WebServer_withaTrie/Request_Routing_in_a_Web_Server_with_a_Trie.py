
# A RouteTrie will store our routes and their associated handlers

class RouteTrie:
    def __init__(self, handler=None, not_found=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.not_found = not_found

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        aux = self.root
        for p in path:
            if p not in aux.children:
                aux.children[p] = RouteTrieNode(None)

            aux = aux.children[p]

        aux.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        if len(path) == 0:
            return self.root.handler

        aux = self.root
        for p in path:
            if p not in aux.children:
                return self.not_found

            aux = aux.children[p]

        if aux.handler == None:
            return self.not_found

        return aux.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,  handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, path, handler):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

        self.trie = RouteTrie(handler, not_found)
        self.trie.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        p = self.split_path(path)
        self.trie.insert(p, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        p = self.split_path(path)
        return self.trie.find(p)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        if path == '/':
            return []
        p = path.split('/')
        p.remove('')

        return p


# original test
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))


# Test 2
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/notes", "notes handles" ) # add a route 
router.add_handler("/payments", "payments handler") #add a route
router.add_handler("/records", " records handler") # add a route 
router.add_handler("/cart", "cart handler")  # add a route

#expected output : 'root handler'
print(router.lookup("")) 

#expected output : 'root handler'
print(router.lookup("/")) 

#expected output : 'not found handler'
print(router.lookup("/home")) 

#expected output : 'about handler'
print(router.lookup("/home/about")) 

#expected output : 'notes handler' 
print(router.lookup("/home/notes"))  

#expected output : 'not found handler' 
print(router.lookup("/home/notes/www")) 

#expected output : 'payments handler'
print(router.lookup("/payments")) 

#expected output : 'records handler' 
print(router.lookup("/records")) 

#expected output : 'not found handler'
print(router.lookup("/cart/yyy")) 

#expected output : 'not found handler'
print(router.lookup("/home/records")) 