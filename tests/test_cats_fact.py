from cats_fact import __version__
from cats_fact.cats_fact import cat_facts
import requests
import pytest

# from unittest import mock


# import requests_mock


def test_version():
    assert __version__ == "0.1.0"


# monkey patch
# @mock.patch("requests.get")


class MockResponse:
    @staticmethod
    def json() -> dict:
        return {"fact": "This is a string"}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


def test_cats_fact(mock_response):
    result = cat_facts()
    assert result == "This is a string"
