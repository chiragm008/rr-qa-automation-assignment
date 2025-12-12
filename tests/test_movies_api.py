import pytest
import re
from utils.api_client import APIClient
from utils.logger import logger
import requests
from config.config import *

# END POINTS

POPULAR_MOVIES = "/movie/popular"
SEARCH_MOVIES = "/search/movie"
TRENDING_MOVIES = "/trending/movie/week"
NEWEST_MOVIES = "/movie/now_playing"
TOP_RATED_MOVIS = "/movie/top_rated"
POPULAR_TV = "/tv/popular"
TRENDING_TV = "/trending/tv/week"
NEWEST_TV = "/tv/now_playing"
TOP_RATED_TV = "/tv/top_rated"
SEARCH_TV = "/search/tv"
DISCOVER_MOVIES = "/discover/movie"


@pytest.mark.parametrize("API", [POPULAR_MOVIES, TRENDING_MOVIES, NEWEST_MOVIES, TOP_RATED_MOVIS])
def test_status_code_200(API):
    logger.info("Validating Status Code 200 for popular movies")
    resp = APIClient.get(API, {"page": 1})
    assert resp.status_code == 200

    logger.info("Checking response structure for popular movies")
    json_data = resp.json()
    assert "page" in json_data
    assert "results" in json_data
    assert "total_pages" in json_data
    assert "total_results" in json_data
    assert isinstance(json_data["results"], list)

    logger.info("Validating fields of first movie item")
    results = resp.json()["results"]
    if not results:
        pytest.skip("No movie results available")
    item = results[0]
    assert isinstance(item["id"], int)
    assert isinstance(item["adult"], bool)
    assert isinstance(item["genre_ids"], list)
    assert isinstance(item["original_language"], str)
    assert isinstance(item["overview"], str)
    assert isinstance(item["popularity"], float)
    assert isinstance(item["vote_count"], int)
    assert isinstance(item["vote_average"], (float, int))
    assert isinstance(item["title"], str)
    assert isinstance(item["original_title"], str)
    if item["release_date"]:
        assert re.match(r"\d{4}-\d{2}-\d{2}", item["release_date"])
    if item["poster_path"]:
        assert item["poster_path"].startswith("/")
def test_search_movies_results():
    logger.info("Testing search with invalid query returns empty list")
    resp = APIClient.get(SEARCH_MOVIES, {"query": "TRON ARES"})
    json_data = resp.json()
    assert resp.status_code == 200
    results = resp.json()["results"]
    if not results:
        pytest.skip("No movie results available")
    item = results[0]
    assert item["genre_ids"] == [878,12,28]
    assert item["id"] == 533533
    assert item["original_language"] == "en"
    assert item["original_title"] == "TRON: Ares"
    assert item["release_date"] == "2025-10-08"

def test_search_empty_results():
    logger.info("Testing search with invalid query returns empty list")
    resp = APIClient.get(SEARCH_MOVIES, {"query": "xyzinvalid123"})
    json_data = resp.json()
    assert resp.status_code == 200
    assert json_data["results"] == []

def test_invalid_api_key():
    logger.info("Testing invalid API key scenario")
    resp = requests.get("https://api.themoviedb.org/3/movie/popular", params={"api_key": "wrongkey"})
    assert resp.status_code == 401

def test_missing_api_key():
    logger.info("Testing missing API key scenario")
    resp = requests.get("https://api.themoviedb.org/3/movie/popular")
    assert resp.status_code == 401

def test_invalid_page_number():
    logger.info("Testing invalid page number")
    resp = APIClient.get(POPULAR_MOVIES, {"page": -5})
    assert resp.status_code == 400

@pytest.mark.parametrize("API", [POPULAR_MOVIES, TRENDING_MOVIES, NEWEST_MOVIES, TOP_RATED_MOVIS])
def test_pagination(API):
    logger.info(f"Testing pagination for {API}")
    resp = APIClient.get(API, {"page": 1})
    json_data = resp.json()
    assert json_data["page"] == 1
    resp = APIClient.get(API, {"page": 10})
    json_data = resp.json()
    assert json_data["page"] == 10

@pytest.mark.parametrize("param", [DISCOVER_NEWEST_PARAM, DISCOVER_TREND_PARAM, DISCOVER_POPULAR_PARAM, DISCOVER_TOP_RATED_PARAM])
def test_discover_endpoint(param):
    logger.info(f"Testing discover endpoint for {param}")
    resp = APIClient.get(DISCOVER_MOVIES, params=param)
    assert resp.status_code == 200
