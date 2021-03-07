from grandpy.cleaner import Cleaner
from grandpy.google_api import GoogleApi
from grandpy.wiki_api import WikiApi


class Response:
    """
    Build our response to return to the Ajax request in the Javascript file

    """

    def __init__(self, message):
        """
        Init method for the Response class

        Parameters
        ----------
        message : user input

        """
        self.message = message

    def get_response(self):
        """
        Build the response to return when the Ajax requests success

        Returns
        -------
        data_to_return: dict

        """
        keywords = Cleaner(self.message).clean_message()
        if keywords != []:
            address, latitude, longitude = GoogleApi(keywords).get_data()
            anecdote, url = WikiApi(latitude, longitude).get_anecdote_and_url()
            data_to_return = {
                "status": "ok",
                "address": address,
                "latitude": latitude,
                "longitude": longitude,
                "anecdote": anecdote,
                "url": url,
            }
        else:
            data_to_return = {"status": "nok"}
        return data_to_return
