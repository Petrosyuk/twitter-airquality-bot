import os
import requests as re

''' API wrapper for http://aqicn.org/ 
    Documentation on the API endpoint can be foud at the following links: 
        https://aqicn.org/api/ 
        https://aqicn.org/json-api/doc/
    '''

API_BASE_URL = 'https://api.waqi.info/feed'
API_TOKEN = os.getenv('AIR_QUALITY_OPEN_DATA_PLATFORM_TOKEN')

# lat_lang = (42.648376, -73.707518)

class AirQualityClient(object):
    def __init__(self):
        pass
    
    def get_by_loc(self, lat:float,lng:float):
        # Returns api data based on geo cordinates.
        rest_path = f'{API_BASE_URL}/geo:{lat};{lng}/?token={API_TOKEN}'
        rsp = re.get(rest_path)
        self._printer(rsp)

    def get_by_city(self,city:str):
        # Returns data by city name
        rest_path = f'{API_BASE_URL}/{city}/?token={API_TOKEN}'
        rsp = re.get(rest_path)
        self._printer(rsp)

    def _printer(self,rsp):
        # Returns filtered JSON data from the API response
        assert (rsp is not None), 'Response did not return an object.'
        # if rsp.status_code != 200:
        #     raise 
        print(rsp.status_code)
        json_object = rsp.json()
        print(json_object)
        return json_object


if __name__ == "__main__":
    aq = AirQualityClient()
    aq.get_by_loc(42.648376, -73.707518)