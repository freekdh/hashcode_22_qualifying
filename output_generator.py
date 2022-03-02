
from solution import Solution


class OutputGenerator:
    def write(self, solution: Solution, file_path: str):
        # Write the solution to a file
        with open(file_path, "w") as output_file:
            n_excecuted_projects = str(len(solution.project_solutions))
            output_file.write(n_excecuted_projects + "\n")
            for project_solution in solution.project_solutions:
                project_name = project_solution.project.name
                output_file.write(project_name + "\n")
                for assignment in sorted(project_solution.assignments, key=lambda x: x.role.index):
                    output_file.write(f"{assignment.contributor.name} ")
                output_file.write("\n")
                    
