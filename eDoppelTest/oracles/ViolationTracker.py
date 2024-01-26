import os
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, List, Set, Tuple

import pandas as pd

from config import PROJECT_ROOT


class ViolationTracker:
    """
    Helper class to track violations detected during scenario generation
    """

    tracker: DefaultDict[str, DefaultDict[str, Set[object]]]
    scenario_tracker: List
    __instance = None

    def __init__(self) -> None:
        self.tracker = defaultdict(lambda: defaultdict(lambda: set()))
        self.scenario_tracker = list()
        ViolationTracker.__instance = self

    @staticmethod
    def get_instance() -> "ViolationTracker":
        """
        Gets the singleton instance

        :returns: instance
        :rtype: ViolationTracker
        """
        return ViolationTracker.__instance

    def add_violation(
        self, gname, sname, record_file, mt, st, data, force=True
    ) -> bool:
        """
        Adds a violation to the tracker

        :param str gname: generation name
        :param str sname: scenario name
        :param str record_file: name of the record file
        :param str mt: main type of the violation
        :param str st: sub type of the violation
        :param any data: any underlying data to distinguish violation
        :param bool force: forcing add even if it is a duplicate

        :returns: True if added, False otherwise
        :rtype: bool
        """
        if force:
            self.scenario_tracker.append(
                (f"{gname}/{sname}", mt, st, data, record_file)
            )
            return True

        if data not in self.tracker[mt][st]:
            self.tracker[mt][st].add(data)
            self.scenario_tracker.append(
                (f"{gname}/{sname}", mt, st, data, record_file)
            )
            return True
        return False

    def save_to_file(self):
        """
        Save the tracked violations to a csv file in ``f'{RECORDS_DIR}/summary.csv'``
        """
        column_names = ["scenario_id", "main_type", "sub_type", "data", "record_path"]
        df = pd.DataFrame(columns=column_names)
        for scenario in self.scenario_tracker:
            df.loc[len(df.index)] = [*scenario]
        records_dir = Path(PROJECT_ROOT, "out")
        if not records_dir.exists():
            records_dir.mkdir(parents=True)
        df.to_csv(Path(records_dir, "summary.csv"))

    def clear(self):
        """
        Clears all tracked violations
        """
        self.tracker = defaultdict(lambda: defaultdict(lambda: set()))
        self.scenario_tracker = list()

    def print(self):
        """
        Helper function to print tracked violations to terminal
        """
        column_names = ["scenario_id", "main_type", "sub_type", "data", "record_path"]
        df = pd.DataFrame(columns=column_names)
        for scenario in self.scenario_tracker:
            df.loc[len(df.index)] = [*scenario]
        print(df[["main_type", "sub_type", "data"]])
