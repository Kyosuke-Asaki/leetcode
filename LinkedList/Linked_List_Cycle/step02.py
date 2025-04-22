class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        連結リストに循環があるか判定する
        Parameters
        ----------
        head: ListNode
        判定対象の連結リスト。
        """
        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False
