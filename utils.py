import requests
import string
import random

client_id    = '78vykx2qlhr17d'
client_secret = 'HRLCcOtteCpRmlJi'
redirect_uri = 'http://localhost:8000'


def get_request_auth_code(first_time):
    if not first_time:
        # latest obtained auth_code
        auth_code = 'YOUR AUTH_CODE HERE'
        return auth_code
    else:
        # Generate a random string to protect against cross-site request forgery
        letters = string.ascii_lowercase
        csrf_token = ''.join(random.choice(letters) for i in range(24))

        # Request authentication URL
        auth_params = {'response_type': 'code',
                    'client_id': client_id,
                    'redirect_uri': redirect_uri,
                    'state': csrf_token,
                    'scope': 'r_liteprofile,r_emailaddress,w_member_social'} 

        html = requests.get("https://www.linkedin.com/oauth/v2/authorization",
                            params = auth_params)

        # Print the link to the approval page
        print(html.url)

        print("used this state string ", csrf_token)

        return "clickthelink"

def get_token(auth_code, first_time):

    if not first_time:
        # previously obtained token
        token = 'AQXSEEYm5TLajZ6tpihTU2P464_sA8uv6_qfBF2GaFlPZyr6XgZRQjOczndKdehZiDtUHCLuEYc39JlL8WJrDV_nnFGwitsiSQEbtijpxGlhhIjVSTNDLWcFKu9DniihgcQ6Lrb7oQZarVwzd55DYBGyHsdvakQNUkGSejFUOq63BUmrBz99YA6oM0hxpWx8YROA8c_ShJ4TM-0HwvVeCbqT7tWGwKUKtNNv3hty37ZNWoEFuYkay5vEAqJWj4zvx4RGM2mScK9PSYmo-Od6YIlymlZL77xS4eCBbXq_5henS8HhYdIuD4Kbwsezi87wjOvZT-XEOX2MkLSEEvMBBQsuw4HBJg'
        return token
    else:
        access_token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

        qd = {'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret}

        response = requests.post(access_token_url, data=qd, timeout=60)
        response = response.json()

        print(response)

        access_token = response['access_token']

        print ("Access Token:", access_token)
        print ("Expires in (seconds):", response['expires_in'])
        return access_token

def perform_profile_post(token):

    access_token = token
    profile_id = "AU3j1zdnt6"

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0',
            'Authorization': 'Bearer ' + access_token}
    post_data = {
        "author": "urn:li:person:"+profile_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    # "text": "Hello World! This is my first Share on LinkedIn!!"
                    "text": "I would like to thank the community for providing me with the title of MSc in Embedded Systems"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post(url, headers=headers, json=post_data)
    return response

def perform_page_post(token):

    organization_id = '74232151'
    access_token = token

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0',
            'Authorization': 'Bearer ' + access_token}
    post_data = {
        "author": "urn:li:organization:"+organization_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "Hello World! This is my first Share on LinkedIn from my organization!"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post(url, headers=headers, json=post_data)
    return response
    
