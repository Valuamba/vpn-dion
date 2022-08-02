# xkcd_client.ApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bot_user**](ApiApi.md#create_bot_user) | **POST** /api/v1/bot_user/create | 
[**create_token_obtain_pair**](ApiApi.md#create_token_obtain_pair) | **POST** /api/v1/token/ | 
[**create_token_refresh**](ApiApi.md#create_token_refresh) | **POST** /api/v1/token/refresh/ | 
[**create_vpn_country**](ApiApi.md#create_vpn_country) | **POST** /api/v1/vpn-country/ | 
[**create_vpn_device_tariff**](ApiApi.md#create_vpn_device_tariff) | **POST** /api/v1/vpn-device-tariff/ | 
[**create_vpn_duration_price**](ApiApi.md#create_vpn_duration_price) | **POST** /api/v1/vpn-duration-price/ | 
[**create_vpn_item**](ApiApi.md#create_vpn_item) | **POST** /api/v1/vpn-item/ | 
[**create_vpn_protocol**](ApiApi.md#create_vpn_protocol) | **POST** /api/v1/vpn-protocol/ | 
[**create_vpn_subscription**](ApiApi.md#create_vpn_subscription) | **POST** /api/v1/vpn-subscription/ | 
[**destroy_vpn_country**](ApiApi.md#destroy_vpn_country) | **DELETE** /api/v1/vpn-country/{pkid}/ | 
[**destroy_vpn_device_tariff**](ApiApi.md#destroy_vpn_device_tariff) | **DELETE** /api/v1/vpn-device-tariff/{pkid}/ | 
[**destroy_vpn_duration_price**](ApiApi.md#destroy_vpn_duration_price) | **DELETE** /api/v1/vpn-duration-price/{pkid}/ | 
[**destroy_vpn_item**](ApiApi.md#destroy_vpn_item) | **DELETE** /api/v1/vpn-item/{pkid}/ | 
[**destroy_vpn_protocol**](ApiApi.md#destroy_vpn_protocol) | **DELETE** /api/v1/vpn-protocol/{pkid}/ | 
[**destroy_vpn_subscription**](ApiApi.md#destroy_vpn_subscription) | **DELETE** /api/v1/vpn-subscription/{pkid}/ | 
[**list_bot_users**](ApiApi.md#list_bot_users) | **GET** /api/v1/bot_user/all | 
[**list_vpn_countrys**](ApiApi.md#list_vpn_countrys) | **GET** /api/v1/vpn-country/ | 
[**list_vpn_device_tariffs**](ApiApi.md#list_vpn_device_tariffs) | **GET** /api/v1/vpn-device-tariff/ | 
[**list_vpn_duration_prices**](ApiApi.md#list_vpn_duration_prices) | **GET** /api/v1/vpn-duration-price/ | 
[**list_vpn_items**](ApiApi.md#list_vpn_items) | **GET** /api/v1/vpn-item/ | 
[**list_vpn_protocols**](ApiApi.md#list_vpn_protocols) | **GET** /api/v1/vpn-protocol/ | 
[**list_vpn_subscriptions**](ApiApi.md#list_vpn_subscriptions) | **GET** /api/v1/vpn-subscription/ | 
[**partial_update_vpn_country**](ApiApi.md#partial_update_vpn_country) | **PATCH** /api/v1/vpn-country/{pkid}/ | 
[**partial_update_vpn_device_tariff**](ApiApi.md#partial_update_vpn_device_tariff) | **PATCH** /api/v1/vpn-device-tariff/{pkid}/ | 
[**partial_update_vpn_duration_price**](ApiApi.md#partial_update_vpn_duration_price) | **PATCH** /api/v1/vpn-duration-price/{pkid}/ | 
[**partial_update_vpn_item**](ApiApi.md#partial_update_vpn_item) | **PATCH** /api/v1/vpn-item/{pkid}/ | 
[**partial_update_vpn_protocol**](ApiApi.md#partial_update_vpn_protocol) | **PATCH** /api/v1/vpn-protocol/{pkid}/ | 
[**partial_update_vpn_subscription**](ApiApi.md#partial_update_vpn_subscription) | **PATCH** /api/v1/vpn-subscription/{pkid}/ | 
[**retrieve_vpn_country**](ApiApi.md#retrieve_vpn_country) | **GET** /api/v1/vpn-country/{pkid}/ | 
[**retrieve_vpn_device_tariff**](ApiApi.md#retrieve_vpn_device_tariff) | **GET** /api/v1/vpn-device-tariff/{pkid}/ | 
[**retrieve_vpn_duration_price**](ApiApi.md#retrieve_vpn_duration_price) | **GET** /api/v1/vpn-duration-price/{pkid}/ | 
[**retrieve_vpn_item**](ApiApi.md#retrieve_vpn_item) | **GET** /api/v1/vpn-item/{pkid}/ | 
[**retrieve_vpn_protocol**](ApiApi.md#retrieve_vpn_protocol) | **GET** /api/v1/vpn-protocol/{pkid}/ | 
[**retrieve_vpn_subscription**](ApiApi.md#retrieve_vpn_subscription) | **GET** /api/v1/vpn-subscription/{pkid}/ | 
[**update_vpn_country**](ApiApi.md#update_vpn_country) | **PUT** /api/v1/vpn-country/{pkid}/ | 
[**update_vpn_device_tariff**](ApiApi.md#update_vpn_device_tariff) | **PUT** /api/v1/vpn-device-tariff/{pkid}/ | 
[**update_vpn_duration_price**](ApiApi.md#update_vpn_duration_price) | **PUT** /api/v1/vpn-duration-price/{pkid}/ | 
[**update_vpn_item**](ApiApi.md#update_vpn_item) | **PUT** /api/v1/vpn-item/{pkid}/ | 
[**update_vpn_protocol**](ApiApi.md#update_vpn_protocol) | **PUT** /api/v1/vpn-protocol/{pkid}/ | 
[**update_vpn_subscription**](ApiApi.md#update_vpn_subscription) | **PUT** /api/v1/vpn-subscription/{pkid}/ | 


# **create_bot_user**
> BotUser create_bot_user()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.bot_user import BotUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    bot_user = BotUser(
        user_id=-9223372036854775808,
        user_name="user_name_example",
        first_name="first_name_example",
        last_name="last_name_example",
        is_bot_blocked=True,
    ) # BotUser |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_bot_user(bot_user=bot_user)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_bot_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_user** | [**BotUser**](BotUser.md)|  | [optional]

### Return type

[**BotUser**](BotUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token_obtain_pair**
> TokenObtainPair create_token_obtain_pair()



Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.token_obtain_pair import TokenObtainPair
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    token_obtain_pair = TokenObtainPair(
        username="username_example",
        password="password_example",
    ) # TokenObtainPair |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_token_obtain_pair(token_obtain_pair=token_obtain_pair)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_token_obtain_pair: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_obtain_pair** | [**TokenObtainPair**](TokenObtainPair.md)|  | [optional]

### Return type

[**TokenObtainPair**](TokenObtainPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token_refresh**
> TokenRefresh create_token_refresh()



Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.token_refresh import TokenRefresh
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    token_refresh = TokenRefresh(
        refresh="refresh_example",
    ) # TokenRefresh |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_token_refresh(token_refresh=token_refresh)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_token_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_refresh** | [**TokenRefresh**](TokenRefresh.md)|  | [optional]

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_country**
> VpnCountry create_vpn_country()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_country import VpnCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    vpn_country = VpnCountry(
        discount_percentage=0,
    ) # VpnCountry |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vpn_country(vpn_country=vpn_country)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_vpn_country: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_country** | [**VpnCountry**](VpnCountry.md)|  | [optional]

### Return type

[**VpnCountry**](VpnCountry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_device_tariff**
> VpnDeviceTariff create_vpn_device_tariff()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_device_tariff import VpnDeviceTariff
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    vpn_device_tariff = VpnDeviceTariff(
        duration=1,
        devices_number=1,
        operation="equal",
        discount_percentage=0,
        result_price="result_price_example",
    ) # VpnDeviceTariff |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vpn_device_tariff(vpn_device_tariff=vpn_device_tariff)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_vpn_device_tariff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_device_tariff** | [**VpnDeviceTariff**](VpnDeviceTariff.md)|  | [optional]

### Return type

[**VpnDeviceTariff**](VpnDeviceTariff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_duration_price**
> VpnDurationPrice create_vpn_duration_price()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_duration_price import VpnDurationPrice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    vpn_duration_price = VpnDurationPrice(
        month_duration=1,
        currency="currency_example",
        amount="amount_example",
    ) # VpnDurationPrice |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vpn_duration_price(vpn_duration_price=vpn_duration_price)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_vpn_duration_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_duration_price** | [**VpnDurationPrice**](VpnDurationPrice.md)|  | [optional]

### Return type

[**VpnDurationPrice**](VpnDurationPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_item**
> VpnItem create_vpn_item()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_item import VpnItem
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    vpn_item = VpnItem(
        instance=1,
        protocol=1,
        public_key="public_key_example",
        private_key="private_key_example",
        address="address_example",
        dns="dns_example",
        preshared_key="preshared_key_example",
        endpoint="endpoint_example",
        allowed_ips="allowed_ips_example",
        config_name="config_name_example",
    ) # VpnItem |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vpn_item(vpn_item=vpn_item)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_vpn_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_item** | [**VpnItem**](VpnItem.md)|  | [optional]

### Return type

[**VpnItem**](VpnItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_protocol**
> VpnProtocol create_vpn_protocol()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_protocol import VpnProtocol
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    vpn_protocol = VpnProtocol(
        protocol="wireguard",
    ) # VpnProtocol |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vpn_protocol(vpn_protocol=vpn_protocol)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_vpn_protocol: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_protocol** | [**VpnProtocol**](VpnProtocol.md)|  | [optional]

### Return type

[**VpnProtocol**](VpnProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_subscription**
> VpnSubscription create_vpn_subscription()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_subscription import VpnSubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    vpn_subscription = VpnSubscription(
        user=1,
        tariff=1,
        total_price="total_price_example",
        discount="discount_example",
        status=1,
        vpn_items=[
            VpnSubscriptionVpnItemsInner(
                protocol=1,
                instance=1,
            ),
        ],
    ) # VpnSubscription |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vpn_subscription(vpn_subscription=vpn_subscription)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->create_vpn_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_subscription** | [**VpnSubscription**](VpnSubscription.md)|  | [optional]

### Return type

[**VpnSubscription**](VpnSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vpn_country**
> destroy_vpn_country(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn country.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_vpn_country(pkid)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->destroy_vpn_country: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn country. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vpn_device_tariff**
> destroy_vpn_device_tariff(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn device tariff.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_vpn_device_tariff(pkid)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->destroy_vpn_device_tariff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn device tariff. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vpn_duration_price**
> destroy_vpn_duration_price(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn duration price.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_vpn_duration_price(pkid)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->destroy_vpn_duration_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn duration price. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vpn_item**
> destroy_vpn_item(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn item.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_vpn_item(pkid)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->destroy_vpn_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn item. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vpn_protocol**
> destroy_vpn_protocol(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn protocol.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_vpn_protocol(pkid)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->destroy_vpn_protocol: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn protocol. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_vpn_subscription**
> destroy_vpn_subscription(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn subscription.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_vpn_subscription(pkid)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->destroy_vpn_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn subscription. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bot_users**
> [BotUser] list_bot_users()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.bot_user import BotUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_bot_users()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_bot_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[BotUser]**](BotUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vpn_countrys**
> [VpnCountry] list_vpn_countrys()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_country import VpnCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vpn_countrys()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_vpn_countrys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[VpnCountry]**](VpnCountry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vpn_device_tariffs**
> [VpnDeviceTariff] list_vpn_device_tariffs()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_device_tariff import VpnDeviceTariff
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vpn_device_tariffs()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_vpn_device_tariffs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[VpnDeviceTariff]**](VpnDeviceTariff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vpn_duration_prices**
> [VpnDurationPrice] list_vpn_duration_prices()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_duration_price import VpnDurationPrice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vpn_duration_prices()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_vpn_duration_prices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[VpnDurationPrice]**](VpnDurationPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vpn_items**
> [VpnItem] list_vpn_items()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_item import VpnItem
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vpn_items()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_vpn_items: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[VpnItem]**](VpnItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vpn_protocols**
> [VpnProtocol] list_vpn_protocols()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_protocol import VpnProtocol
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vpn_protocols()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_vpn_protocols: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[VpnProtocol]**](VpnProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vpn_subscriptions**
> [VpnSubscription] list_vpn_subscriptions()





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_subscription import VpnSubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vpn_subscriptions()
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->list_vpn_subscriptions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[VpnSubscription]**](VpnSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_vpn_country**
> VpnCountry partial_update_vpn_country(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_country import VpnCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn country.
    vpn_country = VpnCountry(
        discount_percentage=0,
    ) # VpnCountry |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_vpn_country(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_country: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_vpn_country(pkid, vpn_country=vpn_country)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_country: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn country. |
 **vpn_country** | [**VpnCountry**](VpnCountry.md)|  | [optional]

### Return type

[**VpnCountry**](VpnCountry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_vpn_device_tariff**
> VpnDeviceTariff partial_update_vpn_device_tariff(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_device_tariff import VpnDeviceTariff
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn device tariff.
    vpn_device_tariff = VpnDeviceTariff(
        duration=1,
        devices_number=1,
        operation="equal",
        discount_percentage=0,
        result_price="result_price_example",
    ) # VpnDeviceTariff |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_vpn_device_tariff(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_device_tariff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_vpn_device_tariff(pkid, vpn_device_tariff=vpn_device_tariff)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_device_tariff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn device tariff. |
 **vpn_device_tariff** | [**VpnDeviceTariff**](VpnDeviceTariff.md)|  | [optional]

### Return type

[**VpnDeviceTariff**](VpnDeviceTariff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_vpn_duration_price**
> VpnDurationPrice partial_update_vpn_duration_price(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_duration_price import VpnDurationPrice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn duration price.
    vpn_duration_price = VpnDurationPrice(
        month_duration=1,
        currency="currency_example",
        amount="amount_example",
    ) # VpnDurationPrice |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_vpn_duration_price(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_duration_price: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_vpn_duration_price(pkid, vpn_duration_price=vpn_duration_price)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_duration_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn duration price. |
 **vpn_duration_price** | [**VpnDurationPrice**](VpnDurationPrice.md)|  | [optional]

### Return type

[**VpnDurationPrice**](VpnDurationPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_vpn_item**
> VpnItem partial_update_vpn_item(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_item import VpnItem
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn item.
    vpn_item = VpnItem(
        instance=1,
        protocol=1,
        public_key="public_key_example",
        private_key="private_key_example",
        address="address_example",
        dns="dns_example",
        preshared_key="preshared_key_example",
        endpoint="endpoint_example",
        allowed_ips="allowed_ips_example",
        config_name="config_name_example",
    ) # VpnItem |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_vpn_item(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_vpn_item(pkid, vpn_item=vpn_item)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn item. |
 **vpn_item** | [**VpnItem**](VpnItem.md)|  | [optional]

### Return type

[**VpnItem**](VpnItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_vpn_protocol**
> VpnProtocol partial_update_vpn_protocol(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_protocol import VpnProtocol
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn protocol.
    vpn_protocol = VpnProtocol(
        protocol="wireguard",
    ) # VpnProtocol |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_vpn_protocol(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_protocol: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_vpn_protocol(pkid, vpn_protocol=vpn_protocol)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_protocol: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn protocol. |
 **vpn_protocol** | [**VpnProtocol**](VpnProtocol.md)|  | [optional]

### Return type

[**VpnProtocol**](VpnProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_vpn_subscription**
> VpnSubscription partial_update_vpn_subscription(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_subscription import VpnSubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn subscription.
    vpn_subscription = VpnSubscription(
        user=1,
        tariff=1,
        total_price="total_price_example",
        discount="discount_example",
        status=1,
        vpn_items=[
            VpnSubscriptionVpnItemsInner(
                protocol=1,
                instance=1,
            ),
        ],
    ) # VpnSubscription |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_vpn_subscription(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_vpn_subscription(pkid, vpn_subscription=vpn_subscription)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->partial_update_vpn_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn subscription. |
 **vpn_subscription** | [**VpnSubscription**](VpnSubscription.md)|  | [optional]

### Return type

[**VpnSubscription**](VpnSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vpn_country**
> VpnCountry retrieve_vpn_country(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_country import VpnCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn country.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_vpn_country(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->retrieve_vpn_country: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn country. |

### Return type

[**VpnCountry**](VpnCountry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vpn_device_tariff**
> VpnDeviceTariff retrieve_vpn_device_tariff(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_device_tariff import VpnDeviceTariff
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn device tariff.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_vpn_device_tariff(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->retrieve_vpn_device_tariff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn device tariff. |

### Return type

[**VpnDeviceTariff**](VpnDeviceTariff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vpn_duration_price**
> VpnDurationPrice retrieve_vpn_duration_price(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_duration_price import VpnDurationPrice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn duration price.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_vpn_duration_price(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->retrieve_vpn_duration_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn duration price. |

### Return type

[**VpnDurationPrice**](VpnDurationPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vpn_item**
> VpnItem retrieve_vpn_item(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_item import VpnItem
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn item.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_vpn_item(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->retrieve_vpn_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn item. |

### Return type

[**VpnItem**](VpnItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vpn_protocol**
> VpnProtocol retrieve_vpn_protocol(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_protocol import VpnProtocol
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn protocol.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_vpn_protocol(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->retrieve_vpn_protocol: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn protocol. |

### Return type

[**VpnProtocol**](VpnProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vpn_subscription**
> VpnSubscription retrieve_vpn_subscription(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_subscription import VpnSubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn subscription.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_vpn_subscription(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->retrieve_vpn_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn subscription. |

### Return type

[**VpnSubscription**](VpnSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_country**
> VpnCountry update_vpn_country(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_country import VpnCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn country.
    vpn_country = VpnCountry(
        discount_percentage=0,
    ) # VpnCountry |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_vpn_country(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_country: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_vpn_country(pkid, vpn_country=vpn_country)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_country: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn country. |
 **vpn_country** | [**VpnCountry**](VpnCountry.md)|  | [optional]

### Return type

[**VpnCountry**](VpnCountry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_device_tariff**
> VpnDeviceTariff update_vpn_device_tariff(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_device_tariff import VpnDeviceTariff
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn device tariff.
    vpn_device_tariff = VpnDeviceTariff(
        duration=1,
        devices_number=1,
        operation="equal",
        discount_percentage=0,
        result_price="result_price_example",
    ) # VpnDeviceTariff |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_vpn_device_tariff(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_device_tariff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_vpn_device_tariff(pkid, vpn_device_tariff=vpn_device_tariff)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_device_tariff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn device tariff. |
 **vpn_device_tariff** | [**VpnDeviceTariff**](VpnDeviceTariff.md)|  | [optional]

### Return type

[**VpnDeviceTariff**](VpnDeviceTariff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_duration_price**
> VpnDurationPrice update_vpn_duration_price(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_duration_price import VpnDurationPrice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this Vpn duration price.
    vpn_duration_price = VpnDurationPrice(
        month_duration=1,
        currency="currency_example",
        amount="amount_example",
    ) # VpnDurationPrice |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_vpn_duration_price(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_duration_price: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_vpn_duration_price(pkid, vpn_duration_price=vpn_duration_price)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_duration_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this Vpn duration price. |
 **vpn_duration_price** | [**VpnDurationPrice**](VpnDurationPrice.md)|  | [optional]

### Return type

[**VpnDurationPrice**](VpnDurationPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_item**
> VpnItem update_vpn_item(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_item import VpnItem
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn item.
    vpn_item = VpnItem(
        instance=1,
        protocol=1,
        public_key="public_key_example",
        private_key="private_key_example",
        address="address_example",
        dns="dns_example",
        preshared_key="preshared_key_example",
        endpoint="endpoint_example",
        allowed_ips="allowed_ips_example",
        config_name="config_name_example",
    ) # VpnItem |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_vpn_item(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_vpn_item(pkid, vpn_item=vpn_item)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn item. |
 **vpn_item** | [**VpnItem**](VpnItem.md)|  | [optional]

### Return type

[**VpnItem**](VpnItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_protocol**
> VpnProtocol update_vpn_protocol(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_protocol import VpnProtocol
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn protocol.
    vpn_protocol = VpnProtocol(
        protocol="wireguard",
    ) # VpnProtocol |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_vpn_protocol(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_protocol: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_vpn_protocol(pkid, vpn_protocol=vpn_protocol)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_protocol: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn protocol. |
 **vpn_protocol** | [**VpnProtocol**](VpnProtocol.md)|  | [optional]

### Return type

[**VpnProtocol**](VpnProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_subscription**
> VpnSubscription update_vpn_subscription(pkid)





### Example


```python
import time
import xkcd_client
from xkcd_client.api import api_api
from xkcd_client.model.vpn_subscription import VpnSubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xkcd_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xkcd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    pkid = "pkid_example" # str | A unique integer value identifying this vpn subscription.
    vpn_subscription = VpnSubscription(
        user=1,
        tariff=1,
        total_price="total_price_example",
        discount="discount_example",
        status=1,
        vpn_items=[
            VpnSubscriptionVpnItemsInner(
                protocol=1,
                instance=1,
            ),
        ],
    ) # VpnSubscription |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_vpn_subscription(pkid)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_vpn_subscription(pkid, vpn_subscription=vpn_subscription)
        pprint(api_response)
    except xkcd_client.ApiException as e:
        print("Exception when calling ApiApi->update_vpn_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkid** | **str**| A unique integer value identifying this vpn subscription. |
 **vpn_subscription** | [**VpnSubscription**](VpnSubscription.md)|  | [optional]

### Return type

[**VpnSubscription**](VpnSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

