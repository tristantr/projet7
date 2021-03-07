from grandpy.google_api import GoogleApi
from grandpy.wiki_api import WikiApi
from grandpy.response import Response

from tests.utils import response

def mock_GoogleApi_get_response(arg):
	return response.GOOGLE_API_RETURN

def mock_WikiApi_get_response(arg):
	return response.WIKI_API_RETURN

def test_get_response_if_keywords(monkeypatch):
	expected_result = response.RESPONSE_RETURN_OK
	monkeypatch.setattr('grandpy.google_api.GoogleApi.get_data', mock_GoogleApi_get_response)
	monkeypatch.setattr('grandpy.wiki_api.WikiApi.get_anecdote_and_url', mock_WikiApi_get_response)
	result = Response(response.MESSAGE).get_response()
	assert result == expected_result

def test_get_response_if_no_keywords(monkeypatch):
	expected_result = response.RESPONSE_RETURN_NOK
	result = Response("").get_response()
	assert result == expected_result