import black
import browser_cookie3
import requests
import sys
import tenacity


class LeetCodeSession:
    LEETCODE_URL = "https://leetcode.com"

    def __init__(self, question_frontend_id=None):
        self.session = self.set_session()
        self.headers = {
            "origin": LeetCodeSession.LEETCODE_URL,
            "referer": LeetCodeSession.LEETCODE_URL,
            "x-requested-with": "XMLHttpRequest",
            "x-csrftoken": self.session.cookies.get("csrftoken"),
        }

        # Problem id is the questionFrontendId, not the questionId
        # A bit sus, but I don't exactly know what should be used
        self.question_frontend_id = question_frontend_id
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
        cookie = browser_cookie3.firefox(domain_name="leetcode")
        session = requests.Session()
        session.get(LeetCodeSession.LEETCODE_URL)  # Get the csrftoken if not captured by browser_cookie3.

        for c in cookie:
            if c.name in ("LEETCODE_SESSION", "csrftoken"):
                session.cookies.set_cookie(c)

        if session.cookies.get("LEETCODE_SESSION") is None or session.cookies.get("csrftoken") is None:
            print("User is not authenticated.")
            print(session.cookies.get("LEETCODE_SESSION"))
            print(session.cookies.get("csrftoken"))
            sys.exit(1)

        return session

    @tenacity.retry(
        retry=tenacity.retry_if_result(lambda res: res["state"] != "SUCCESS"),
        stop=tenacity.stop_after_attempt(5),
        wait=tenacity.wait_exponential(multiplier=1, min=2, max=4),
    )
    def try_get_expected(self, submission_id):
        try:
            res = self.session.get(f"{LeetCodeSession.LEETCODE_URL}/submissions/detail/{submission_id}/check/")
            return res.json()
        except requests.ConnectionError:
            print("Error: Request failed.")
            sys.exit(1)
        except requests.JSONDecodeError:
            print(res.text)
            print("Error: Invalid JSON response.")
            sys.exit(1)

    def graphql(self, query, variables):
        response = self.try_request_post(
            url=f"{LeetCodeSession.LEETCODE_URL}/graphql/",
            json={"query": query, "variables": variables},
        )

        if "data" not in response:
            print("Error: No data in response.")
            print(response)
            sys.exit(1)

        return response["data"]

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

    def get_problem_info(self, title_slug):
        query = """
            query questionTitle($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                questionId
                titleSlug
              }
            }
        """

        variables = {"titleSlug": title_slug}

        return self.graphql(query, variables)["question"]

    def get_problem_slug(self, problem_frontend_id):
        # It's also possible to get the questionId, but in fact it returns the
        # questionFrontendId which is not the same as the questionId.
        # I guess the graphql was updated but some old code is still available.
        # There is certainly a better way to get the titleSlug from the problem number... But hey, it works.
        query = """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(categorySlug: $categorySlug limit: $limit skip: $skip filters: $filters) {
                questions: data {
                    titleSlug
                }
            }
        }
        """
        variables = {
            "categorySlug": "",
            "skip": problem_frontend_id - 1,
            "limit": 1,
            "filters": {},
        }

        return self.graphql(query, variables)["problemsetQuestionList"]["questions"][0]["titleSlug"]

    def get_daily_problem_slug(self):
        query = """
        query questionOfToday {
          activeDailyCodingChallengeQuestion {
            question{
             titleSlug 
             questionFrontendId
            }
          }
        }
        """

        return self.graphql(query, {})["activeDailyCodingChallengeQuestion"]["question"]

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

        answer = self.try_request_post(
            f"{LeetCodeSession.LEETCODE_URL}/problems/{title_slug}/interpret_solution/", json
        )

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

        answer = self.try_request_post(f"{LeetCodeSession.LEETCODE_URL}/problems/{title_slug}/submit/", json)

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

    def set_problem_infos(self):
        if self.question_frontend_id is None:
            problem = self.get_daily_problem_slug()
            self.question_frontend_id = int(problem["questionFrontendId"])
            problem_slug = problem["titleSlug"]
        else:
            problem_slug = self.get_problem_slug(self.question_frontend_id)

        problem = self.get_problem_info(problem_slug)
        self.title_slug = problem["titleSlug"]
        self.question_id = problem["questionId"]
