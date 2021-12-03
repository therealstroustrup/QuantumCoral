#!/usr/bin/env python3
#!/usr/bin/env python2

import spectre_api_client
import argparse
import os
from spectre_api_client.api import default_api
# Defining the host is optional and defaults to https://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = spectre_api_client.Configuration(
    host="https://smarttexserver.projekte.fh-hagenberg.at/icapi"
)


def main(mission):
    # Enter a context with an instance of the API client
    with spectre_api_client.ApiClient(configuration) as api_client:
        api_instance = default_api.DefaultApi(api_client)
        try:
            mission = mission.replace("true", "True")
            mission = eval(mission)
            # Create new command
            missionID = mission['id']
            commandlist = api_instance.get_commands_from_mission(missionID)
            usedDevices = dict()
            for command in commandlist['commands']:
                usedDevices[command['device']] = api_instance.get_device_by_id(command['device'])['mac_address']

            device = dict()

            date_time = mission['scheduled']
            date_time = date_time.replace(':', '-')
            date_time = date_time.replace('T', '_')
            file_path = 'mission_queue/' + date_time + '.txt'

            file = open(file_path, "w")

            print(commandlist)

            for command in commandlist['commands']:
                if "?" in command:
                    print(device[command['device']].read(command['text_command']))
                else:
                    print(command['text_command'])
                    file.write(command['text_command'] + '\n')

            mission = api_instance.get_missions_by_id(missionID)
            mission['status'] = "Success"
            api_instance.update_mission(mission, missionID)
            print("finished")

        except spectre_api_client.ApiException as e:
            print("Exception when calling DefaultApi->update_mission: %s\n" % e)

        file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Callback for new Mission')
    parser.add_argument('Mission', help='')
    args = parser.parse_args()
    main(args.Mission)
