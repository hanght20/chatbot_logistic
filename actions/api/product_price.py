import json


def get_product_price(name, attribute):
    try:
        with open("actions/api/product_price.json", 'r',  encoding="utf8") as f:
            data = json.loads(f.read())
            for product in data:
                if product["name"] == str.lower(name):
                    return product[str.lower(attribute)]
    except Exception as e:
        print(str(e))
