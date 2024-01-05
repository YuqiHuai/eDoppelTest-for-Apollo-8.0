from shapely.geometry import Polygon

from apollo import Channels
from apollo.utils import generate_adc_polygon, generate_obs_polygon
from typing import Optional, Tuple


class CollisionFitness:
    def __init__(self) -> None:
        self.interested_topics = [Channels.Localization.name, Channels.Obstacles.name]
        self.last_localization = None
        self.last_perception = None
        self.closest_distance = float("inf")
        self.violatoin_location: Optional[Tuple[float, float]] = None
        self.violation_time: Optional[float] = None

    def on_new_message(self, topic: str, msg, t: float) -> None:
        if topic not in self.interested_topics:
            # ignore messages from other topics
            return

        if self.violatoin_location and self.violation_time:
            # we already found a collision
            return

        if topic == Channels.Localization.name:
            self.last_localization = msg
        else:
            self.last_perception = msg

        if self.last_localization is None or self.last_perception is None:
            # we don't have enough information yet
            return

        ads_polygon = generate_adc_polygon(
            self.last_localization.pose.position, self.last_localization.pose.heading
        )
        shapely_ads_polygon = Polygon([(p.x, p.y) for p in ads_polygon])

        for obs in self.last_perception.perception_obstacle:
            obs_polygon = generate_obs_polygon(obs)
            shapely_obs_polygon = Polygon([(p.x, p.y) for p in obs_polygon])

            dist = shapely_ads_polygon.distance(shapely_obs_polygon)

            min_dist = min(self.closest_distance, dist)
            if min_dist < self.closest_distance:
                self.closest_distance = min_dist

            if min_dist == 0.0:
                self.violatoin_location = (
                    self.last_localization.pose.position.x,
                    self.last_localization.pose.position.y,
                )
                self.violation_time = t

    def get_fitness(self) -> float:
        return self.closest_distance
