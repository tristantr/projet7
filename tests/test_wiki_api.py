from grandpy.wiki_api import WikiApi
from tests.utils import wikipedia

wikiApi = WikiApi(46.807719, 7.159642)

def test_get_anecdote_and_url(monkeypatch):
    expected_result = wikipedia.RESULT['query']['pages'][0]['extract'], \
                        wikipedia.RESULT['query']['pages'][0]['fullurl']
    response_json = wikipedia.RESULT
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
        def json(self):
            return response_json
    monkeypatch.setattr('requests.get', MockRequestsGet)
    result = wikiApi.get_anecdote_and_url()
    assert result == expected_result