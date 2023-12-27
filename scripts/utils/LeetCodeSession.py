import black
import browser_cookie3
import requests
import sys
import tenacity

LEETCODE_URL = "https://leetcode.com"


class LeetCodeSession:
    def __init__(self, problem_number=None):
        self.session = self.set_session()
        self.headers = {
            "origin": LEETCODE_URL,
            "referer": LEETCODE_URL,
            "x-requested-with": "XMLHttpRequest",
            "x-csrftoken": self.session.cookies.get("csrftoken"),
        }

        self.problem_number = problem_number
        self.title_slug = None
        self.question_id = None

        self.black_mode = self.set_black_mode()
        self.set_black_mode()

    def set_black_mode(self):
        toml_config = black.parse_pyproject_toml(black.find_pyproject_toml(".."))
        toml_config["target_version"] = {black.TargetVersion[v.upper()] for v in toml_config["target_version"]}

        return black.Mode(
            line_length=toml_config["line_length"],
            target_versions=toml_config["target_version"],  # Why does parsing the pyproject returns another key name?
        )

    @staticmethod
    def set_session():
        cookie = browser_cookie3.firefox(domain_name="leetcode.com")
        session = requests.Session()

        for c in cookie:
            if c.name in ("LEETCODE_SESSION", "csrftoken"):
                session.cookies.set_cookie(c)

        if session.cookies.get("LEETCODE_SESSION") is None or session.cookies.get("csrftoken") is None:
            print("User is not authenticated.")
            sys.exit(1)

        return session

    @tenacity.retry(
        retry=tenacity.retry_if_result(lambda res: res["state"] != "SUCCESS"),
        stop=tenacity.stop_after_attempt(5),
        wait=tenacity.wait_fixed(2),
    )
    def try_get_expected(self, submission_id):
        try:
            res = self.session.get(f"{LEETCODE_URL}/submissions/detail/{submission_id}/check/")
            return res.json()
        except requests.ConnectionError:
            print("Error: Request failed.")
            sys.exit(1)
        except requests.JSONDecodeError:
            print(res.text)
            print("Error: Invalid JSON response.")
            sys.exit(1)

    def graphql(self, query, variables):
        return self.try_request_post(
            url=f"{LEETCODE_URL}/graphql/",
            json={"query": query, "variables": variables},
        )["data"]

    def try_request_post(self, url, json):
        try:
            res = self.session.post(url, json=json, headers=self.headers)
            return res.json()
        except requests.ConnectionError:
            print("Error: Request failed.")
            sys.exit(1)
        except requests.JSONDecodeError:
            print(res.text)
            print("Error: Invalid JSON response.")
            sys.exit(1)

    def get_submission_detail(self, submission_id):
        return self.try_get_expected(submission_id)

    def get_problem_info(self, problem_number):
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

        return self.graphql(query, variables)["problemsetQuestionList"]["questions"][0]

    def get_problem_example_test_case(self, title_slug):
        query = """
        query getQuestionDetail($titleSlug: String!) {
           question(titleSlug: $titleSlug) {
                exampleTestcaseList
             }
        }
        """
        variables = {"titleSlug": title_slug}

        return self.graphql(query, variables)["question"]["exampleTestcaseList"]

    def send_dry_run(self, title_slug, data_input, question_id, typed_code):
        json = {
            "lang": "python3",
            "question_id": f"{question_id}",
            "typed_code": f"{typed_code}",
            "data_input": f"{data_input}",
        }

        answer = self.try_request_post(f"{LEETCODE_URL}/problems/{title_slug}/interpret_solution/", json)

        if "interpret_id" not in answer:
            print(f"Error: No interpret_id in response:\n{answer}")
            sys.exit(1)

        return self.get_submission_detail(answer["interpret_id"])

    def send_submission(self, title_slug, question_id, typed_code):
        json = {
            "lang": "python3",
            "question_id": f"{question_id}",
            "typed_code": f"{typed_code}",
        }

        answer = self.try_request_post(f"{LEETCODE_URL}/problems/{title_slug}/submit/", json)

        if "submission_id" not in answer:
            print(f"Error: No submission_id in response:\n{answer}")
            sys.exit(1)

        return self.get_submission_detail(answer["submission_id"])

    def get_code_snippet(self, title_slug):
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
        code_snippets = self.graphql(query, variables)
        return code_snippets["question"]["codeSnippets"]

    def set_problem_infos(self, problem_number):
        problem = self.get_problem_info(problem_number)
        self.title_slug = problem["titleSlug"]
        self.question_id = problem["questionId"]
