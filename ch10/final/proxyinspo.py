import requests

class inspirationAPI:
    def __init__(self, quote="", author=""):
        '''
        Sends over data from the API
        args: self, quote, author. The quote and author parameters are parameters from the API, which get returned when the function
        is called
        return: None
        '''
        self.url = f'https://api.goprogram.ai/inspiration'
        self.params = {
            'type': 'single',
            'quote': quote,
            'author': author
        }

    def get(self):
        '''
        Takes the data from the API, converts it into a json file, and then prints it out when this proxy class is called.
        args: self
        return: "quote" and "author data
        '''
        r = requests.get(f'{self.url}?{self.params}')
        response = r.json()
        inspo_dict = response
        return inspo_dict["quote"], inspo_dict["author"]
    
    def __str__(self):
        '''
        Returns a string representation of object
        args: self
        return: string value
        '''
        quote, author = self.get()
        return f'"{quote}"\n- {author}'

        # quote1 = inspirationAPI(quote=self.params["quote"])
        # author1 = inspirationAPI(author=self.params["author"])
        # return quote1, author1