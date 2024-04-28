"""
Pixela API Integration

This Python script demonstrates the integration with the Pixela API for creating and managing graphs to track daily activities. 
It includes functionality for creating a new user, defining a graph, posting values to the graph, updating existing values, and deleting values.

Libraries Used:
- requests: for making HTTP requests
- datetime: for working with dates and times

Usage:
- Replace USERNAME and TOKEN with your Pixela account username and API token, respectively.
- Uncomment the create_user and create_graph sections to create a new user and graph.
- Use the post_pixel method to post new values to the graph.
- Use the update_pixel method to update existing values on the graph.
- Use the delete_pixel method to delete existing values from the graph (optional).
- Run: $python3 main.py
"""

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "********"
TOKEN = "********"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create an user
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

#Create a grph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Running",
    "unit" : "km",
    "type" : "float",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# Go to url to check the graph
# https://pixe.la/v1/users/akw8989/graphs/graph1

#Poat a value to the graph
graph_post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

request_body = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5.1",
}

response = requests.post(url=graph_post_pixel, headers=headers, json=request_body)
print(response.text)

#Update - Put request
DATE = "20240413" #Format string : <YYYYMMdd>
graph_update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{DATE}"

new_pixel = {
    "quantity" : "10.2",
}

response = request_body.put(url=graph_update_pixel, json=new_pixel, headers=headers)
print(response.text)

#Delete
""" graph_delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{DATE}"

response = request_body.delete(url=graph_update_pixel, headers=headers)
print(response.text) """