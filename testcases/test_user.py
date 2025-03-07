import requests


def test_user_album_count_passing():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    resp_dict = response.json()
    print(resp_dict)
    user_count = sum([1 for entry in resp_dict if entry["userId"] == 7])
    print('user_count=', user_count)
    assert user_count == 10

def test_user_album_count_failing():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    resp_dict = response.json()
    print(resp_dict)
    user_count = sum([1 for entry in resp_dict if entry["userId"] == 7])
    print('user_count=', user_count)
    assert user_count == 11