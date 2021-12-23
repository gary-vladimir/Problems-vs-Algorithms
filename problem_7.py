from collections import defaultdict


class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):

        path_parts = path.split("/")
        node = self.root

        for part in path_parts:
            if part != '':
                node = node.children[part]

        node.handler = handler

    def find(self, path):

        path_parts = path.split("/")
        node = self.root

        for part in path_parts:
            if part != '':
                node = node.children[part]

        return node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler


class Router:
    def __init__(self, root_handler):  self.route_trie = RouteTrie(
        root_handler)

    def add_handler(self, path, handler): self.route_trie.insert(path, handler)

    def lookup(self, path): return self.route_trie.find(path)


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler")
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
