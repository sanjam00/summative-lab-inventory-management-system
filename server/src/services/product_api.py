import requests

def normalize(text):
  return text.lower().strip() if text else ""

def score_product(product, query):
  # finds the best match based on name of product entered
  name = normalize(product.get("product_name", ""))
  query = normalize(query)

  score = 0

  # exact match gets highest score
  if query == name:
    score += 100

  # partial match
  if query in name:
    score += 50

  query_words = set(query.split())
  name_words = set(name.split())

  overlap = query_words.intersection(name_words)
  score += len(overlap) * 10

  return score

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

    products = data.get("products", [])

    if not products:
      return {}
    
    best_product = max(products, key=lambda p: score_product(p, query))

    return {
      "product_name": best_product.get("product_name", ""),
      "brands": best_product.get("brands", ""),
      "ingredients_text": (
        best_product.get("ingredients_text_en") or
        best_product.get("ingredients_text") or
        ""
      )
    }

  except Exception as e:
    print("API error:", e)

  return {} # in case nothing is found