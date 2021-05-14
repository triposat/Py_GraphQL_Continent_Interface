import requests
import json
# import pandas as pd


# A simple function to use requests.post to make the API call. Note the json= section.
def run_query(url, query):
    request = requests.post(url, json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))


data_to_fetch = {'url': 'https://countries.trevorblades.com/', 'query': """
{
  continents{
    code
    name
    countries{
      name
    }
  }
}
"""}


def main():
    print(run_query(data_to_fetch['url'],data_to_fetch['query']))


if __name__ == "__main__":
    main()
