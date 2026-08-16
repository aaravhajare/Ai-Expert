import pandas as pd
from textblob import TextBlob
from colorama import init , Fore
import time

init(autoreset=True)

try :
    df = pd.read_csv("imdb_top_1000.csv")

except FileNotFoundError :
    print(Fore.RED + "The db file was not found"); raise SystemExit

geners = sorted({g.strip() for xs in df["Gener"].dropna().str.split(", ") for g in xs})



def dots() :
    for _ in range(3) :
        print(Fore.YELLOW + "." , end = "" , flush=True , ); time.spleep(0.5)

def senti(p) :
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

def recomed(gener = None , mood = None , rating = None , n = 5) :
    d = df 

    if gener : d = d[df["Gener"].str.contains(gener , case=False , na=False)]

    if rating is not None : d = d[df["IMDB_Rating"] >= rating]

    if d.empty : return "No suitable movie recommendation for you"

    d , need , out = d.sample(frac=1 ).reset_index(drop=True) , bool(mood) , []

    for _ , r in d.iterrows :

        ov = r.get("Overview")

        if pd.isna(ov) : continue

        pol = TextBlob(ov).sentiment.polarity

        if (not need) or pol >= 0 :
            out.append((r["Series_Title"] , pol))

            if len(out) == n : break

    return out if out else "No suitable movie recommendation for you"


def show(recs , name) :
    print(Fore.YELLOW + f"\n Ai Analysed movie recommendation for you : {name}" )
    for i , (t ,p) in enumerate(recs , 1) :
        print(f"{Fore.CYAN}{i} . {t} (polarity {p:. 2f}  , {senti(p)}) ")

def get_gener() :
    print(Fore.GREEN + "Availavble GEnere :")
    for i , g in enumerate(geners , 1 ) : print(Fore.CYAN + i , "." , g)