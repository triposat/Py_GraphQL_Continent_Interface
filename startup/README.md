# Project Startup

Using Graphql 

<a href="​https://countries.trevorblades.com/​">API URL</a>

to fetch data (query “​continents​” for listing the continents and “​continent​” for details of one continent), implement the following tasks:

●  Create a mobile optimized website with following two screens :
<ol>
<li> Interface showing continents List.
<li> Continent details interface (which is shown when user taps on any continent list item in the list interface in [1] )
</ol>

## What is <a href="https://graphql.org/"> GraphQL</a>?
GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data.

## Using python to connect with GraphQL API

Install following modules:

>1. requests (used to connect to GraphQL)
>2. json (used to parse GraphQL data)
>3. pandas (used for visibility of our data)

#### Import to python script
```python
import requests
import json
import pandas as pd
```

#### Request the API for data
```python
url = 'https://countries.trevorblades.com/'
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)
```
