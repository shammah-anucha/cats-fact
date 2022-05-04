from cats_fact import __version__
from cats_fact.cats_fact import cat_facts


url = "https://catfact.ninja/fact"
response, status, header = cat_facts(url)


def test_version():
    assert __version__ == '0.1.0'


def test_cat_facts_response():
    assert status == 200


def test_cat_facts_header():
    assert header == "application/json"


# def test_cat_facts_body():
#     response_body = response.json()
#     assert response_body['length'] == 61


# mocking - to test 