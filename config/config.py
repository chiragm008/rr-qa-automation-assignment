BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "add494e96808c55b3ee7f940c9d5e5b6"
DEFAULT_PAGE = 1

DISCOVER_NEWEST_PARAM = {"sort_by" : "release_date.desc",
    "release_date.gte" : "1900-01-01",
    "release_date.lte" : "2025-12-31",
    "vote_average.gte" : 0,
    "vote_average.lte" : 5,
    "page" : 1,
    "with_genres" : 28,
    "api_key" : "add494e96808c55b3ee7f940c9d5e5b6"}


DISCOVER_TREND_PARAM = {"sort_by" : "vote_count.desc",
    "release_date.gte" : "1900-01-01",
    "release_date.lte" : "2025-12-31",
    "vote_average.gte" : 0,
    "vote_average.lte" : 5,
    "page" : 1,
    "with_genres" : 28,
    "api_key" : "add494e96808c55b3ee7f940c9d5e5b6"}

DISCOVER_POPULAR_PARAM = {"sort_by" : "popularity.desc",
    "release_date.gte" : "1900-01-01",
    "release_date.lte" : "2025-12-31",
    "vote_average.gte" : 0,
    "vote_average.lte" : 5,
    "page" : 1,
    "with_genres" : 28,
    "api_key" : "add494e96808c55b3ee7f940c9d5e5b6"}

DISCOVER_TOP_RATED_PARAM = {"sort_by" : "vote_average.desc",
    "release_date.gte" : "1900-01-01",
    "release_date.lte" : "2025-12-31",
    "vote_average.gte" : 0,
    "vote_average.lte" : 5,
    "page" : 1,
    "with_genres" : 28,
    "api_key" : "add494e96808c55b3ee7f940c9d5e5b6"}