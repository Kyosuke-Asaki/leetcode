from typing import Any

class Node(object):
    def __init__(self, data: Any, next_node = None):
        self.data = data # データ
        self.next = next_node # 次のNodeを指す参照変数(ポインタ)



class LinkedList(object):
    def __init__(self, head = None) -> None:
        self.head = head # インスタンス化した時にNoneをいれておく。

    def append(self, data: Any) -> None:  # リストへの追加
        new_node = Node(data)  # 追加する要素をNodeクラスを使ってインスタンス化
        if self.head is None:  # headがNoneの場合、今回追加する要素は先頭になるため、self.headへ代入
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:  # whileは.nextがNoneになると抜けるので一番最後まで繰り返す
            last_node = last_node.next

        last_node.next = new_node  # 最後の要素のポインタに今回追加するインスタンスを追加する


    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:  # 削除したい要素が先頭の場合
            self.head = current_node.next  # 先頭を次のオブジェクトにする
            current_node = None  # current_nodeをNodeにする。ガベージコレクションを待ってもいいけど念のため。
            return

        previous_node = None

        # 削除するデータがあるまで、先頭から探す
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:  # current_nodeがNoneになった場合、削除する値はリストにないのでrerutn
            return

        # 削除する要素があったら
        previous_node.next = current_node.next  # currentは削除されるため、その前のオブジェクトにcurrentのポインタを代入
        current_node = None  # ガベージコレクションを待ってもいいけど念のため。

# よくある解答
class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle

# 愚直にやってみる
class Solution(object):
    def hasCycle(self, head):
        max_num_of_nodes = int(1e4+1)

        nodes = []
        head_next = head
        for i in range(max_num_of_nodes):
            if head_next in nodes:
                return True
            elif head_next is None:
                return False
            else:
                nodes.append(head_next)
                head_next = head_next.next
        print("ノードの数が多すぎるため停止しました")
        raise TypeError

if __name__ == '__main__':

    # testcase1 自力でLinkedListを作ってみる
    node1 = Node(data=2) #最初のノード
    node2 = Node(data=-4, next_node=node1)
    node3 = Node(data=0, next_node=node2)
    node4 = node1
    node4.next = node3
    node5 = Node(data=3, next_node=node4)

    node5_i = node5
    for i in range(10):
        print(node5_i.data)
        node5_i = node5_i.next

    # output
    # 3
    # 2
    # 0
    # -4
    # 2
    # 0
    # -4
    # 2
    # 0
    # -4

    pos = 1
    sol = Solution()
    print(sol.hasCycle(node5))
