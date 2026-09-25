import httpx
from typing import Optional
from pydantic import BaseModel,ConfigDict, ValidationError

class Product(BaseModel):
    model_config = ConfigDict(strict=True)
    id: int
    product_code:Optional[int] = None
    product_name:Optional[str]=None

class Location(BaseModel):
    model_config = ConfigDict(strict=True)
    id: int
    location_osm_id: Optional[int] = None
    location_osm_type:Optional[str] = None   


class foodrecord(BaseModel):
    model_config = ConfigDict(strict=True)
    id: int
    product_id:int
    location_id:int  
    proof_id:int
    location:Location
    product:Product
    

url = 'https://prices.openfoodfacts.org/api/v1/prices?size=1'

try:
      response = httpx.get(url)
      response.raise_for_status   
      data=response.json()
      record= data['items'][0]
      price = foodrecord.model_validate(record)

      print('validation successful')
      print(price)
      print('Product_code:',price.product.product_name)

except httpx.HTTPError as e:
    print(f'API request failed:{e}')

except ValueError:
    print('API did not return valid JSON record ')

except ValidationError as e:
    print('Pydantic validation failed:')
    print(e)    

