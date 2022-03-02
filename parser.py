from objects import Contributor, Project, Skill, Role
from problem import Problem

class Parser:
    def __init__(self):
        pass
    
    def parse(self, file_path: str) -> Problem:
        contributors, projects = set(), set()
        with open(file_path) as f:
            lines = [x.strip() for x in f.readlines()]
            line = 0
            n_contributors, n_projects = [int(x) for x in lines[line].split()]
            line += 1
            contributors = set()
            for i in range(n_contributors):
                name = lines[line].split()[0]
                num_skills = int(lines[line].split()[1])
                line += 1
                skills = list()
                for j in range(num_skills):
                    skill_name = lines[line].split()[0]
                    skill_level = int(lines[line].split()[1])
                    skill = Skill(name=skill_name, level=skill_level)
                    skills.append(skill)
                    line += 1
                contributor = Contributor(name=name, skills=tuple(skills), num_skills=num_skills)
                contributors.add(contributor)
            projects = set()
            for i in range(n_projects):
                project_name = lines[line].split()[0]
                duration, score, best_before, n_roles = [int(x) for x in lines[line].split()[1:]]
                project_duration = duration
                project_score = score
                project_best_before = best_before
                project_n_roles = n_roles
                line += 1
                roles = []
                for j in range(n_roles):
                    skill_name = lines[line].split()[0]
                    skill_level = int(lines[line].split()[1])
                    skill = Skill(name=skill_name, level=skill_level)
                    roles.append(Role(skill=skill, index=j))
                    line += 1
                project_roles = roles
                project = Project(name=project_name, duration=project_duration, score=project_score, best_before=project_best_before, roles=tuple(project_roles))
                projects.add(project)
            return Problem(contributors=contributors, projects=projects)

