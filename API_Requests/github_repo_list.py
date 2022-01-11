#! /usr/bin/python3

import requests

user = input("What GitHub User would you like the details for : ")
api_url = "https://api.github.com/users/{}/repos".format(user)
response = requests.get(api_url)
my_projects = response.json()

for project in  my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")