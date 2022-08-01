# xkcd_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import xkcd_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import xkcd_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import xkcd_client
from pprint import pprint
from xkcd_client.api import api_api
from xkcd_client.model.bot_user import BotUser
from xkcd_client.model.token_obtain_pair import TokenObtainPair
from xkcd_client.model.token_refresh import TokenRefresh
from xkcd_client.model.vpn_country import VpnCountry
from xkcd_client.model.vpn_device_tariff import VpnDeviceTariff
from xkcd_client.model.vpn_duration_price import VpnDurationPrice
from xkcd_client.model.vpn_item import VpnItem
from xkcd_client.model.vpn_protocol import VpnProtocol
from xkcd_client.model.vpn_subscription import VpnSubscription
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with xkcd_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    bot_user = BotUser(
        user_id=-9223372036854775808,
        user_name="user_name_example",
        first_name="first_name_example",
        last_name="last_name_example",
        is_bot_blocked=True,
    ) # BotUser |  (optional)

    try:
        api_response = api_instance.create_bot_user(bot_user=bot_user)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_bot_user: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**create_bot_user**](docs/ApiApi.md#create_bot_user) | **POST** /api/v1/bot_user/create | 
*ApiApi* | [**create_token_obtain_pair**](docs/ApiApi.md#create_token_obtain_pair) | **POST** /api/v1/token/ | 
*ApiApi* | [**create_token_refresh**](docs/ApiApi.md#create_token_refresh) | **POST** /api/v1/token/refresh/ | 
*ApiApi* | [**create_vpn_country**](docs/ApiApi.md#create_vpn_country) | **POST** /api/v1/vpn-country/ | 
*ApiApi* | [**create_vpn_device_tariff**](docs/ApiApi.md#create_vpn_device_tariff) | **POST** /api/v1/vpn-device-tariff/ | 
*ApiApi* | [**create_vpn_duration_price**](docs/ApiApi.md#create_vpn_duration_price) | **POST** /api/v1/vpn-duration-price/ | 
*ApiApi* | [**create_vpn_item**](docs/ApiApi.md#create_vpn_item) | **POST** /api/v1/vpn-item/ | 
*ApiApi* | [**create_vpn_protocol**](docs/ApiApi.md#create_vpn_protocol) | **POST** /api/v1/vpn-protocol/ | 
*ApiApi* | [**create_vpn_subscription**](docs/ApiApi.md#create_vpn_subscription) | **POST** /api/v1/vpn-subscription/ | 
*ApiApi* | [**destroy_vpn_country**](docs/ApiApi.md#destroy_vpn_country) | **DELETE** /api/v1/vpn-country/{pkid}/ | 
*ApiApi* | [**destroy_vpn_device_tariff**](docs/ApiApi.md#destroy_vpn_device_tariff) | **DELETE** /api/v1/vpn-device-tariff/{pkid}/ | 
*ApiApi* | [**destroy_vpn_duration_price**](docs/ApiApi.md#destroy_vpn_duration_price) | **DELETE** /api/v1/vpn-duration-price/{pkid}/ | 
*ApiApi* | [**destroy_vpn_item**](docs/ApiApi.md#destroy_vpn_item) | **DELETE** /api/v1/vpn-item/{pkid}/ | 
*ApiApi* | [**destroy_vpn_protocol**](docs/ApiApi.md#destroy_vpn_protocol) | **DELETE** /api/v1/vpn-protocol/{pkid}/ | 
*ApiApi* | [**destroy_vpn_subscription**](docs/ApiApi.md#destroy_vpn_subscription) | **DELETE** /api/v1/vpn-subscription/{pkid}/ | 
*ApiApi* | [**list_bot_users**](docs/ApiApi.md#list_bot_users) | **GET** /api/v1/bot_user/all | 
*ApiApi* | [**list_vpn_countrys**](docs/ApiApi.md#list_vpn_countrys) | **GET** /api/v1/vpn-country/ | 
*ApiApi* | [**list_vpn_device_tariffs**](docs/ApiApi.md#list_vpn_device_tariffs) | **GET** /api/v1/vpn-device-tariff/ | 
*ApiApi* | [**list_vpn_duration_prices**](docs/ApiApi.md#list_vpn_duration_prices) | **GET** /api/v1/vpn-duration-price/ | 
*ApiApi* | [**list_vpn_items**](docs/ApiApi.md#list_vpn_items) | **GET** /api/v1/vpn-item/ | 
*ApiApi* | [**list_vpn_protocols**](docs/ApiApi.md#list_vpn_protocols) | **GET** /api/v1/vpn-protocol/ | 
*ApiApi* | [**list_vpn_subscriptions**](docs/ApiApi.md#list_vpn_subscriptions) | **GET** /api/v1/vpn-subscription/ | 
*ApiApi* | [**partial_update_vpn_country**](docs/ApiApi.md#partial_update_vpn_country) | **PATCH** /api/v1/vpn-country/{pkid}/ | 
*ApiApi* | [**partial_update_vpn_device_tariff**](docs/ApiApi.md#partial_update_vpn_device_tariff) | **PATCH** /api/v1/vpn-device-tariff/{pkid}/ | 
*ApiApi* | [**partial_update_vpn_duration_price**](docs/ApiApi.md#partial_update_vpn_duration_price) | **PATCH** /api/v1/vpn-duration-price/{pkid}/ | 
*ApiApi* | [**partial_update_vpn_item**](docs/ApiApi.md#partial_update_vpn_item) | **PATCH** /api/v1/vpn-item/{pkid}/ | 
*ApiApi* | [**partial_update_vpn_protocol**](docs/ApiApi.md#partial_update_vpn_protocol) | **PATCH** /api/v1/vpn-protocol/{pkid}/ | 
*ApiApi* | [**partial_update_vpn_subscription**](docs/ApiApi.md#partial_update_vpn_subscription) | **PATCH** /api/v1/vpn-subscription/{pkid}/ | 
*ApiApi* | [**retrieve_vpn_country**](docs/ApiApi.md#retrieve_vpn_country) | **GET** /api/v1/vpn-country/{pkid}/ | 
*ApiApi* | [**retrieve_vpn_device_tariff**](docs/ApiApi.md#retrieve_vpn_device_tariff) | **GET** /api/v1/vpn-device-tariff/{pkid}/ | 
*ApiApi* | [**retrieve_vpn_duration_price**](docs/ApiApi.md#retrieve_vpn_duration_price) | **GET** /api/v1/vpn-duration-price/{pkid}/ | 
*ApiApi* | [**retrieve_vpn_item**](docs/ApiApi.md#retrieve_vpn_item) | **GET** /api/v1/vpn-item/{pkid}/ | 
*ApiApi* | [**retrieve_vpn_protocol**](docs/ApiApi.md#retrieve_vpn_protocol) | **GET** /api/v1/vpn-protocol/{pkid}/ | 
*ApiApi* | [**retrieve_vpn_subscription**](docs/ApiApi.md#retrieve_vpn_subscription) | **GET** /api/v1/vpn-subscription/{pkid}/ | 
*ApiApi* | [**update_vpn_country**](docs/ApiApi.md#update_vpn_country) | **PUT** /api/v1/vpn-country/{pkid}/ | 
*ApiApi* | [**update_vpn_device_tariff**](docs/ApiApi.md#update_vpn_device_tariff) | **PUT** /api/v1/vpn-device-tariff/{pkid}/ | 
*ApiApi* | [**update_vpn_duration_price**](docs/ApiApi.md#update_vpn_duration_price) | **PUT** /api/v1/vpn-duration-price/{pkid}/ | 
*ApiApi* | [**update_vpn_item**](docs/ApiApi.md#update_vpn_item) | **PUT** /api/v1/vpn-item/{pkid}/ | 
*ApiApi* | [**update_vpn_protocol**](docs/ApiApi.md#update_vpn_protocol) | **PUT** /api/v1/vpn-protocol/{pkid}/ | 
*ApiApi* | [**update_vpn_subscription**](docs/ApiApi.md#update_vpn_subscription) | **PUT** /api/v1/vpn-subscription/{pkid}/ | 


## Documentation For Models

 - [BotUser](docs/BotUser.md)
 - [TokenObtainPair](docs/TokenObtainPair.md)
 - [TokenRefresh](docs/TokenRefresh.md)
 - [VpnCountry](docs/VpnCountry.md)
 - [VpnDeviceTariff](docs/VpnDeviceTariff.md)
 - [VpnDeviceTariffDurationData](docs/VpnDeviceTariffDurationData.md)
 - [VpnDurationPrice](docs/VpnDurationPrice.md)
 - [VpnItem](docs/VpnItem.md)
 - [VpnItemInstanceData](docs/VpnItemInstanceData.md)
 - [VpnItemInstanceDataCountryData](docs/VpnItemInstanceDataCountryData.md)
 - [VpnItemInstanceDataProtocolsDataInner](docs/VpnItemInstanceDataProtocolsDataInner.md)
 - [VpnItemProtocolData](docs/VpnItemProtocolData.md)
 - [VpnProtocol](docs/VpnProtocol.md)
 - [VpnSubscription](docs/VpnSubscription.md)
 - [VpnSubscriptionTariffData](docs/VpnSubscriptionTariffData.md)
 - [VpnSubscriptionUserData](docs/VpnSubscriptionUserData.md)
 - [VpnSubscriptionVpnItemsInner](docs/VpnSubscriptionVpnItemsInner.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in xkcd_client.apis and xkcd_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from xkcd_client.api.default_api import DefaultApi`
- `from xkcd_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import xkcd_client
from xkcd_client.apis import *
from xkcd_client.models import *
```

