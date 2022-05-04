from cats_fact import __version__
from cats_fact.cats_fact import cat_facts
from unittest import mock
# import requests
# import requests_mock


def test_version():
    assert __version__ == '0.1.0'


# monkey patch
# @mock.patch("requests.get")

def test_cats_fact(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock_response",
                                               **{"status_code": 200,
                                                  "json.return_value": {"fact": "This is a string"}})
    assert cat_facts() == 'This is a string'                                            
    

# def test_cats_fact(requests_mock):
#     requests_mock.get("https://catfact.ninja/fact", text='data')
#     assert cat_facts()



# url = "https://catfact.ninja/fact"
# response, status, header = cat_facts(url)



# def test_cat_facts_response():
#     assert status == 200


# def test_cat_facts_header():
#     assert header == "application/json"


# def test_cat_facts_body():
#     response_body = response.json()
#     assert response_body['length'] == 61


# mocking - to test 
