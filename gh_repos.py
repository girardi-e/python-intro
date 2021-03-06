import requests


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    api_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)

    parameters = {
        "q": query,
        "sort": sort,
        "order": order
    }

    response = requests.get(api_search_url, params=parameters)

    # handling errors
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(
            f"Something went wrong! Status code was: {status_code}"
        )
    else:
        response_json = response.json()["items"]
        return response_json


if __name__ == "__main__":
    languages = ["Python", "Javascript", "Ruby"]
    # have a main method here
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
