import requests
import json

country = input("Enter country name: ")

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    country_data = data[0]

    name = country_data["name"]["common"]
    capital = country_data.get("capital", ["Unknown"])[0]
    population = country_data["population"]
    region = country_data["region"]
    subregion = country_data.get("subregion", "Unknown")

    languages = list(
        country_data.get("languages", {}).values()
    )

    currencies = list(
        country_data.get("currencies", {}).keys()
    )

    flag = country_data["flag"]

    result = {
        "name": name,
        "capital": capital,
        "population": population,
        "region": region,
        "subregion": subregion,
        "languages": languages,
        "currencies": currencies,
        "flag": flag
    }

    print("\n🌍 COUNTRY INFORMATION")
    print("----------------------")
    print("Name:", name)
    print("Capital:", capital)
    print("Population:", population)
    print("Region:", region)
    print("Subregion:", subregion)
    print("Languages:", ", ".join(languages))
    print("Currencies:", ", ".join(currencies))
    print("Flag:", flag)

    with open("country.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print("\n✅ country.json created!")

else:
    print("❌ Country not found.")