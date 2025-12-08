#Defines a function to access the files in the .env file
def loadEnv(fileName: str) -> str:
    """
    Docstring for getAPIKey

    Access the API KEY from the .env file

    Parameters:
    ----------
    fileName    :   str
                The name of the file in .env to access

    Returns:
    -------
    data    :   str
            The data contained in the file provided in the .env file
    """
    #imports os
    import os

    #Imports load_dotenv from dotenv
    from dotenv import load_dotenv

    load_dotenv()

    data = os.getenv(fileName)

    return data if data != None else f"{fileName} was not found in the .env file"

#Defines a function that returns the API url
def getURL()-> str:
    return "https://api.themoviedb.org/3/discover/movie"


#Defines a function that creates a session for the retry logic
def create_retry(total: int = 3, 
                 backoff_factor: float = 0.3, 
                 status_forcelist: tuple = (429, 500, 502, 503, 504), 
                 alllowed_methods: tuple = ("GET", "POST")) -> object:
    """

    Creates a logic to retry when quering an API


    Parameters:
    -----------
    total : int
            The maximum retries

    backoff_factor  :   int
                The base delay before another retry request is made

    status_forcelist    :   tuple
                A tuple of status codes to perform retries on

    allowed_methods     :   tuple
                    A tuple of HTTP allowed methods to be allowed to make the retry request

    Return:
        Retry session

    """
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    #Creates a session
    session = requests.Session()

    retries = Retry(
        total=total,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=alllowed_methods
    )

    adapter = HTTPAdapter(max_retries=retries)

    session.mount("https://", adapter)

    session.mount("https://", adapter)

    return session


def main():
    print(f"The API key is : \n{loadEnv(fileName="API_KEY")}")


if __name__ == "__main__":
    main()