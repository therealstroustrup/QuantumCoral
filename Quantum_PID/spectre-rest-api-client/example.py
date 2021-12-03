import time
import spectre_api_client
from pprint import pprint
from spectre_api_client.api import default_api
from spectre_api_client.model.command import Command
from spectre_api_client.model.command_list import CommandList
from spectre_api_client.model.data_point_list import DataPointList
from spectre_api_client.model.data_series import DataSeries
from spectre_api_client.model.device import Device
from spectre_api_client.model.device_list import DeviceList
from spectre_api_client.model.error_msg import ErrorMsg
from spectre_api_client.model.firmware import Firmware
from spectre_api_client.model.firmware_list import FirmwareList
from spectre_api_client.model.id_obj import IdObj
from spectre_api_client.model.mission import Mission
from spectre_api_client.model.mission_list import MissionList
from spectre_api_client.model.spy import Spy
from spectre_api_client.model.spy_list import SpyList
from spectre_api_client.model.textile import Textile
from spectre_api_client.model.textile_list import TextileList
from spectre_api_client.model.url import Url
from spectre_api_client.model.versions import Versions
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host = "https://smarttexserver.projekte.fh-hagenberg.at/icapi"
)

# Enter a context with an instance of the API client
with spectre_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    # command = Command(
    #     id=1,
    #     text_command="text_command_example",
    #     delay_ms=1,
    #     device=1,
    #     mission=1,
    # ) # Command |

    try:
        # Create new command
        response = api_instance.get_commands()
        print(type(response))
        input()
        pprint(response)
        input()
        response = api_instance.get_devices()
        pprint(response)
        input()
        # response = api_instance.get_firmware_list()
        # pprint(response)
        # input()
        response = api_instance.get_missions()
        pprint(response)
        input()
        response = api_instance.get_spies()
        pprint(response)
        input()
        response = api_instance.get_textiles()
        pprint(response)
        input()
        response = api_instance.get_version()
        pprint(response)

    except spectre_api_client.ApiException as e:
        print("Exception when calling DefaultApi->add_command: %s\n" % e)
