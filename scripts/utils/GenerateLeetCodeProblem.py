from .LeetCodeSession import LeetCodeSession

# pylint: disable=wildcard-import,unused-wildcard-import
from typing import *  # Kind of hacky, but it's required since we can not know the output type of the problem
import black
import jinja2
import os
import re
import sys


class GenerateLeetCodeProblem(LeetCodeSession):
    def __init__(self, problem_number):
        super().__init__(problem_number)
        self.problem_info = None
        self.template = jinja2.Template(open("scripts/utils/templates/problem_template").read())

    def get_default_code(self, code_snippets, lang="Python3"):
        python3_snippet = next(json["code"] for json in code_snippets if json["lang"] == lang)

        expected_output_type = eval(python3_snippet.split("->")[1].split(":")[0].strip())
        if expected_output_type is None:
            return python3_snippet + "return\n"

        origin_expected_output_type = get_origin(expected_output_type)
        default_value = expected_output_type() if origin_expected_output_type is None else origin_expected_output_type()

        return python3_snippet + f"return {repr(default_value)}\n"

    def get_infos(self):
        if self.title_slug is None or self.question_id is None:
            self.set_problem_infos(self.problem_number)

        testcases_input = self.get_problem_example_test_case(self.title_slug)
        default_code = self.get_default_code(self.get_code_snippet(self.title_slug))
        dry_run_answer = self.send_dry_run(self.title_slug, "\n".join(testcases_input), self.question_id, default_code)

        if dry_run_answer["status_code"] != 10:
            print(dry_run_answer)
            sys.exit(1)

        # Each testcase input has one line per input
        testcases_input = list(map(str.split, testcases_input))
        testcases_input = [tuple(map(eval, inputs)) for inputs in testcases_input]
        self.problem_info = {
            "default_code": default_code,
            "testcases_input": testcases_input,
            "testcases_expected": dry_run_answer["expected_code_answer"],
        }

    def dump(self):
        if self.problem_info is None:
            return

        # Not optimal, does not handle custom import from Leetcode (or custom class, to improve)
        imports = ["import pytest"]
        if "List[" in self.problem_info["default_code"]:
            imports.append("from typing import List")
        if "Optional[" in self.problem_info["default_code"]:
            imports.append("from typing import Optional")

        solution = self.problem_info["default_code"]
        function_name = re.findall(r"def ([^(]+)", self.problem_info["default_code"])[0]
        code = self.template.render(
            solution=solution,
            imports=imports,
            function_name=function_name,
            testcases=zip(self.problem_info["testcases_input"], self.problem_info["testcases_expected"]),
        )

        formatted_code = black.format_str(code, mode=self.black_mode)
        path = f"problems/problem_{self.problem_number:04d}/"
        os.makedirs(path, exist_ok=True)
        with open(path + "solution_1.py", "w") as f:
            f.write(formatted_code)
