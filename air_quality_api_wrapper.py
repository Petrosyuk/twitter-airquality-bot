import os
import requests as re

''' API wrapper for http://aqicn.org/ 
    Documentation on the API endpoint can be foud at the following links: 
        https://aqicn.org/api/ 
        https://aqicn.org/json-api/doc/
    '''

API_BASE_URL = 'https://api.waqi.info/feed'
API_TOKEN = os.getenv('AIR_QUALITY_OPEN_DATA_PLATFORM_TOKEN')


def get_loc_results():
    lat_lang = (42.648376, -73.707518)

def get_city_feed():
    # Returns a city feed request status
    city = 'new york city'

    rest_path = f'{API_BASE_URL}/{city}/?token={API_TOKEN}'
    # rest_path = 'https://api.waqi.info/feed/shanghai/?token=demo'
    print(rest_path)
    rsp = re.get(rest_path)

    print(rsp.status_code)
    print(rsp.json())


if __name__ == "__main__":
    get_city_feed()
