from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users" 
user_name="" #the usual
token="" #the ancient one

user_params = {
    "token":"", # only for create new one 
    "username":"", # only for creating new one
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
    }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

# https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"
test_graph = "graph1"

graph_config = {
    "id":"graph1",
    "name":"my first graph",
    "unit":"km",
    "type":"float",
    "color":"shibafu"
    }
headers={"X-USER-TOKEN":token}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = datetime(year=2025, month=8, day=4)

update_graph_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"36.8"
    }

update_graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{test_graph}"

response = requests.post(url=update_graph_endpoint, json=update_graph_params, headers=headers)
print(response.text)