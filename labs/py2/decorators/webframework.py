'''
Create the scaffolding for a Flask-like framework.

>>> app = WebApp()
>>> @app.route("/")
... def index():
...     return 'Index Page'
...
>>> @app.route("/contact/")
... def contact():
...     return 'Contact Page'
...
>>> app.get("/")
'Index Page'
>>> app.get("/contact/")
'Contact Page'
>>> app.get("/no-such-page/")
'ERROR - no such page'


'''

# Write your code here:

class WebApp:
    """create a cache to store the routing information
            """
    cache = {}
    def route(self, *args):
        """store routing info in cache data structure
                argument as key and the invoker function as value
                """
        def wrapper(*abc):
            self.cache[args[0]] = abc[0]()
        return wrapper

    def get(self,*args, **kwargs):
        """seach value for argument in cache
                if found the return the value else return error message
                """
        if args[0] in self.cache:
            return self.cache.get(args[0])
        else:
            return 'ERROR - no such page'

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.
