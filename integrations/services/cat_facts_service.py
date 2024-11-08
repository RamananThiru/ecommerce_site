import requests

def get_random_cat_fact():
    """
    Fetches a random cat fact from the catfact.ninja API.

    Returns: json response with fact info
    """
    url = 'https://catfact.ninja/fact'
    try:
        response = requests.get(url)
        data = response.json()
        data['success'] = True
        return data
    except requests.exceptions.RequestException as e:
        return { 'success': False, 'message': 'Something Went Wrong', 'error': str(e) }
