from typing import List, Optional
import requests, logging

def auth_with_password(self, url: str, identity: str, password: str) -> Optional[str]: 
    try:
        response = requests.post(url=f'{url}/api/collections/users/auth-with-password',
                                data={'identity': identity, 'password': password}).json()
    except:
        logging.warning('Failed to authenticate, 400')
        return None
    return response['token']