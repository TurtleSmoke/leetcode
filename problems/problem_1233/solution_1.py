from collections import defaultdict
from typing import List

import pytest


class Solution:
    class Trie:
        def __init__(self):
            self.children = defaultdict(Solution.Trie)
            self.word = ""

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Solution.Trie()
        for path in folder:
            node = root
            sub_folders = path.split("/")
            for sub_folder in sub_folders[1:]:
                node = node.children[sub_folder]
            node.word = path

        def dfs(node):
            if node.word:
                yield node.word
            else:
                for child in node.children:
                    yield from dfs(node.children[child])

        return list(dfs(root))


tests = [
    (
        (["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"],),
        ["/a", "/c/d", "/c/f"],
    ),
    (
        (["/a", "/a/b/c", "/a/b/d"],),
        ["/a"],
    ),
    (
        (["/a/b/c", "/a/b/ca", "/a/b/d"],),
        ["/a/b/c", "/a/b/ca", "/a/b/d"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().removeSubfolders(*inputs)
    assert output == expected
