import requests
from keys import TOKEN, USERNAME, GRAPH_ID
from datetime import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",   
}

#POST - Create User Account
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
# https://pixe.la/v1/users/iamsdawson/graphs/graph1.html

graph_config = {
    "id": GRAPH_ID,
    "name": "my cycling graph",
    "unit": "mile",
    "type": "float",   
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#POST - Create Graph
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


#POST - Create Pixel
pixel_creation_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today= dt.now()
# today = dt(year=2022, month=6, day=20)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "15"
# }

# #PUT Update Pixel
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)