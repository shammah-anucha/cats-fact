# import requests
# # import json
# # from pygments import highlight
# # from pygments.formatters.terminal256 import Terminal256Formatter
# # from pygments.lexers.web import JsonLexer

# url = "https://catfact.ninja/fact"


# # request mock: to mock an access to the url
# # testing the return of the function which is the fact
# def cat_facts(url):
#     response = requests.get(url)
#     obj = response.json()
#     print(obj['fact'])

#     # # pretty print Json
#     # json_formatted_str = json.dumps(obj, indent=4)
#     # colorful_json = highlight(
#     #                           json_formatted_str,
#     #                           lexer=JsonLexer(),
#     #                           formatter=Terminal256Formatter()
#     #                           )
#     # status = response.status_code
#     # header = response.headers["Content-Type"]

#     # print(colorful_json)

#     # return colorful_json, status, header


# if __name__ == "__main__":
#     cat_facts(url)


# mock_response = mock.Mock(return_value=2)
# mock_response.json.return_value = {"fact": "This is a string"}
# mock_response.status_code = 200
# print(mock_response())
# print(mock_response.status_code)
# print(mock_response.json())


# mock_response = mock.Mock(name="mock_response", **{"status_code": 200, "json.return_value": {"fact": "This is a string"}})
# print(mock_response.status_code)
# print(mock_response.json())

# mock_requests_get = mock.Mock(return_value=mock_response)
# print(mock_requests_get().status_code)
# print(mock_requests_get().json())
# requests.get = mock_requests_get
# print(cat_facts())


# def test_cats_fact(monkeypatch):
#     def mock_get(*args, **kwargs):
#         return MockResponse()

#     monkeypatch.setattr(requests, "get", mock_get)
#     result = cat_facts()
#     assert result["mock_key"] == "This is a string"


# def test_cats_fact(monkeypatch):
#     monkeypatch.setitem(cat_facts.DEFAUL_CONFIG, "fact", "test_fact")

#     expected = "fact = test_fact"


# @mock.patch("requests.get")
# def test_cats_fact(mock_requests_get):
#     mock_requests_get.return_value = mock.Mock(
#         name="mock_response",
#         **{"status_code": 200, "json.return_value": {"fact": "This is a string"}}
#     )
#     assert cat_facts() == "This is a string"


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
