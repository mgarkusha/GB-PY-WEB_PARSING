import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# Функция для апи GitHub.com
def github_repo(user_name):
    base_url = "https://api.github.com/users/" + user_name + "/repos"
    return requests.get(base_url, auth=(gh_username, gh_token))


# Креды GB
gh_username = os.getenv("gh_username")
gh_token = os.getenv("gh_token")

####################
# 1 Часть задания (про github)
####################
name = str(input("Введите имя пользователя GitHub.com: "))
r_gh = github_repo(name)

# Запись в файл
if r_gh.ok:
    if r_gh.status_code == 200:
        path = "repos_" + name + ".json"
        with open(path, "w") as f:
            json.dump(r_gh.json(), f, indent=2)
        print("Запись в файл " + "repos_" + name + ".json")
