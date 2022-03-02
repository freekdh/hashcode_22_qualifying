
from parser import Parser


def test_first_problem():
    problem = Parser().parse(file_path="/Users/freekdehaas/Downloads/input_data/a_an_example.in.txt")

    assert len(problem.projects) == 3
    assert len(problem.contributors) == 3

    assert {contributor.name for contributor in problem.contributors} == {"Anna", "Bob", "Maria"}

if __name__ == "__main__":
    test_first_problem()