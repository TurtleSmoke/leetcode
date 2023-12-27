#!.venv/bin/python
from utils.GenerateLeetCodeProblem import GenerateLeetCodeProblem
from utils.PublishLeetCodeProblem import PublishLeetCodeProblem

import sys

# To lazy to use real argument parsing
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python leetcode.py <generate|publish> <problem_number> [solution_number]")
        sys.exit(1)

    if sys.argv[1] == "generate":
        if len(sys.argv) != 3:
            print("Usage: python generate_problem.py <problem_number>")
            sys.exit(1)

        generate_problem = GenerateLeetCodeProblem(int(sys.argv[2]))
        generate_problem.get_infos()
        generate_problem.dump()
    elif sys.argv[1] == "publish":
        if len(sys.argv) not in (3, 4):
            print("Usage: python publish_problem.py <problem_number> [solution_number]")
            sys.exit(1)

        publish_problem = PublishLeetCodeProblem(*map(int, sys.argv[2:]))
        publish_problem.publish_problem()
    else:
        print("Usage: python publish_problem.py <generate|publish> <problem_number> [solution_number]")
        sys.exit(1)
