# -*- coding: utf-8 -*-
import requests
import json


def get_wall(domain):
    vk_config = {"token": "d103d007e0ebb9606798bae7760eb2b6f486ee36049911ffc49d59ada57edbefd687583c4fed0a9947092",
                 "client_id": "7851141",
                 "version": "5.124",
                 "domain": "https://api.vk.com/method/"}

    req = requests.get(vk_config["domain"] + "wall.get", params = {"access_token": vk_config["token"],
                                                                   "v": vk_config["version"],
                                                                   "account_id": vk_config["client_id"],
                                                                   "domain": domain,
                                                                   "count": 100})

    posts_data = req.json()["response"]["items"]
    for i in range(len(posts_data)):
        data = posts_data[i]["text"]
        data = data.split()
        for word in data:
            word.split()
        corpus[len(corpus)] = {"post_text": posts_data[i]["text"],
                               "words": len(data)}


domain = "bubble"
corpus = {}
corpus_sum = 0
while len(corpus) < 200 or corpus_sum < 10000:
    corpus_sum = 0
    get_wall(domain)
    for i in range(len(corpus)):    
        corpus_sum += corpus[i]['words']

with open("corpus.json", "w", encoding="utf-8") as f:
    json.dump(corpus, f, ensure_ascii=False)

print("Группа: https://vk.com/" + domain)
print("Количество документов: ", len(corpus))
print("Общее число слов: ", corpus_sum)
print("Среднее количество слов на документ: ", round(corpus_sum/len(corpus)))