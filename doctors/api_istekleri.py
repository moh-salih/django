import httpx


SIGN_IN_API_ENPOINT = 'https://api.uimconsulting.com/az/v2/auths'
def try_signing_in(email, password):
    status = {'message': ''}

    response = httpx.post(SIGN_IN_API_ENPOINT, data= {
        'username': email,
        'password': password
    })
    
    if response.status_code == 200:
        json_response = response.json()
        
        if 'message' in json_response:
            status['message'] = json_response['message']
        if 'data' in json_response:
            status['access_token'] = json_response['data']['token']
        
    return status


SIGN_UP_API_ENPOINT = 'https://api.uimconsulting.com/az/v2/users'
def try_signing_up(email, password):
    status = {'message': ''}

    response = httpx.post(SIGN_UP_API_ENPOINT, data= {
        'email': email,
        'password': password
    })
    
    # if response.status_code == 200:
    json_response = response.json()
    print(json_response)
    if 'message' in json_response:
        if type(json_response['message']) == list:
            status['message'] = json_response['message'][0]
        else:
            status['message'] = json_response['message']
    if 'data' in json_response:
        status['access_token'] = json_response['data']['token']
    print('Not 200: ', response.json())
    return status

