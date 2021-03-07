import requests
import os
import json
from .logger import logger


class GoogleApi:
    """
    Google API request object

    """

    def __init__(self, keywords):
        """
        Init method for the GoogleApi class

        Parameters
        ----------
        keywords : remaining keywords after cleaning the user input

        """
        self.keywords = keywords

    def get_data(self):
        """
        Return data from the Google Api request

        Returns
        -------
        address: string
        latitude: float
        longitude: float

        """
        logger.info(os.environ.get('GOOGLE_KEY'))
        payload = {
            "input": "{}".format(self.keywords),
            "inputtype": "textquery",
            "fields": "formatted_address,geometry,name",
            "key": os.environ["GOOGLE_KEY"]
        }
        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/json",
            params=payload,
        )

        if response.status_code == 200:
            address = response.json()["candidates"][0]["formatted_address"]
            latitude = response.json()[
                 "candidates"][0]["geometry"]["location"]["lat"]
            longitude = response.json()[
                "candidates"][0]["geometry"]["location"]["lng"]

        return address, latitude, longitude
