import requests
import pandas as pd
import argparse


def call_api(url, header=None):
    response = requests.get(url, headers=header)
    data = response.json()
    return data

def get_dataframe(data):
    df = pd.DataFrame(data)
    return df

try:
    url = "https://globalmart-api.onrender.com/mentorskool/v1/sales"
    parser = argparse.ArgumentParser()
    parser.add_argument('--access_token', help='Your access token')
    args = parser.parse_args()

    access_token = args.access_token
    print('Your access token is:', access_token)
    header = {"access_token": access_token}
    data = call_api(url, header=header)
    df = get_dataframe(data)
    print(df)

except IndexError:
    print("Invalid Index")

except requests.exceptions.HTTPError as err:
    print(err)
    
except requests.exceptions.RequestException as r:
    print(r)