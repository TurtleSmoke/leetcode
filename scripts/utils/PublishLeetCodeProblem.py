from .LeetCodeSession import LeetCodeSession

import ast
import black
import sys


class PublishLeetCodeProblem(LeetCodeSession):
    def __init__(self, problem_id, solution_number=1):
        super().__init__(problem_id)
        self.code_path = f"problems/problem_{self.problem_id:04d}/solution_{solution_number}.py"
        self.submission_detail = None

        self.full_code = open(self.code_path).read()
        self.tree = ast.parse(self.full_code)

    def add_failed_testcase(self):
        # Testcase has one line per input
        input_formatted = self.submission_detail["input"].split("\n")
        input_formatted = tuple(map(eval, input_formatted))
        expected_output = eval(self.submission_detail["expected_output"])
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
            if isinstance(node, (ast.Import, ast.ImportFrom))
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
            self.set_problem_infos(self.problem_id)

        self.submission_detail = self.send_submission(self.title_slug, self.question_id, self.get_code_to_submit())

        if self.submission_detail["status_code"] == 10:
            print("Submission Accepted!")
        elif self.submission_detail["status_code"] == 11:
            self.dump_new_code()
            print("Added failed testcase to code.")
        else:
            print("Submission Error!")
            print(self.submission_detail)
            sys.exit(1)
