class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l):
        if not l:
            return l

        head = ListNode()
        current = head
        for i in l:
            current.next = ListNode(i)
            current = current.next
        return head.next

    @staticmethod
    def to_list(head):
        if not head:
            return head

        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l

    @staticmethod
    def assert_list_equal(head1, head2):
        ohead1 = head1
        ohead2 = head2
        while head1 and head2:
            assert head1.val == head2.val, f"got: {ListNode.to_list(ohead1)}, expected: {ListNode.to_list(ohead2)}"
            head1 = head1.next
            head2 = head2.next
        assert not head1 and not head2, f"got: {ListNode.to_list(ohead1)}, expected: {ListNode.to_list(ohead2)}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(l):
        if not l:
            return None

        root = TreeNode(l[0])
        queue = [root]
        i = 1
        while i < len(l):
            node = queue.pop(0)
            if i < len(l) and l[i] is not None:
                node.left = TreeNode(l[i])
                queue.append(node.left)
            i += 1
            if i < len(l) and l[i] is not None:
                node.right = TreeNode(l[i])
                queue.append(node.right)
            i += 1

        return root

    @staticmethod
    def to_list(root):
        if not root:
            return []

        l = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                l.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                l.append(None)
        while l and l[-1] is None:
            l.pop()
        return l
