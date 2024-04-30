import os

from flask_login import login_user

def test_routes_defined(client, app_functional, new_user):
    for rule in app_functional.url_map.iter_rules():
        if("GET" in rule.methods):
            if(rule.endpoint != 'static'):
                response = client.get('/{}'.format(rule.endpoint))
                print("Testing Endpoint: {}".format(rule.endpoint))
                if(response.status_code == 401):
                    '''
                    if unauthorised access
                        1. login user
                        2. send another get request
                        3. assert response code == 200
                    '''
                    with app_functional.test_request_context():
                        login_user(new_user)
                        response = client.get('/{}'.format(rule.endpoint))
                        assert response.status_code == 200
                else:
                    #assert good response or redirect
                    assert response.status_code == 200 or 302