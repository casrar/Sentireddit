from typing import List
import requests

def auth_with_password(url: str, identity: str, password: str) -> str: 
    response = requests.post(url=f'{url}/api/admins/auth-with-password',
                            data={'identity': identity, 'password': password})
    response.raise_for_status()
    response = response.json()
    return response['token']

def __get_total_records(url: str, auth_token: str) -> int: 
    params = { 'perPage': 1 }
    response = requests.get(url,
                        params=params,
                        headers={'Authorization': auth_token})
    response.raise_for_status()
    response = response.json()
    return response['totalItems']
    
def get_all_data_sources(url: str, auth_token: str) -> List[dict]:
    url = f'{url}/api/data_source/records'
    per_page = __get_total_records(url=url, auth_token=auth_token)
    params = { 'perPage': per_page }
    response = requests.post(url=url,
                            params=params,
                            data={'Authorization': auth_token})
    response.raise_for_status()
    response = response.json()
    return response['items']

