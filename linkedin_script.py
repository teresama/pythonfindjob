import requests
import string
import random
from utils import get_request_auth_code, get_token, perform_profile_post, perform_page_post

#objective: access a company profile and display the similar companies option 
client_id    = 'YOURCLIENTID'
client_secret = 'YOURCLIENTSECRET'

def main():
    
    # To get auth_code
    inp_letter = input("first time running script (do you have an auth code)? (y/n)")
    while (inp_letter != "y") and (inp_letter != "n"):
        inp_letter = input("first time running script (do you have an auth code)? (y/n)")
    if inp_letter == "n":
        first_time = False
    else:
        first_time = True
    auth_code = get_request_auth_code(first_time)
    if auth_code == "clickthelink":
        print()
        print("Please click the link above and search for string after code= ...., that is your auth_code")
        return "click"    
    else:
        #To get token
        first_time_token = False
        token = get_token(auth_code, first_time_token) 
    

    ############## POSTING ###############
    # As of now I can only access my profile
    # response = perform_profile_post(token)

    # If I get marketing for done, uncomment
    # response = perform_page_post(token)

    # print(response) #if response == 201 success, if response == 403, forbidden
    
    ############## GETTING ###############
    #commands for getting can be done through curl:
    # curl -H "Authorization: Bearer <YOUR AUTH CODE>" -X GET "https://api.linkedin.com/v2/me"

    # get a 2-legged authorization code.  
    access_token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

    qd = {'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret}

    response = requests.post(access_token_url, data=qd)
    response = response.json()

    print(response)

    access_token = response['access_token']

    print ("Access Token:", access_token)

    
    return response


if __name__ == '__main__':
    main()