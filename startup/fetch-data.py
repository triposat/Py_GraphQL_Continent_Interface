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

def convert_to_json(dict):
    return json.dumps(dict)

data_to_fetch = {
'url': 'https://countries.trevorblades.com/',
'query': """
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

def add_json_to_file(data):
    with open('data.json','w') as f:
        f.write(data)

def main():
    queried_data = run_query(data_to_fetch['url'],data_to_fetch['query'])
    queried_json = convert_to_json(queried_data)
    add_json_to_file(queried_json)



if __name__ == "__main__":
    main()
