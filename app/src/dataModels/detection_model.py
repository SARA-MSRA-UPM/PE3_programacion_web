# external imports

# internal imports

class DetectionModel:
    def __init__(
            self,
            radar_name: str,
            distance_to_radar: float,
            relative_facing: float,
    ):
        self.radar_name = radar_name
        self.distance_to_radar = distance_to_radar
        self.relative_facing = relative_facing
