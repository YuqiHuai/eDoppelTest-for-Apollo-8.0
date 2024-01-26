from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
PROJECT_NAME = "eDoppelTest"
DATA_DIR = Path(PROJECT_ROOT, "data")
DOWNLOAD_DIR = Path(DATA_DIR, "download")

# Apollo Configurations
APOLLO_ROOT = Path(DATA_DIR, "apollo")
APOLLO_FLAGFILE = Path(APOLLO_ROOT, "modules", "common", "data", "global_flagfile.txt")
APOLLO_RELEASE = "https://github.com/ApolloAuto/apollo/archive/refs/tags/v8.0.0.zip"
APOLLO_RELEASE_NAME = "apollo-8.0.0"
SIM_CONTROL_RELEASE = (
    "https://github.com/YuqiHuai/sim_control_standalone/archive/refs/tags/v8.0.1.zip"
)
SIM_CONTROL_RELEASE_NAME = "sim_control_standalone-8.0.1"

# Map Configurations
MAPS_DIR = Path(DATA_DIR, "maps")
SUPPORTED_MAPS = list(x.name for x in MAPS_DIR.iterdir() if x.is_dir())


# Other Configurations
LOGGING_PREFIX_REGEX = (
    "^(?P<severity>[DIWEF])(?P<month>\d\d)(?P<day>\d\d) "
    "(?P<hour>\d\d):(?P<minute>\d\d):(?P<second>\d\d)\.(?P<microsecond>\d\d\d) "
    "(?P<filename>[a-zA-Z<][\w._<>-]+):(?P<line>\d+)"
)
LOGGING_FORMAT = (
    "<level>{level.name[0]}{time:MMDD}</level> "
    "<green>{time:HH:mm:ss.SSS}</green> "
    "<cyan>{file}:{line}</cyan>] "
    "<bold>{message}</bold>"
)

HD_MAP = "borregas_ave"

INSTANCE_MAX_WAIT_TIME = 5
MAX_ADC_COUNT = 2
MAX_PD_COUNT = 2
SCENARIO_UPPER_LIMIT = 30
FORCE_INVALID_TRAFFIC_CONTROL = False
RUN_FOR_HOUR = 1
