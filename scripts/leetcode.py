#!.venv/bin/python
from utils.GenerateLeetCodeProblem import GenerateLeetCodeProblem
from utils.PublishLeetCodeProblem import PublishLeetCodeProblem

import sys

# To lazy to use real argument parsing
if __name__ == "__main__":
    if sys.argv[1] == "generate":
        if len(sys.argv) not in (2, 3):
            print("Usage: python generate_problem.py [problem_id]")
            sys.exit(1)

        generate_problem = GenerateLeetCodeProblem(*map(int, sys.argv[2:]))
        generate_problem.get_infos()
        generate_problem.dump()
    elif sys.argv[1] == "publish":
        if len(sys.argv) not in (2, 3, 4):
            print("Usage: python publish_problem.py <problem_id> [solution_number]")
            sys.exit(1)

        publish_problem = PublishLeetCodeProblem(*map(int, sys.argv[2:]))
        publish_problem.publish_problem()
    else:
        print("Usage: python publish_problem.py generate [problem_id]")
        print("Usage: python publish_problem.py publish <problem_id> [solution_number]")
        sys.exit(1)
