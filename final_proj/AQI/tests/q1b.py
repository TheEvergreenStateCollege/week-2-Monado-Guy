test = {   'name': 'q1b',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> set(epa_data_CA.keys()) == set(['daily_county_aqi', 'daily_ozone', 'daily_so2', 'daily_co', 'daily_no2', 'daily_temp', 'daily_wind'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> epa_data_CA.get('daily_county_aqi')['State Name'].unique()[0] == 'California'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
