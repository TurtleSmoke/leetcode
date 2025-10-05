import ast
import sys

import black

from .LeetCodeSession import LeetCodeSession


class PublishLeetCodeProblem(LeetCodeSession):
    def __init__(self, question_frontend_id=None, solution_number=1):
        super().__init__(question_frontend_id)
        self.solution_number = solution_number

        self.submission_detail = None
        self.code_path = None
        self.full_code = None
        self.tree = None

    def add_failed_testcase(self):
        # Testcase has one line per input
        input_formatted = self.submission_detail["last_testcase"].split("\n")
        expected_output = (
            self.submission_detail["expected_output"]
            .replace("true", "True")
            .replace("false", "False")
            .replace("null", "None")
        )

        input_formatted = tuple(eval(x.replace("null", "None")) for x in input_formatted)
        expected_output = eval(expected_output)

        tests = next(node for node in self.tree.body if isinstance(node, ast.Assign) and node.targets[0].id == "tests")
        tests.value.elts.append(
            ast.Tuple(
                elts=[
                    ast.Constant(value=input_formatted),
                    ast.Constant(value=expected_output),
                ],
            ),
        )

        # Add an element that will be removed to keep a trailing comma for better formatting with black
        for test in tests.value.elts:
            test.elts.append(ast.Str("TRAILING_TO_REMOVE"))

    def get_code_to_submit(self):
        imports = [
            ast.get_source_segment(self.full_code, node)
            for node in self.tree.body
            if isinstance(node, ast.Import)
            or (isinstance(node, ast.ImportFrom) and "problems.utils" not in node.module)
        ]

        solution = next(
            ast.get_source_segment(self.full_code, node) for node in self.tree.body if isinstance(node, ast.ClassDef)
        )

        return "\n".join(imports) + "\n" + solution

    def dump_new_code(self):
        self.add_failed_testcase()
        code = ast.unparse(self.tree).replace("'TRAILING_TO_REMOVE'", "")
        formatted_code = black.format_str(code, mode=self.black_mode)

        with open(self.code_path, "w") as solution:
            solution.write(formatted_code)

    def publish_problem(self):
        if self.title_slug is None:
            self.set_problem_infos()

        self.code_path = f"problems/problem_{self.question_frontend_id:04d}/solution_{self.solution_number}.py"
        self.full_code = open(self.code_path).read()
        self.tree = ast.parse(self.full_code)

        self.submission_detail = self.send_submission(self.title_slug, self.question_id, self.get_code_to_submit())

        if self.submission_detail["status_code"] == 10:
            print("Submission Accepted!")
        elif self.submission_detail["status_code"] in (11, 12, 14, 15):
            # Blablabla, you should use an Enum, blabla, I'm lazy.
            # 11: Wrong Answer
            # 12: Memory Limit Exceeded
            # 14: Time Limit Exceeded
            # 15: Runtime Error
            self.dump_new_code()
            print("Added failed testcase to code.")
            print(self.submission_detail["status_msg"])
        else:
            print("Submission Error!")
            print(self.submission_detail)
            sys.exit(1)
