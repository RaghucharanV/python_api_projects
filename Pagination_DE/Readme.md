# Python API Data Extraction and Pagination: Streamlining Data Retrieval and Navigation

## Resouces of Project

> Programming languages: Python, Requests lib, Pandas, Numpy

> API: ['https://rickandmortyapi.com/api/']

## About Project

Its an end to end data extraction from an api using requests and a python library. In this project, we extracted 42 pages of by using pagination method. 
The data that extracted into CSV file using pandas Library.



## About Code:

1.Pagination of API using request library

```python

def main_request(baseurl, endpoint,x):
    r = requests.get(baseurl+endpoint+ f'?page={x}')
    return r.json()


```

2. Extracting Data Using request and Pandas library

``` python

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name':item['name'],
            'no_ep': len(item['episode'])
        }
        charlist.append(char)
    return charlist


```


3. Saving Data into a CSV file of all pages in csv file

``` python

data = main_request(baseurl, endpoint,2)
mainlist =[]
for x in range(1,get_pages(data)+1):
    mainlist.extend(parse_json(main_request(baseurl, endpoint,x)))

df = pd.DataFrame(mainlist)

df.to_csv('charlist.csv',index= False)



```

The [charlist.csv]



