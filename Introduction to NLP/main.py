import requests

from config import API_KEY

model_id = "facebook/bart-large-mnli"

api_url = "https://router.huggingface.co/hf-inference/models/{model_id}"

headers = {"Authorization" : f"Bearer {API_KEY}"}

topics = ["sports"  , "Technology" , "Business" , "Politics" , "Health"]



def ask_hf(headline : str) :

    payload = {"inputs" : headline , "parameters" : {"candidate_labels" : topics}}

    r = requests.post(api_url , headers= headers , json = payload , timeout= 30)

    if not r.ok :

        raise  RuntimeError(f"Hf error {r.status_code} : {r.text}")

    return r.json



def best_topic(preds : list) :

    best = max(preds , key = lambda x : x["score"])

    return best["label"] , best["score"]


def bar(score : float) :

    pct = score * 100

    blocks = int(pct // 10)

    return " " * blocks + " " * (10 - blocks)


def show(headline : str , preds : list) :

    top_label , top_score = best_topic(preds) 

    print("\n" + "=" * 60)

    print("??? News Topic Clasifier")

    print("=" * 60)

    print("Headline : " , headline)

    print("Best Tpoic : " , top_label)

    print("Confidense" , round(top_score * 100,1)) , "%" , bar(top_score)

    print("\n Top 3")

    top3 = sorted(preds , key = lambda x : x["score"] , reverse = True [:3])


    for i , p in enumarate(top3 , start = 1) :

