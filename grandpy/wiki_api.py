import requests


class WikiApi:
    """
    Wiki Media API request object

    """

    def __init__(self, latitude, longitude):
        """
        Init method for the WikiApi class

        Parameters
        ----------
        latitude : from the GoogleApi class instance
        longitude : from the GoogleApi class instance

        """
        self.latitude = latitude
        self.longitude = longitude
        self.__get_proximate_place_id()

    def __get_proximate_place_id(self):
        """
        Return the page Id of a place closed to the returned address

        Returns
        -------
        place_id: int

        """
        payload = {
            "format": "json",
            "list": "geosearch",
            "gscoord": "{}|{}".format(self.latitude, self.longitude),
            "gslimit": "1",
            "gsradius": "1000",
            "action": "query",
        }
        response = requests.get(
            "https://en.wikipedia.org/w/api.php", params=payload)

        if response.status_code == 200:
            response_json = response.json()
            self.place_id = response_json["query"]["geosearch"][0]["pageid"]

    def get_anecdote_and_url(self):
        """
        Return anecdote and the url of the proximate place

        Returns
        -------
        anecdote: string
        url: string

        """

        payload = {
            "action": "query",
            "format": "json",
            "prop": "info|extracts",
            "pageids": "{}".format(self.place_id),
            "formatversion": "2",
            "exsentences": "1",
            "exlimit": "1",
            "explaintext": "1",
            "inprop": "url",
        }
        response = requests.get(
            "https://en.wikipedia.org/w/api.php", params=payload)

        r_json = response.json()
        anecdote = r_json["query"]["pages"][0]["extract"]
        url = r_json["query"]["pages"][0]["fullurl"]

        return anecdote, url
