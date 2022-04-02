import requests
url = "https://api.yelp.com/v3/businesses/search"
api_key = "R4HCsyhxbgkPf7UAXlk2LvKsEyvJRxkBYLVfL7_keZuED3w7f0aEtgAvzNgCeY61cZxeFAVj0b9cNdSHIYml-AHEGXkPA3CW3sFxd6pOVUIb0CZ9GgJLKM85oqrOYHYx"
params = {
    "term": "Restaurant",
    "location": "Bentonville, AR"
}
headers = {
    "Authorization": "Bearer " + api_key
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
name = [business["name"] for business in businesses if business["rating"] > 4.5]
print(name)
#for business in businesses:
    #print(business["name"])