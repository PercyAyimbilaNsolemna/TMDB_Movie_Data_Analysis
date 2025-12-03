
#Imports pandas
import pandas as pd

#Defines a function that fetches data from an API and converts the data to a dataframe
def extractDataFromAPI(url: str, API_KEY: str, maxPages: int = 500) -> pd.DataFrame: # Add return type pd.DataFrame
    """

    Queries an API (Movie Dataset API), extracts the dataset and convert it to a pandas dataFrame

    Parameters
    ----------
    url :   str
        The URL for the API

    API_KEY : str
            The API KEY for authentication

    maxPages    :   int
                Sets the default to 500
                The maximum number of pages to fetch

    Returns:
    -------
    pd.dataFrame
        DataFRame of all the data from the API (all movies from the Movie Dataset API)

    """

    import requests

    #Checks if the url and API KEY have been provieded
    if url is None and API_KEY is None:
        raise ValueError("URL and API Key are required but were not provided.")
    
    elif url is None:
        raise ValueError("URL is required but was not provided.")
    
    elif API_KEY is None:
        raise ValueError("API key is required but missing.")
    
    #Strips off any witespace from the url and the API Key
    url, API_KEY = url.strip(), API_KEY.strip()

    #Construct the structure of the header
    headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
    }
    
    #Creates a dataFrame to store the movie dataset
    df = pd.DataFrame()

    #Declares and initialize page to the first page
    page = 1

    while page <= maxPages:
        params = {
            "page": page,
            "include_adult": True,
            "language": "en-US"
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()

        except requests.exceptions.Timeout:
            return "Request timed out. Check your internet connection and try again"
        except requests.exceptions.ConnectionError:
            return "Unable to connect to server. Check your internet connection or the API URL"
        except requests.exceptions.HTTPError:
            return f"HTTP Error {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Network error: {e}"

        #Safe json parse
        try:
            json_data = response.json()
        except ValueError:
            return "Invalid JSON received."

        results = json_data.get("results", [])

        if not results:
            break

        page_df = pd.json_normalize(results)

        #Concat the page_df to the main df
        df = pd.concat([df, page_df], ignore_index=True)

        print(f"Page {page} loaded ({len(page_df)} rows)")

        if page >= json_data.get("total_pages", 0):
            break

        page += 1

    return df
    

def main():
    import os
    import sys

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_root)

    from Config.config import loadEnv

    url = "https://api.themoviedb.org/3/discover/movie"
    API_KEY = loadEnv(fileName="API_KEY")
    data = extractDataFromAPI(url, API_KEY, maxPages=2)
    print(data.head())

if __name__ == "__main__":
    main()