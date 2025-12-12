import requests
from config.config import BASE_URL, API_KEY
from utils.logger import logger

class APIClient:
    @staticmethod
    def get(endpoint, params=None):
        if params is None:
            params = {}
        params["api_key"] = API_KEY
        url = BASE_URL + endpoint
        logger.info(f"GET Request → URL: {url} PARAMS: {params}")
        response = requests.get(url, params=params)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text[:500]}")
        return response
