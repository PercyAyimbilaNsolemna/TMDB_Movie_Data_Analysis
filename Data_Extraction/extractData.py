class ApiRequestError(Exception):
    """Base class for API request errors."""

#Imports pandas
import pandas as pd
from typing import Optional
import requests


#Defines a function that fetches data from an API and converts the data to a dataframe
def extractDataFromAPI(session: Optional[requests.Session], 
                       url: str, 
                       API_KEY: str,
                       movie_ids: list) -> pd.DataFrame: # Add return type pd.DataFrame
    """

    Queries an API (Movie Dataset API), extracts the dataset and convert it to a pandas dataFrame

    Parameters
    ----------
    sesssion    :   Session Object
                    Session object to handle retry logic

    url :   str
        The URL for the API

    API_KEY : str
            The API KEY for authentication

    movie_ids   :   list
                List of IDs for movies to be extracted

    maxPages    :   int
                Sets the default to 500
                The maximum number of pages to fetch

    Returns:
    -------
    CSV file
        CSV of all the data from the API (all movies from the Movie Dataset API)

    """
    import logging
    import json

    #Checks if the url and API KEY have been provieded
    if url is None and API_KEY is None:
        raise ValueError("URL and API Key are required but were not provided.")
    
    elif url is None:
        raise ValueError("URL is required but was not provided.")
    
    elif API_KEY is None:
        raise ValueError("API key is required but missing.")
    
    #Validation for movied IDs
    if not movie_ids:
        raise ValueError("Movie ID list cannot be empty")
    
    #Strips off any witespace from the url and the API Key
    url, API_KEY = url.strip(), API_KEY.strip()

    #Construct the structure of the header
    headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
    }
    
    #Creates a dataFrame to store the movie dataset
    df = pd.DataFrame()

    params = {
            "include_adult": True,
            "language": "en-US"
        }

    for count, movie_id in enumerate(movie_ids, start=1):
        endpoint = f"{url}/{movie_id}"
        try:
            response = session.get(url=endpoint, headers=headers, params=params, timeout=10)
        
        except requests.exceptions.Timeout:
            raise ApiRequestError("Request timed out. Check your internet connection and try again.")
        except requests.exceptions.ConnectionError:
            raise ApiRequestError("Unable to connect to server. Check your internet connection or the API URL.")
        except requests.exceptions.HTTPError:
            raise ApiRequestError(f"HTTP Error {e.response.status_code}: {e.response.reason}")
        except requests.exceptions.RequestException as e:
            raise ApiRequestError(f"Network error: {e}")

        #Proceed with the necessary details when call was successful 
        # Handle 404 Not Found
        if response.status_code == 404:
            #logger.info("Movie ID %s not found (404). Skipping.", movie_id)
            #failed_ids.append((movie_id, "not_found"))
            continue


        #Safe json parse
        try:
            json_data = json.loads(response.text)
        except ValueError:
            return "Invalid JSON received."


        if not json_data:
            break

        movie_df = pd.json_normalize(json_data)

        #Concat the page_df to the main df
        df = pd.concat([df, movie_df], ignore_index=True)

    return df
    

def main():
    import os
    import sys

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_root)

    from Config.config import loadEnv, getURL, create_retry

    url = getURL()
    API_KEY = loadEnv(fileName="API_KEY")
    movie_ids = [299534, 19995, 140607, 299536, 597, 135397, 420818, 24428, 168259, 99861,
                    284054, 12445, 181808, 330457, 351286, 109445, 321612, 260513]

    data = extractDataFromAPI(session=create_retry(), url=url, API_KEY=API_KEY, movie_ids=movie_ids)
    print(data.head())


if __name__ == "__main__":
        main()