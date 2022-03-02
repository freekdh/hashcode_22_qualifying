

from parser import Parser

from greedy_algorithm import GreedyAlgorithm
from output_generator import OutputGenerator


def main():
    problems = ["a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]
    
    for problem_name in problems:
        print(f"Solving {problem_name}")
        problem = Parser().parse(file_path=f"/Users/freekdehaas/Downloads/input_data/{problem_name}.in.txt")

        greedy_algorithm = GreedyAlgorithm()

        solution = greedy_algorithm.solve(problem=problem)
        
        output_generator = OutputGenerator()
        output_generator.write(solution=solution, file_path=f"/Users/freekdehaas/Downloads/input_data/{problem_name}.out.txt")

if __name__ == "__main__":
    main()