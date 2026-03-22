import requests

def fetch_product_details(query):
  url = f"https://world.openfoodfacts.org/cgi/search.pl"

  params = {
    "search_terms": query,
    "search_simple": 1,
    "action": "process",
    "json": 1
  }

  try:
    res = requests.get(url, params=params)
    data = res.json()

    if data["products"]:
      product = data["products"][0]  # take first match

      return {
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "ingredients_text": product.get("ingredients_text", "")
      }

  except Exception as e:
    print("API error:", e)

  return {} # in case nothing is found