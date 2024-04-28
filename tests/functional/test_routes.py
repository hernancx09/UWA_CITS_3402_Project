import os
from config import basedir

TEMPLATES = os.path.join(basedir, 'app/templates')

def test_routes_defined(client, app_functional):
    for rule in app_functional.url_map.iter_rules():
        if("GET" in rule.methods):
            if(rule.endpoint != 'static'):
                response = client.get('/{}'.format(rule.endpoint))

                print("Testing Endpoint: {}".format(rule.endpoint))
                assert response.status_code == 200
    '''
    for name in os.listdir(TEMPLATES):
        response = client.get('/{}'.format(name))

        assert response.status_code == 200
    '''