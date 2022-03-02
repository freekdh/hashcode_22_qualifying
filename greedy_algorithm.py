from copy import deepcopy
from typing import Dict, List, Set
from objects import Contributor, Project, Role, Skill
from problem import Problem
from solution import Assignment, ProjectSolution, Solution

class NoValidContributorException(Exception):
    pass

class GreedyAlgorithm:
    def __init__(self):
        pass

    def _rank_projects(self, projects: Set[Project]) -> List[Project]:
        project_ranks = []
        project_dict = {project.name: project for project in projects}
        for project in projects:
            num_roles = len(project.roles)
            best_before = project.best_before # sooner is better
            score = project.score/(num_roles * project.duration * (0.1+best_before))
            project_ranks.append((project.name, score))
        sorted_projects_list = sorted(project_ranks, key=lambda x:x[1], reverse=True)
        sorted_projects = [project_dict[x[0]] for x in sorted_projects_list]

        return sorted_projects

    def _select_contributor(self, role: Role, available_contributors: Dict[Contributor, int], chosen_contributors) -> Contributor:
        # you can't choose a contributor from the chosen_contributor list.
        role_name = role.skill.name
        max_score = 0
        best_contributor = None
        for contributor, availability in available_contributors.items():
            if contributor in chosen_contributors:
                continue
            contributor_skill = 0
            for skill in contributor.skills:
                if skill.name == role_name:
                    contributor_skill = skill.level

            skill_delta = contributor_skill - role.skill.level  # lower is better
            num_skills = len(contributor.skills)    # lower is better
            score = (role.skill.level <= contributor_skill) / (0.1 + skill_delta * num_skills * availability)
            if score > max_score:
                max_score = score
                best_contributor = contributor
        if best_contributor is None:
            raise NoValidContributorException()
        return best_contributor

    def _compute_start_day(self, assignments, available_contributors):
        # find out when the project can start given the availability and the assignments
        # project can only start ones all contributors are available
        return max(available_contributors[assignment.contributor] for assignment in assignments)


    def _update_skill(self, skills, role):
        for skill in skills:
            if skill.name == role.skill.name and skill.level <= role.skill.level:
                yield skill.increase_in_level()
            else:
                yield skill.copy()

    def _update_available_contributors(self, available_contributors, assignments, end_day) -> Dict[Contributor, int]:
        # update the available contributors given that they end at the end_day of the project. 
        new_available_contributors = deepcopy(available_contributors)
        for assignment in assignments:
            del new_available_contributors[assignment.contributor]
            new_skills = tuple(self._update_skill(assignment.contributor.skills, assignment.role))
            new_available_contributors[Contributor(name=assignment.contributor.name, skills=new_skills, num_skills=None)] = end_day + 1
        return new_available_contributors


    def solve(self, problem: Problem):
        ranked_projects = self._rank_projects(problem.projects)

        available_contributors = {contributor: 0 for contributor in problem.contributors}

        project_solutions = list()
        failed_projects_list = []

        for focal_project in ranked_projects:
            chosen_contributors = set()
            try:
                assignments = set()
                for role in focal_project.roles:
                    contributor = self._select_contributor(role=role, available_contributors=available_contributors, chosen_contributors=chosen_contributors)
                    chosen_contributors.add(contributor)
                    assignments.add(Assignment(contributor=contributor, role=role))
            except NoValidContributorException:
                failed_projects_list.append(focal_project)
                # Going to skip this project because we can't find a contributor for a role
                continue

            start_day = self._compute_start_day(assignments, available_contributors)
            end_day = start_day + focal_project.duration

            available_contributors = self._update_available_contributors(available_contributors, assignments, end_day)
            project_solutions.append(ProjectSolution(project=focal_project, start_day=start_day, end_day=end_day, assignments=tuple(assignments)))


        # second pass...

        for focal_project in failed_projects_list:
            chosen_contributors = set()
            try:
                assignments = set()
                for role in focal_project.roles:
                    contributor = self._select_contributor(role=role, available_contributors=available_contributors, chosen_contributors=chosen_contributors)
                    chosen_contributors.add(contributor)
                    assignments.add(Assignment(contributor=contributor, role=role))
            except NoValidContributorException:
                # Going to skip this project because we can't find a contributor for a role
                continue

            start_day = self._compute_start_day(assignments, available_contributors)
            end_day = start_day + focal_project.duration

            available_contributors = self._update_available_contributors(available_contributors, assignments, end_day)
            project_solutions.append(ProjectSolution(project=focal_project, start_day=start_day, end_day=end_day, assignments=tuple(assignments)))

        return Solution(project_solutions=project_solutions)

