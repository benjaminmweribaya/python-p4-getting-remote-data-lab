import requests
import json

class GetRequester:

    def __init__(self, url):
        """
        Initializes the GetRequester with a URL.
        """
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the body of the response.
        """
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """
        Sends a GET request to the URL, retrieves the response, 
        and converts it into a Python dictionary or list.
        """
        response_body = self.get_response_body()
        return json.loads(response_body)  # Parse the JSON string into Python data