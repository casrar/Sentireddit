class Database():
    def auth_to_db(config):
        # error check and log
        response = requests.post(
            'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
            data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
        auth_token = response['token']
        return auth_token

    def get_data_sources(auth_token):
        # error check and log
        response = requests.get(
            'http://127.0.0.1:8090/api/collections/data_source/records', 
            headers={'Authorization': auth_token}).json()

        data_sources = []
        for i in range(response['totalItems']):
            data_sources.append(
                (response['items'][i]['subreddit'], 
                response['items'][i]['query'],
                response['items'][i]['id'])) 
        return data_sources

    def get_most_negative_data_record(first_date, second_date, data_source, auth_token):
        dates = ordered_form_date_to_unix(first_date=first_date, second_date=second_date)
        params = {
            'sort': '+neg',
            'perPage': '1',
            'filter': f'(data_source=\'{data_source}\' && created_timestamp >= {dates[0]} && created_timestamp <= {dates[1]})'
        }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=urlencode(params),
                                headers={'Authorization': auth_token}).json() 
        items = response['items']
        return items[0]['body'] if items else 'N/A'

    def get_most_positive_data_record(first_date, second_date, data_source, auth_token):
        dates = ordered_form_date_to_unix(first_date=first_date, second_date=second_date)
        params = {
            'sort': '-pos',
            'perPage': '1',
            'filter': f'(data_source=\'{data_source}\' && created_timestamp >= {dates[0]} && created_timestamp <= {dates[1]})'
        }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=urlencode(params),
                                headers={'Authorization': auth_token}).json() 
        items = response['items']
        return items[0]['body'] if items else 'N/A'

    def get_total_records(url, auth_token):
        params = { 'perPage': 1 }
        response = requests.get(url,
                                params=params,
                                headers={'Authorization': auth_token}).json()
        if response['totalItems'] < 1:
            return None
        return response['totalItems']

    def get_all_data(auth_token):
        per_page = get_total_records('http://127.0.0.1:8090/api/collections/data/records', auth_token=auth_token)
        if per_page and per_page < 1:
            return None
        params = { 'perPage': per_page }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=urlencode(params),
                                headers={'Authorization': auth_token}).json() 
        return response

    def get_all_data_sources(auth_token):
        per_page = get_total_records('http://127.0.0.1:8090/api/collections/data_source/records', auth_token=auth_token)
        if per_page and per_page < 1:
            return None
        params = { 'perPage': per_page }
        response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records',
                                params=params,
                                headers={'Authorization': auth_token}).json() 
        return response

    def get_all_data_in_date_range(first_date, second_date, data_source, auth_token):
        per_page = get_total_records('http://127.0.0.1:8090/api/collections/data/records', auth_token=auth_token)
        if per_page and per_page < 1:
            return None
        dates = ordered_form_date_to_unix(first_date=first_date, second_date=second_date)
        params = {
                'per_page': per_page,
                'filter': f'(data_source=\'{data_source}\' && created_timestamp >= {dates[0]} && created_timestamp <= {dates[1]})'
            }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=urlencode(params),
                                headers={'Authorization': auth_token}).json() 
        return response

    def get_all_data_from_data_source(data_source, auth_token):
        per_page = get_total_records('http://127.0.0.1:8090/api/collections/data/records', auth_token=auth_token)
        if per_page and per_page < 1:
            return None
        params = {
                'per_page': per_page,
                'filter': f'(data_source=\'{data_source}\')'
            }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=urlencode(params),
                                headers={'Authorization': auth_token}).json() 
        return response
