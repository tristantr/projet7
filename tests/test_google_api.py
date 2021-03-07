from grandpy.google_api import GoogleApi
from tests.utils import google_place_api


def test_download_data(monkeypatch):
    expected_result = google_place_api.RESULT['candidates'][0]['formatted_address'], \
                        google_place_api.RESULT['candidates'][0]['geometry']['location']['lat'], \
                        google_place_api.RESULT['candidates'][0]['geometry']['location']['lng']
    reponse_json = google_place_api.RESULT                
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
        def json(self):
            return reponse_json
    monkeypatch.setattr('requests.get', MockRequestsGet)
    googleApi = GoogleApi('museum art history fribourg')
    result = googleApi.get_data()
    assert result == expected_result
