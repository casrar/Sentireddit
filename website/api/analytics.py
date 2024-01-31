@app.route('/update_graph', methods=['POST'])
def update_graph():
    context = {}
    chart_data = None

    validated_form = analytics.validate_analytics_form(request) 
    if validated_form is None:
        return render_template('partials/chart.html', context=context, chart_data=chart_data)
    chart_type, data_source, first_date, second_date = validated_form
    
    chart_data = analytics.generate_chart(chart_type=chart_type, first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    if chart_data is None:
        return render_template('partials/chart.html', context=context, chart_data=chart_data)

    return render_template('partials/chart.html', context=context, chart_data=chart_data)

@app.route('/update_data_source', methods=['POST'])
def update_data_source():
    context = {}
    chart_data = None
    
    validated_form = analytics.validate_analytics_form(request) 
    if validated_form is None:
        return render_template('partials/analytics_metrics.html', context=context, chart_data=chart_data)
    chart_type, data_source, first_date, second_date = validated_form

    chart_data = analytics.generate_chart(chart_type=chart_type, first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    if chart_data is None:
        return render_template('partials/chart.html', context=context, chart_data=chart_data)
    
    items = analytics.get_all_data_in_date_range(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)['items']
    if not items: # Return nothing if no data exists
        return render_template('partials/analytics_metrics.html', context=context, chart_data=chart_data)
    context['avg_compound'], context['avg_pos'], context['avg_neu'], context['avg_neg'] = analytics.calculate_average_sentiments(items)
    context['avg_compound'] = round(context['avg_compound'], 2)
    context['avg_pos'] = round(context['avg_pos'], 2)
    context['avg_neu'] = round(context['avg_neu'], 2) 
    context['avg_neg'] = round(context['avg_neg'], 2) 
    context['summary'] = analytics.sentiment_observation(context['avg_compound'])
    context['most_positive_post'] = analytics.get_most_positive_data_record(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    context['most_negative_post'] = analytics.get_most_negative_data_record(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    return render_template('partials/analytics_metrics.html', context=context, chart_data=chart_data)