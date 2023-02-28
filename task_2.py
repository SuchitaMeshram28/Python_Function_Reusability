import requests
import json
import pandas as pd

def call_api(url, header=None):
    """
    This function is created to fetch add from api source.

    Parameters: 
    url: It is the endpoint url of the API source which is used to retrieve data.
    header: Parameters required to authenticate the API source like access token.

    After fetching the data, it is being converted and collected into json format.

    Return: The final result is returned in json format.  
    """
    response = requests.get(url, headers=header)
    data = json.loads(response.text)
    return data


def get_dataframe(data):
    """
    This function is created to convert the json data which is fetched from the API source into a dataframe.

    Parameters: 
    data: A json format data which needs to be converted

    Return: Final data is returned in the form of pandas.DataFrame. 
    """
    df = pd.json_normalize(data, record_path='data')
    return df

try:
    url = "https://globalmart-api.onrender.com/mentorskool/v1/sales"
    header = {"access_token": 'fe66583bfe5185048c66571293e0d358'}
    data = call_api(url, header=header)
    # print(data)
    df = get_dataframe(data)
    print(df.head())
    print(df.columns)

except IndexError:
    print("Invalid Index")

except requests.exceptions.HTTPError as err:
    print(err)
    
except requests.exceptions.RequestException as r:
    print(r)
