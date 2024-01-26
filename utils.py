import os
import random
import string
import sys
from datetime import datetime
from pathlib import Path
from typing import List

from absl import flags
from absl.flags import FLAGS
from loguru import logger
from nanoid import generate

from apollo.map_service import MapService
from config import DATA_DIR, LOGGING_FORMAT, PROJECT_NAME, PROJECT_ROOT

_loaded_map_services = {}


def get_map_service_for_map(map_name: str):
    if map_name in _loaded_map_services:
        return _loaded_map_services[map_name]
    ms = MapService()
    ms.load_map_from_file(Path(DATA_DIR, "maps", map_name, "base_map.bin"))
    _loaded_map_services[map_name] = ms
    return ms


def generate_id(size=5):
    return generate(string.ascii_letters, size=size)


def set_up_gflags():
    # Execution flags
    flags.DEFINE_string("map", "borregas_ave", "Name of the map to use.")
    flags.DEFINE_integer("num_adc", 5, "Number of ADCs to use.")
    flags.DEFINE_boolean("dry_run", os.uname()[0] != "Linux", "Dry run mode.")
    flags.DEFINE_boolean("dreamview", False, "Enable Dreamview.")
    flags.DEFINE_string(
        "execution_id", datetime.now().strftime(r"%m%d_%H%M%S"), "Execution ID."
    )
    flags.DEFINE_integer("perception_frequency", 10, "Perception frequency.")
    flags.DEFINE_integer("scenario_length", 30, "Length of the scenario in seconds.")
    flags.DEFINE_boolean("colorize", True, "Colorize log output.")
    flags.DEFINE_string("log_level", "INFO", "Log level.")

    # Genetic algorithm flags
    flags.DEFINE_integer("num_scenario", 20, "Number of scenarios to generate.")
    flags.DEFINE_float("num_hour", 12.0, "Number of hours to generate scenarios for.")

    flags.DEFINE_float("mut_pb", 0.2, "Probability of mutation.")
    flags.DEFINE_float("cx_pb", 0.8, "Probability of crossover.")
    flags.DEFINE_float("add_pb", 0.1, "Probability of adding an obstacle.")
    flags.DEFINE_float("del_pb", 0.1, "Probability of deleting an obstacle.")
    flags.DEFINE_float("replace_pb", 0.1, "Probability of replacing the ego car.")


def get_out_dir(root: Path = PROJECT_ROOT, mkdir: bool = True) -> Path:
    result = Path(root, "out", f"{FLAGS.execution_id}_{FLAGS.map}")
    if not result.exists() and mkdir:
        result.mkdir(parents=True)
    return result


def get_log_file() -> Path:
    return Path(
        PROJECT_ROOT, "out", f"{FLAGS.execution_id}_{FLAGS.map}", f"{PROJECT_NAME}.log"
    )


def set_up_logging(level: str | int) -> None:
    # set up logging
    logger.remove()
    logger.add(get_log_file(), format=LOGGING_FORMAT, level=level, enqueue=True)
    logger.add(
        sys.stdout,
        format=LOGGING_FORMAT,
        colorize=FLAGS.colorize,
        level=level,
        enqueue=True,
    )


def random_numeric_id(length=5) -> List[int]:
    """
    Generates a list of random integer ids

    :param int length: expected length of the ID

    :returns: list of integer ids
    :rtype: List[int]
    """
    return sorted(random.sample(range(100000, 999999), k=length))
