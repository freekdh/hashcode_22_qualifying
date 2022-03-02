from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass(frozen=True, eq=True)
class Skill:
    name: str
    level: int

    def __geq__(self, other: "Skill"):
        return self.level > other.level
    
    def __leq__(self, other: "Skill"):
        return self.level < other.level
    
    def __eq__(self, other: "Skill"):
        return self.level == other.level

    def copy(self):
        return Skill(self.name, self.level)
    
    def increase_in_level(self):
        return Skill(self.name, self.level+1)

@dataclass(frozen=True, eq=True)
class Contributor:
    name: str
    skills: Tuple[Skill]
    num_skills: int

@dataclass(frozen=True, eq=True)
class Role:
    index: int
    skill: Skill

@dataclass(frozen=True, eq=True)
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    roles: Tuple[Role]

