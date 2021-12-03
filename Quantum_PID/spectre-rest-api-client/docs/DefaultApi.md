# spectre_api_client.DefaultApi

All URIs are relative to *https://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_command**](DefaultApi.md#add_command) | **POST** /commands | Create new command
[**add_data**](DefaultApi.md#add_data) | **POST** /data | Add new datapoints
[**add_device**](DefaultApi.md#add_device) | **POST** /devices | Create new device
[**add_firmware**](DefaultApi.md#add_firmware) | **POST** /firmware | Add new firmware.
[**add_mission**](DefaultApi.md#add_mission) | **POST** /missions | Add new mission
[**add_spy**](DefaultApi.md#add_spy) | **POST** /spies | Create new spy
[**add_textile**](DefaultApi.md#add_textile) | **POST** /textiles | Create new textile
[**delete_command**](DefaultApi.md#delete_command) | **DELETE** /commands/{id} | Delete command
[**delete_device**](DefaultApi.md#delete_device) | **DELETE** /devices/{id} | Delete device
[**delete_firmware**](DefaultApi.md#delete_firmware) | **DELETE** /firmware/{id} | Delete firmware
[**delete_mission**](DefaultApi.md#delete_mission) | **DELETE** /missions/{id} | Delete mission
[**delete_spy**](DefaultApi.md#delete_spy) | **DELETE** /spies/{id} | Delete spy
[**delete_textile**](DefaultApi.md#delete_textile) | **DELETE** /textiles/{id} | Delete textile
[**get_command_by_id**](DefaultApi.md#get_command_by_id) | **GET** /commands/{id} | Get command by id
[**get_commands**](DefaultApi.md#get_commands) | **GET** /commands | Get commands
[**get_commands_from_mission**](DefaultApi.md#get_commands_from_mission) | **GET** /missions/{id}/commands | Get commands of a mission
[**get_dashboard_data_from_mission**](DefaultApi.md#get_dashboard_data_from_mission) | **GET** /missions/{id}/dashboardData | Get dashboard data of a mission
[**get_dashboard_from_mission**](DefaultApi.md#get_dashboard_from_mission) | **GET** /missions/{id}/dashboard | Get dashboard of a mission
[**get_data**](DefaultApi.md#get_data) | **GET** /data | Get data from influxDB
[**get_dataseries_by_id**](DefaultApi.md#get_dataseries_by_id) | **GET** /dataseries/{id} | Get data from influxDB
[**get_dataseries_from_mission**](DefaultApi.md#get_dataseries_from_mission) | **GET** /missions/{id}/dataseries | Get dataseries of a mission
[**get_device_by_id**](DefaultApi.md#get_device_by_id) | **GET** /devices/{id} | Get devices
[**get_devices**](DefaultApi.md#get_devices) | **GET** /devices | Get devices
[**get_firmware_by_id**](DefaultApi.md#get_firmware_by_id) | **GET** /firmware/{id} | Get information about a specific firmware
[**get_firmware_from_mission**](DefaultApi.md#get_firmware_from_mission) | **GET** /missions/{id}/firmware | Get firmware of a mission
[**get_firmware_list**](DefaultApi.md#get_firmware_list) | **GET** /firmware | Get available firmware versions
[**get_missions**](DefaultApi.md#get_missions) | **GET** /missions | Get missions
[**get_missions_by_id**](DefaultApi.md#get_missions_by_id) | **GET** /missions/{id} | Get missions with a specific ID
[**get_next_pending_mission**](DefaultApi.md#get_next_pending_mission) | **GET** /spies/{id}/nextMission | Get next pending mission for a spy
[**get_spies**](DefaultApi.md#get_spies) | **GET** /spies | Get all spies
[**get_spy**](DefaultApi.md#get_spy) | **GET** /spy | Get spy
[**get_spy_by_id**](DefaultApi.md#get_spy_by_id) | **GET** /spies/{id} | Get a specific spy
[**get_spy_from_mission**](DefaultApi.md#get_spy_from_mission) | **GET** /missions/{id}/spy | Get spy of a mission
[**get_textile_by_id**](DefaultApi.md#get_textile_by_id) | **GET** /textiles/{id} | Get a specific textile
[**get_textile_from_mission**](DefaultApi.md#get_textile_from_mission) | **GET** /missions/{id}/textile | Get textile of a mission
[**get_textiles**](DefaultApi.md#get_textiles) | **GET** /textiles | Get all textiles
[**get_version**](DefaultApi.md#get_version) | **GET** /version | Returns the API version
[**update_command**](DefaultApi.md#update_command) | **PUT** /commands/{id} | Update command
[**update_device**](DefaultApi.md#update_device) | **PUT** /devices/{id} | Update device
[**update_firmware**](DefaultApi.md#update_firmware) | **PUT** /firmware/{id} | Update firmware
[**update_mission**](DefaultApi.md#update_mission) | **PUT** /missions/{id} | Update mission
[**update_spy**](DefaultApi.md#update_spy) | **PUT** /spies/{id} | Update spy
[**update_textile**](DefaultApi.md#update_textile) | **PUT** /textiles/{id} | Update textile


# **add_command**
> IdObj add_command(command)

Create new command

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.command import Command
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    command = Command(
        id=1,
        text_command="text_command_example",
        delay_ms=1,
        device=1,
        mission=1,
    ) # Command | 

    # example passing only required values which don't have defaults set
    try:
        # Create new command
        api_response = api_instance.add_command(command)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**Command**](Command.md)|  |

### Return type

[**IdObj**](IdObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added new spy |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not create spy - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_data**
> add_data(data_point_list)

Add new datapoints

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.data_point_list import DataPointList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    data_point_list = DataPointList(
        data_points=[
            DataPoint(
                timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                vin=3.14,
                vout=3.14,
                frequency=3.14,
                phase=3.14,
                converted=3.14,
                reserved1=3.14,
                reserved2=3.14,
                data_series_id=1,
            ),
        ],
    ) # DataPointList | DataSeries, which should be added. If a the ID of the DataSeries is passed with the object, the data is added to the series. Otherwise a new series is created. 

    # example passing only required values which don't have defaults set
    try:
        # Add new datapoints
        api_instance.add_data(data_point_list)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_list** | [**DataPointList**](DataPointList.md)| DataSeries, which should be added. If a the ID of the DataSeries is passed with the object, the data is added to the series. Otherwise a new series is created.  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added new data |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not add new data - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device**
> IdObj add_device(device)

Create new device

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.device import Device
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    device = Device(
        id=1,
        name="name_example",
        type="type_example",
        mac_address="mac_address_example",
        port=1,
        spy=1,
    ) # Device | 

    # example passing only required values which don't have defaults set
    try:
        # Create new device
        api_response = api_instance.add_device(device)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)|  |

### Return type

[**IdObj**](IdObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added new device |  -  |
**400** | Insufficient data or invalid values |  -  |
**500** | Could not create spy - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_firmware**
> IdObj add_firmware(firmware)

Add new firmware.

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.firmware import Firmware
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    firmware = Firmware(
        id=1,
        name="name_example",
        version=1,
        url="url_example",
        md5="md5_example",
    ) # Firmware | New firmware

    # example passing only required values which don't have defaults set
    try:
        # Add new firmware.
        api_response = api_instance.add_firmware(firmware)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_firmware: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firmware** | [**Firmware**](Firmware.md)| New firmware |

### Return type

[**IdObj**](IdObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added a new firmware |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not create firmware - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mission**
> IdObj add_mission(mission)

Add new mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.mission import Mission
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mission = Mission(
        id=1,
        name="name_example",
        description="description_example",
        scheduled=dateutil_parser('1970-01-01T00:00:00.00Z'),
        dashboard_url="dashboard_url_example",
        live=True,
        status="Pending",
        spy=1,
        firmware=1,
        dataseries=1,
        user=1,
        textile=1,
    ) # Mission | Mission to create

    # example passing only required values which don't have defaults set
    try:
        # Add new mission
        api_response = api_instance.add_mission(mission)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission** | [**Mission**](Mission.md)| Mission to create |

### Return type

[**IdObj**](IdObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added a new mission |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not create mission - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_spy**
> IdObj add_spy(spy)

Create new spy

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    spy = Spy() # Spy | 

    # example passing only required values which don't have defaults set
    try:
        # Create new spy
        api_response = api_instance.add_spy(spy)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_spy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spy** | [**Spy**](Spy.md)|  |

### Return type

[**IdObj**](IdObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added new spy |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not create spy - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_textile**
> IdObj add_textile(textile)

Create new textile

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.textile import Textile
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    textile = Textile(
        id=1,
        name="name_example",
        length=1,
        width=1,
        height=1,
        material="material_example",
        titer=1,
        gsm=1,
        warp=1,
        weft=1,
        binding="binding_example",
        conductivity="conductivity_example",
        metadata="metadata_example",
        manufacturer="manufacturer_example",
    ) # Textile | 

    # example passing only required values which don't have defaults set
    try:
        # Create new textile
        api_response = api_instance.add_textile(textile)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_textile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textile** | [**Textile**](Textile.md)|  |

### Return type

[**IdObj**](IdObj.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added new textile |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not create textile - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_command**
> delete_command()

Delete command

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete command
        api_instance.delete_command()
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted command |  -  |
**400** | Command does not exist |  -  |
**500** | Could not delete command - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device()

Delete device

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete device
        api_instance.delete_device()
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted device |  -  |
**400** | Device does not exist |  -  |
**500** | Could not delete device - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firmware**
> delete_firmware()

Delete firmware

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete firmware
        api_instance.delete_firmware()
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_firmware: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted firmware |  -  |
**400** | Firmware does not exist |  -  |
**500** | Could not delete firmware - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mission**
> delete_mission()

Delete mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete mission
        api_instance.delete_mission()
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted mission |  -  |
**400** | Mission does not exist |  -  |
**500** | Could not delete mission - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_spy**
> delete_spy()

Delete spy

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete spy
        api_instance.delete_spy()
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_spy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted spy |  -  |
**400** | Spy does not exist |  -  |
**500** | Could not delete Spy - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_textile**
> delete_textile()

Delete textile

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete textile
        api_instance.delete_textile()
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_textile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted textile |  -  |
**400** | Textile does not exist |  -  |
**500** | Could not delete Textile - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_by_id**
> Command get_command_by_id()

Get command by id

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.command import Command
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get command by id
        api_response = api_instance.get_command_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_command_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Command**](Command.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested command |  -  |
**400** | Command not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands**
> CommandList get_commands()

Get commands

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.command_list import CommandList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mission = 1 # int | ID of the appropriate mission (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get commands
        api_response = api_instance.get_commands(mission=mission)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_commands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission** | **int**| ID of the appropriate mission | [optional]

### Return type

[**CommandList**](CommandList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested commands |  -  |
**400** | Invalid mission ID |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands_from_mission**
> CommandList get_commands_from_mission()

Get commands of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.command_list import CommandList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get commands of a mission
        api_response = api_instance.get_commands_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_commands_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**CommandList**](CommandList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the requested dataseries |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_data_from_mission**
> str get_dashboard_data_from_mission()

Get dashboard data of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get dashboard data of a mission
        api_response = api_instance.get_dashboard_data_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_dashboard_data_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested dashboard data |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_from_mission**
> Url get_dashboard_from_mission()

Get dashboard of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.url import Url
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get dashboard of a mission
        api_response = api_instance.get_dashboard_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_dashboard_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Url**](Url.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested dashboard |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data**
> DataSeries get_data(_from, to)

Get data from influxDB

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.data_series import DataSeries
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    _from = "from_example" # str | Start date of the data points to return
    to = "to_example" # str | End date of the data points to return

    # example passing only required values which don't have defaults set
    try:
        # Get data from influxDB
        api_response = api_instance.get_data(_from, to)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Start date of the data points to return |
 **to** | **str**| End date of the data points to return |

### Return type

[**DataSeries**](DataSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retruns the requested data points |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataseries_by_id**
> DataSeries get_dataseries_by_id()

Get data from influxDB

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.data_series import DataSeries
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get data from influxDB
        api_response = api_instance.get_dataseries_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_dataseries_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**DataSeries**](DataSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retruns the requested data points |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataseries_from_mission**
> DataSeries get_dataseries_from_mission()

Get dataseries of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.data_series import DataSeries
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get dataseries of a mission
        api_response = api_instance.get_dataseries_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_dataseries_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**DataSeries**](DataSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the requested dataseries |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> Device get_device_by_id()

Get devices

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.device import Device
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get devices
        api_response = api_instance.get_device_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested device |  -  |
**404** | Device not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> DeviceList get_devices()

Get devices

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.device_list import DeviceList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    spy = 1 # int | ID of the appropriate mission (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get devices
        api_response = api_instance.get_devices(spy=spy)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spy** | **int**| ID of the appropriate mission | [optional]

### Return type

[**DeviceList**](DeviceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested commands |  -  |
**400** | Invalid device ID |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_by_id**
> Firmware get_firmware_by_id()

Get information about a specific firmware

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.firmware import Firmware
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get information about a specific firmware
        api_response = api_instance.get_firmware_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_firmware_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Firmware**](Firmware.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested firmware |  -  |
**404** | Firmware not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_from_mission**
> Firmware get_firmware_from_mission()

Get firmware of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.firmware import Firmware
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get firmware of a mission
        api_response = api_instance.get_firmware_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_firmware_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Firmware**](Firmware.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested firmware |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_list**
> FirmwareList get_firmware_list()

Get available firmware versions

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.firmware_list import FirmwareList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get available firmware versions
        api_response = api_instance.get_firmware_list()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_firmware_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FirmwareList**](FirmwareList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of available firmware versions |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_missions**
> MissionList get_missions()

Get missions

By default this returns all missions. A parameter can be used to filter messages from a specific spy. 

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.mission_list import MissionList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    spy = 1 # int | ID of the spy to filter (optional)
    status = "status_example" # str | Status of the missions (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get missions
        api_response = api_instance.get_missions(spy=spy, status=status)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_missions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spy** | **int**| ID of the spy to filter | [optional]
 **status** | **str**| Status of the missions | [optional]

### Return type

[**MissionList**](MissionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of requested missions |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_missions_by_id**
> Mission get_missions_by_id()

Get missions with a specific ID

This endpoint returns the mission with the specified ID 

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.mission import Mission
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get missions with a specific ID
        api_response = api_instance.get_missions_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_missions_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Mission**](Mission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested mission |  -  |
**404** | Mission not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_pending_mission**
> Mission get_next_pending_mission()

Get next pending mission for a spy

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.mission import Mission
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get next pending mission for a spy
        api_response = api_instance.get_next_pending_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_next_pending_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Mission**](Mission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the next pending mission |  -  |
**204** | No pending mission available |  -  |
**404** | Spy not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spies**
> SpyList get_spies()

Get all spies

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy_list import SpyList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    name = "name_example" # str | Name of the spy (optional)
    mac = "f3:25:37:5e:03:0f" # str | Mac address of the spy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all spies
        api_response = api_instance.get_spies(name=name, mac=mac)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_spies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the spy | [optional]
 **mac** | **str**| Mac address of the spy | [optional]

### Return type

[**SpyList**](SpyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of all spies |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spy**
> Spy get_spy()

Get spy

Enpoint is used to get on specific spy. It returns successfully only if exactly one spy is fetched from the database. 

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    name = "name_example" # str | Name of the spy (optional)
    mac = "f3:25:37:5e:03:0f" # str | Mac address of the spy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get spy
        api_response = api_instance.get_spy(name=name, mac=mac)
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_spy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the spy | [optional]
 **mac** | **str**| Mac address of the spy | [optional]

### Return type

[**Spy**](Spy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested spy |  -  |
**400** | Request is ambiguous |  -  |
**404** | Spy not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spy_by_id**
> Spy get_spy_by_id()

Get a specific spy

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get a specific spy
        api_response = api_instance.get_spy_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_spy_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Spy**](Spy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested spy |  -  |
**404** | Spy not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spy_from_mission**
> Spy get_spy_from_mission()

Get spy of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get spy of a mission
        api_response = api_instance.get_spy_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_spy_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Spy**](Spy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the requested spy |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_textile_by_id**
> Textile get_textile_by_id()

Get a specific textile

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.textile import Textile
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get a specific textile
        api_response = api_instance.get_textile_by_id()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_textile_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Textile**](Textile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested textile |  -  |
**404** | Textile not found |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_textile_from_mission**
> Textile get_textile_from_mission()

Get textile of a mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.textile import Textile
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get textile of a mission
        api_response = api_instance.get_textile_from_mission()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_textile_from_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | defaults to 0

### Return type

[**Textile**](Textile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested textile |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_textiles**
> TextileList get_textiles()

Get all textiles

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.textile_list import TextileList
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all textiles
        api_response = api_instance.get_textiles()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_textiles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TextileList**](TextileList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of all textiles |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> Versions get_version()

Returns the API version

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.versions import Versions
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the API version
        api_response = api_instance.get_version()
        pprint(api_response)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->get_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Versions**](Versions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the current API version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_command**
> update_command(command)

Update command

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.command import Command
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    command = Command(
        id=1,
        text_command="text_command_example",
        delay_ms=1,
        device=1,
        mission=1,
    ) # Command | 

    # example passing only required values which don't have defaults set
    try:
        # Update command
        api_instance.update_command(command)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->update_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**Command**](Command.md)|  |
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated command |  -  |
**400** | Command not found, insufficient data or not allowed values  |  -  |
**500** | Could not update command - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> update_device(device)

Update device

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.device import Device
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    device = Device(
        id=1,
        name="name_example",
        type="type_example",
        mac_address="mac_address_example",
        port=1,
        spy=1,
    ) # Device | 

    # example passing only required values which don't have defaults set
    try:
        # Update device
        api_instance.update_device(device)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->update_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)|  |
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated device |  -  |
**400** | Device not found, insufficient data or not allowed values  |  -  |
**500** | Could not update device - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firmware**
> update_firmware(firmware)

Update firmware

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.firmware import Firmware
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    firmware = Firmware(
        id=1,
        name="name_example",
        version=1,
        url="url_example",
        md5="md5_example",
    ) # Firmware | New firmware values

    # example passing only required values which don't have defaults set
    try:
        # Update firmware
        api_instance.update_firmware(firmware)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->update_firmware: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firmware** | [**Firmware**](Firmware.md)| New firmware values |
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated firmware |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not update firmware - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mission**
> update_mission(mission)

Update mission

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.mission import Mission
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mission = Mission(
        id=1,
        name="name_example",
        description="description_example",
        scheduled=dateutil_parser('1970-01-01T00:00:00.00Z'),
        dashboard_url="dashboard_url_example",
        live=True,
        status="Pending",
        spy=1,
        firmware=1,
        dataseries=1,
        user=1,
        textile=1,
    ) # Mission | 

    # example passing only required values which don't have defaults set
    try:
        # Update mission
        api_instance.update_mission(mission)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->update_mission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission** | [**Mission**](Mission.md)|  |
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated mission |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not update mission - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_spy**
> update_spy(spy)

Update spy

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    spy = Spy() # Spy | 

    # example passing only required values which don't have defaults set
    try:
        # Update spy
        api_instance.update_spy(spy)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->update_spy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spy** | [**Spy**](Spy.md)|  |
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated spy |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not update spy - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_textile**
> update_textile(textile)

Update textile

### Example

```python
import time
import spectre_api_client
from spectre_api_client.api import default_api
from spectre_api_client.model.textile import Textile
from spectre_api_client.model.error_msg import ErrorMsg
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://localhost:5000"
)


# Enter a context with an instance of the API client
with spectre_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    textile = Textile(
        id=1,
        name="name_example",
        length=1,
        width=1,
        height=1,
        material="material_example",
        titer=1,
        gsm=1,
        warp=1,
        weft=1,
        binding="binding_example",
        conductivity="conductivity_example",
        metadata="metadata_example",
        manufacturer="manufacturer_example",
    ) # Textile | 

    # example passing only required values which don't have defaults set
    try:
        # Update textile
        api_instance.update_textile(textile)
    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->update_textile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textile** | [**Textile**](Textile.md)|  |
 **id** | **int**|  | defaults to 0

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated textile |  -  |
**400** | Insufficient data or not allowed values |  -  |
**500** | Could not update textile - server side error |  -  |
**0** | Generic error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

