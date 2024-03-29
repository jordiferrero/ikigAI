import requests


def get_most_relevant_image(search_query, api_key, per_page=1):
    """
    Function to search for the most relevant image based on a search text string using the Pexels API.

    Args:
    - search_query (str): The text to search for images.
    - api_key (str): Your Pexels API key.
    - per_page (int): Number of images per page to retrieve. Default is 1.

    Returns:
    - str: URL of the most relevant image.
    """
    # Pexels API endpoint for searching photos
    url = f"https://api.pexels.com/v1/search?query={search_query}&per_page={per_page}"

    # Headers containing the API key
    headers = {"Authorization": api_key}

    try:
        # Sending GET request to Pexels API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON response

        # Extract the URL of the most relevant image
        if data.get("photos"):
            relevant_image_url = data["photos"][0]["src"]["large"]
            return relevant_image_url
        else:
            print("No images found for the search query.")
            return None

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
