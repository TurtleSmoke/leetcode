import os
import re
import sys

# pylint: disable=wildcard-import,unused-wildcard-import
from typing import *  # Kind of hacky, but it's required since we can not know the output type of the problem

import black
import jinja2

from .LeetCodeSession import LeetCodeSession


class GenerateLeetCodeProblem(LeetCodeSession):
    def __init__(self, question_frontend_id=None):
        super().__init__(question_frontend_id)
        self.template = jinja2.Template(open("scripts/utils/templates/problem_template").read())
        self.problem_info = None

    def get_default_code(self, code_snippets, lang="Python3"):
        python3_snippet = next(json["code"] for json in code_snippets if json["lang"] == lang)

        try:
            expected_output_type = eval(python3_snippet.split("->")[1].split(":")[0].strip())
        except (NameError, IndexError):
            return python3_snippet + "return None"

        if expected_output_type is None:
            return python3_snippet + "return\n"

        origin_expected_output_type = get_origin(expected_output_type)
        default_value = expected_output_type() if origin_expected_output_type is None else origin_expected_output_type()

        return python3_snippet + f"return {repr(default_value)}\n"

    def get_infos(self):
        if self.title_slug is None or self.question_id is None or self.problem_info is None:
            self.set_problem_infos()

        testcases_input = self.get_problem_example_test_case(self.title_slug)
        default_code = self.get_default_code(self.get_code_snippet(self.title_slug))
        dry_run_answer = self.send_dry_run(self.title_slug, "\n".join(testcases_input), self.question_id, default_code)

        if dry_run_answer["status_code"] != 10:
            print(dry_run_answer)
            sys.exit(1)

        # Each testcase input has one line per input
        testcases_input = list(map(lambda s: s.split("\n"), testcases_input))
        # Replace null by None, useful when input is Optional
        testcases_input = [[input.replace("null", "None") for input in inputs] for inputs in testcases_input]
        # Replace true and false by True and False
        testcases_input = [
            [input.replace("true", "True").replace("false", "False").replace("null", "None") for input in inputs]
            for inputs in testcases_input
        ]
        testcases_input = [tuple(map(eval, inputs)) for inputs in testcases_input]

        testcases_expected = dry_run_answer["expected_code_answer"]
        # Replace true and false by True and False
        testcases_expected = [
            expected.replace("true", "True").replace("false", "False").replace("null", "None")
            for expected in testcases_expected
        ]
        self.problem_info = {
            "default_code": default_code,
            "testcases_input": testcases_input,
            "testcases_expected": testcases_expected,
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
        if "ListNode" in self.problem_info["default_code"]:
            imports.append("from problems.utils import ListNode")
        elif "TreeNode" in self.problem_info["default_code"]:
            imports.append("from problems.utils import TreeNode")
        elif "Node" in self.problem_info["default_code"]:
            imports.append("from problems.utils import Node")

        solution = self.problem_info["default_code"]
        function_name = re.findall(r"def ([^_][^(]+)", self.problem_info["default_code"])[0]
        code = self.template.render(
            solution=solution,
            imports=imports,
            function_name=function_name,
            testcases=zip(self.problem_info["testcases_input"], self.problem_info["testcases_expected"], strict=False),
        )

        formatted_code = black.format_str(code, mode=self.black_mode)
        path = f"problems/problem_{self.question_frontend_id:04d}/"
        os.makedirs(path, exist_ok=True)
        with open(path + "solution_1.py", "w") as f:
            f.write(formatted_code)

        print(f"Generated problem {self.question_frontend_id}")
        print(f"Check it out at {LeetCodeSession.LEETCODE_URL}/problems/{self.title_slug}/")
