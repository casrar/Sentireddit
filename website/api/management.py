from flask import Blueprint

bp = Blueprint("management", __name__)

@app.route('/data_management', methods=['POST', 'GET'])
def data_management():
    context = {}
    try:
        context['data_sources'] = analytics.get_all_data_sources(auth_token)['items']
        context['data'] = analytics.get_all_data(auth_token)['items']
    except:
        if 'data_sources' not in context:
            context['data_sources'] = {}
        if 'data' not in context:
            context['data'] = {}

    return render_template('data_management.html', context=context)

@app.route('/add_data_source', methods=['POST'])
def add_data_source():
    context = {}
    data = {
        'subreddit': request.form['subreddit'],
        'query': request.form['query']
    }
    response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records',
                                json=data).json()     
    context['data_sources'] = analytics.get_all_data_sources(auth_token)['items']
    return render_template('/partials/data_sources.html', context=context)

@app.route('/remove_data_source', methods=['DELETE'])
def remove_data_source():
    context = {}
    selected_data = request.form.getlist('selected-data')
    data = []
    for id in selected_data:
        data += analytics.get_all_data_from_data_source(data_source=id, auth_token=auth_token)['items']
    for item in data: 
        id = item['id']
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data/records/{id}')

    for id in selected_data:
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data_source/records/{id}')
    try:
        context['data_sources'] = analytics.get_all_data_sources(auth_token)['items']
        context['data'] = analytics.get_all_data(auth_token)['items']
    except:
        if 'data_sources' not in context:
            context['data_sources'] = {}
        if 'data' not in context:
            context['data'] = {}
    return render_template('/partials/data_sources_and_data.html', context=context)

@app.route('/remove_data', methods=['DELETE'])
def remove_data():
    context = {}
    selected_data = request.form.getlist('selected-data')
    for id in selected_data:
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data/records/{id}')
    context['data'] = analytics.get_all_data(auth_token)['items']
        
    return render_template('/partials/data.html', context=context)