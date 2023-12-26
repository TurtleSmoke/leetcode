import os
import re
import sys
from typing import *  # Kind of hacky, but it's required since we can not know what types are used in the code snippet

import browser_cookie3
import requests
import tenacity

session = None

BASE_URL = "https://leetcode.com"
GRAPHQL_URL = f"{BASE_URL}/graphql/"
INTERPRET_URL = lambda slug: f"{BASE_URL}/problems/{slug}/interpret_solution/"
CHECK_URL = lambda qid: f"{BASE_URL}/submissions/detail/{qid}/check/"


def is_interpret_done(res):
    return res["state"] != "SUCCESS"


@tenacity.retry(
    retry=tenacity.retry_if_result(is_interpret_done),
    stop=tenacity.stop_after_attempt(5),
    wait=tenacity.wait_fixed(2),
)
def try_get_expected(submission_id):
    try:
        res = session.get(CHECK_URL(submission_id))
        return res.json()
    except requests.ConnectionError:
        print("Error: Request failed.")
        sys.exit(1)
    except requests.JSONDecodeError:
        print(res.text)
        print("Error: Invalid JSON response.")
        sys.exit(1)


def graphql(query, variables, headers=None):
    return try_request_post(
        url=GRAPHQL_URL,
        json={"query": query, "variables": variables},
        headers=headers,
    )["data"]


def try_request_post(url, json, headers=None, cookies=None):
    try:
        res = session.post(url, json=json, headers=headers, cookies=cookies)
        return res.json()
    except requests.ConnectionError:
        print("Error: Request failed.")
        sys.exit(1)
    except requests.JSONDecodeError:
        print(res.text)
        print("Error: Invalid JSON response.")
        sys.exit(1)


def get_problem_info(problem_number):
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(categorySlug: $categorySlug limit: $limit skip: $skip filters: $filters) {
            questions: data {
                questionId
                titleSlug
            }
        }
    }
    """
    variables = {
        "categorySlug": "",
        "skip": problem_number - 1,
        "limit": 1,
        "filters": {},
    }

    return graphql(query, variables)["problemsetQuestionList"]["questions"][0]


def get_problem_input(title_slug):
    query = """
    query getQuestionDetail($titleSlug: String!) {
       question(titleSlug: $titleSlug) {
            exampleTestcaseList
         }
    }
    """
    variables = {"titleSlug": title_slug}

    return graphql(query, variables)["question"]["exampleTestcaseList"]


def get_problem_expected(title_slug, data_input, question_id, typed_code):
    json = {
        "lang": "python3",
        "question_id": f"{question_id}",
        "typed_code": f"{typed_code}",
        "data_input": f"{data_input}",
    }

    headers = {
        "origin": BASE_URL,
        "referer": BASE_URL,
        "x-requested-with": "XMLHttpRequest",
        "x-csrftoken": session.cookies.get("csrftoken"),
    }

    result = try_request_post(
        url=INTERPRET_URL(title_slug),
        json=json,
        headers=headers,
    )

    if "error" in result:
        print(result["error"])
        sys.exit(1)

    submissions_detail = try_get_expected(result["interpret_id"])

    if submissions_detail["status_code"] != 10:
        print(submissions_detail["status_msg"])
        sys.exit(1)

    return submissions_detail["expected_code_answer"]


def get_code_snippet(title_slug):
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            codeSnippets {
                lang
                code
            }
        }
    }
    """
    variables = {"titleSlug": f"{title_slug}"}
    code_snippets = graphql(query, variables)
    python3_snippet = {info["lang"]: info["code"] for info in code_snippets["question"]["codeSnippets"]}["Python3"]

    expected_output_type = eval(python3_snippet.split("->")[1].split(":")[0].strip())
    origin_expected_output_type = get_origin(expected_output_type)
    default_value = expected_output_type() if origin_expected_output_type is None else origin_expected_output_type()

    return python3_snippet + f"return {repr(default_value)}\n"


def set_session():
    cookie = getattr(browser_cookie3, "firefox")(domain_name="leetcode.com")
    global session
    session = requests.Session()
    for c in cookie:
        if c.name in ("LEETCODE_SESSION", "csrftoken"):
            session.cookies.set_cookie(c)


def get_problems_infos(n):
    problem = get_problem_info(n)
    input = get_problem_input(problem["titleSlug"])
    code = get_code_snippet(problem["titleSlug"])
    expected = get_problem_expected(problem["titleSlug"], "\n".join(input), problem["questionId"], code)

    input = list(map(str.split, input))

    return {
        "input": input,
        "code": code,
        "expected": expected,
    }


def generate_problem(problem_number):
    problem_info = get_problems_infos(problem_number)

    tests_template = (
        lambda input, expected: f"""    (
        {tuple(eval(i) for i in input)},
        {expected},
    ),"""
    )

    tests = (
        "tests = [\n"
        + "\n".join(
            tests_template(input, expected) for input, expected in zip(problem_info["input"], problem_info["expected"])
        )
        + "\n]"
    )

    problem_name = f"problem_{problem_number:04d}"
    os.makedirs(f"problems/{problem_name}", exist_ok=True)
    with open(f"problems/{problem_name}/solution_1.py", "w") as solution:
        if "List[" in problem_info["code"]:
            solution.writelines("from typing import List\n")
        if "Optional[" in problem_info["code"]:
            solution.writelines("from typing import Optional\n")

        solution.writelines("import pytest\n\n\n")
        solution.writelines(problem_info["code"])
        solution.writelines("\n\n")
        solution.writelines(tests)
        solution.writelines("\n\n\n")

        solution.writelines(
            f"""@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().{re.findall(r"def ([^(]+)", problem_info["code"])[0]}(*inputs)
    assert output == expected
"""
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_problem.py <problem_number>")
        sys.exit(1)

    set_session()
    generate_problem(int(sys.argv[1]))
