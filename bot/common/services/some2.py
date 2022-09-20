from pydantic import BaseModel


class Address(BaseModel):
    """
    Cat API Address definition
    """
    city: str
    zip_code: str
    number: int

class CatRequest(BaseModel):
    """
    Cat API Request definition
    """
    name: str
    age: int
    address: Address

my_json = {
    "name": "Lévy",
    "age": 3,
    "address": {
        "city": "Wonderland",
        "zip_code": "ABCDE",
        "number": 123
    }
}

data = CatRequest.parse_raw(' { "name": "Lévy", "age": 3, "address": { "city": "Wonderland", "zip_code": "ABCDE", "number": 123 }}')
data = CatRequest.parse_obj(my_json)
data.name  # Lévy
data.address.number # 123