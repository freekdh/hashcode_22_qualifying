from dataclasses import dataclass
from typing import List, Set

from objects import Contributor, Project, Role

@dataclass(frozen=True, eq=True)
class Assignment:
    contributor: Contributor
    role: Role

@dataclass(frozen=True, eq=True)
class ProjectSolution:
    project: Project
    start_day: int
    end_day: int
    assignments: Set[Assignment]

    # def __post_init__(self):
    #     for role in self.project.roles:
    #         assert self.assignments
    #     # Here we check that all the roles in the project have an assignment...

@dataclass
class Solution:
    project_solutions: List[ProjectSolution]
