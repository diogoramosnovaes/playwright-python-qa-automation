import os

def get_base_url():
    return os.getenv("base_url") or "https://www.saucedemo.com"

def get_api_url():
    return "https://petstore.swagger.io/v2"
