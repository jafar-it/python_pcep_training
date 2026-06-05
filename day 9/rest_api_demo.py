import requests as req

# print(requests.__version__)

# GET request
# response = req.get("https://jsonplaceholder.typicode.com/posts")

# print("Status Code: ", response.status_code)
# print("Content: ", response.text)
# print("Headers: ", response.headers)
# print("In JSON")
# print(response.json())

#query parameters
#manual way - not recommended
# response = req.get("https://jsonplaceholder.typicode.com/posts?userId=1&id=2")

# best preactice
try:

    params = {
        # 'userId': 10,
        '_pages': 5,
        "_limit": 10
    }

    response = req.get("https://jsonplaceholder.typicode.com/posts", params=params)
    response.raise_for_status()  # raises HTTPError for status >=400
    posts = response.json()

    print(posts)

    # for post in posts[:10]:
    #     print(f"Id: {post['id']}, Title: {post['title']}")
except req.exceptions.HTTPError as e:
    print("Http Error: ", e)
except req.exceptions.RequestException as e:
    print("Something went wrong: ", e)

