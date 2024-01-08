class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_ListNode(l):
        if not l:
            return l

        head = ListNode()
        current = head
        for i in l:
            current.next = ListNode(i)
            current = current.next
        return head.next

    @staticmethod
    def ListNode_to_list(head):
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
            assert (
                head1.val == head2.val
            ), f"got: {ListNode.ListNode_to_list(ohead1)}, expected: {ListNode.ListNode_to_list(ohead2)}"
            head1 = head1.next
            head2 = head2.next
        assert (
            not head1 and not head2
        ), f"got: {ListNode.ListNode_to_list(ohead1)}, expected: {ListNode.ListNode_to_list(ohead2)}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_TreeNode(l):
        if not l:
            return None

        def rec(i):
            if i >= len(l) or l[i] is None:
                return None
            node = TreeNode(l[i])
            node.left = rec(2 * i + 1)
            node.right = rec(2 * i + 2)
            return node

        return rec(0)
