import requests

class humorAPI:
    def __init__(self, joke=""):
        '''
        Sends over the data from the API
        args: self, joke. "joke" is one of the parameters from the API, that gets returned when this proxy class is called
        return: None
        '''
        limit = 1
        self.url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
        self.params = {
            'type': 'single',
            'category': joke
        }

    def get(self):
        '''
        Takes the data from the API, converts it into a json file, and then prints it out when this proxy class is called.
        args: self
        return: "joke" data
        '''
        r = requests.get(f'{self.url}?{self.params}', headers={'X-Api-Key':'frEz+k/OaaH4fYcwSsIxUg==myHIK3hhq76k9s6G'})
        response = r.json()
        joke_dict = response[0]
        return joke_dict["joke"]
    
    def __str__(self):
        '''
        Returns a string representation of object
        args: self
        return: string value
        '''
        return f'humorAPI(category={self.params["joke"]})'