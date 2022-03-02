from dataclasses import dataclass
from typing import Set

from objects import Contributor, Project

@dataclass
class Problem:
    contributors: Set[Contributor]
    projects: Set[Project]
