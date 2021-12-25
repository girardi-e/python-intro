# First thing we'll do is import the requests library
import requests

# Define a variable with the URL of the API
api_url = "http://shibe.online/api/shibes?count=1"

# adding parameters (based on api documentation)
params = {
    "count": 5
}

# Call the root of the api with GET, store the answer in a response variable
# Pass params in with the request (optional)
# This call will return a list of URLs that represent dog pictures
response = requests.get(api_url, params=params)

# Get the status code for the response. Should be 200 OK
# Which means everything worked as expected
status_code = response.status_code
print(f"Response status code is: {status_code}")

# Get the result as JSON
response_json = response.json()

# Print it. We should see a list with one image URL.
print(response_json)
