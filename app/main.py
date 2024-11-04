# external imports
import random
from time import sleep
import requests

# internal imports
from src.dataModels.radar_model import RadarModel
from src.actors.stream_reader import StreamReader


BASE_IP = "127.0.0.1"
MAIN_URL = f"http://{BASE_IP}:8000"
SCENARIO_CONFIGURATION_URL = f"{MAIN_URL}/scenarioConfiguration"
SCENARIO_LIST_URL = f"{MAIN_URL}/scenarioList"
SCENARIO_ID_URL = f"{MAIN_URL}/scenario"

if __name__ == '__main__':

    # # Get Hello World
    # response_main = requests.get(MAIN_URL)
    # print(response_main.text)

    # Environment configuration
    radars = (
        RadarModel(
            radar_name="radar0",
            x=0,
            y=0,
            detection_range=500,
            orientation_initial=45,
            increment=5,
        ).model_to_dict_for_radar_server(),
        RadarModel(
            radar_name="radar1",
            x=500,
            y=500,
            detection_range=500,
            orientation_initial=45,
            increment=5,
        ).model_to_dict_for_radar_server()
    )
    requests.post(SCENARIO_CONFIGURATION_URL, json=radars)

    get_scenario_response = requests.get(SCENARIO_CONFIGURATION_URL)
    if get_scenario_response.status_code != 200:
        print("Error during environment configuration")
        print(get_scenario_response.text)
        exit(1)

    # Select environment to get data
    response_scenario_list = requests.get(SCENARIO_LIST_URL).json()
    print(response_scenario_list)
    id_scenario = response_scenario_list["scenarios"][
        random.randint(0, len(response_scenario_list["scenarios"]) - 1)
    ]

    response_scenario_id = requests.get(
        SCENARIO_ID_URL + f"/{id_scenario}"
    ).json()
    scenario_port = response_scenario_id["port"]

    # Open socket to start stream of detections
    stream_reader = StreamReader(url=BASE_IP, port=scenario_port)
    stream_reader.start()
