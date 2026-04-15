# external imports
# internal imports


class RadarDetectionModel:
    def __init__(
            self,
            radar_name: str,
            distance_to_radar: float,
            relative_facing: float,
    ):
        self.radar_name = radar_name
        self.distance_to_radar = distance_to_radar
        self.relative_facing = relative_facing

    def __repr__(self):
        return ("RadarDetection("
            f"radar={self.radar_name}, "
            f"distance={self.distance_to_radar}, "
            f"facing={self.relative_facing}, "
            ")")
