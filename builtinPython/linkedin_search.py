from linkedin import Linkedin
import settings as settings

# Authenticate using any Linkedin account credentials
api = Linkedin('YOUR EMAIL HERE', 'YOUR TOCKEN HERE')

# GET company information
companyInfo = api.get_company('YOUR COMPANY TO SEARCH')

print(companyInfo)