# external imports

# internal imports

class RadarModel:
    def __init__(
            self,
            radar_name: str,
            x: float,
            y: float,
            detection_range: float,
            orientation_initial: float,
            increment: float,
    ):
        self.radar_name = radar_name
        self.x = x
        self.y = y
        self.detection_range = detection_range
        self.orientation_initial = orientation_initial
        self.increment = increment

    def model_to_dict_for_radar_server(self) -> dict:
        return {
            "name": self.radar_name,
            "position_x": self.x,
            "position_y": self.y,
            "detection_range": self.detection_range,
            "orientation_initial": self.orientation_initial,
            "increment": self.increment,
        }