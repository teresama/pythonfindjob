# Using LinkedIn API for searching companies #

One day you see yourself with a Master degree in your hand but no specific plan on what is your next step. 

*End goal:*


What if there is a Software tool that gives you ideas and suggestions of companies where you could work for? 

*But repo under construction, as of now:*


That is the motivation guiding me to use LinkedIn APIs with Python to find companies to get inspired and do a more automatic job search.

*** Disclaimer ***
LinkedIn can block your account in case it detects you are using the tool for commercial research purposes, or to automatically spy on profiles. Therefore it is recommended that your API calls are spaced in time.

## Let's start ##

This great post explains exactly how to start with our LinkedIn job search tool with creating a page and get our credentials [linkedinAPI](https://towardsdatascience.com/linkedin-api-python-programmatically-publishing-d88a03f08ff1).

## After having created your resources on LinkedIn... ##

2 options:

### For posting/modifying your LinkedIn profile: Using Linkedin API ###
Once you have followed the tutorial above, you should have the client ID and the client secret to add in lines 7 and 8 respectively of [linkedin_script.py](linkedin_script.py).


Run the file [linkedin_script.py](linkedin_script.py). If it is the first time running the script, you will obtain an auth_code. To obtain the auth_code, you will need to click the link generated in your console, that will redirect you to your default browser where you will need to login with your LinkedIn credentials. 

Once you have the code, add it in line 13 on [utils.py](utils.py). 
From now on, you will run the script [linkedin_script.py](linkedin_script.py) with "n" as a response. 

The functionality of the script is the following:

* POST: 
    * In profile: by calling *perform_profile_post()*
    * In page: by calling *perform_page_post()*
* GET: get information of your profile by calling *requests.post()*  

### For checking companies: Using a built-in Python API that requests LinkedIn urls ###

This LinkedIn API adapted to Python is obtained from: [linkedin-api](https://github.com/tomquirk/linkedin-api).

Simply add in [linkedin_search.py](builtinPython/linkedin_search.py) your email and the token associated to your account in line 5.

Request using the call *api.get_company()*.
