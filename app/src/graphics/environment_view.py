# external imports
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# internal imports
from src.models.radar_model import RadarModel
from src.models.radar_detection_model import RadarDetectionModel


class EnvironmentView:
    def __init__(
            self,
            axes: plt.axes):
        self.axes = axes

    def plot_new_radar_detection(self):
        pass

