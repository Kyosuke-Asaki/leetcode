## 問題
今回解いた問題：[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)

次に解く予定：[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

## step.01
### コード
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next

```
### 過程
一見して一つ前の問題と変わらないように見える。
cycleの起点を示すため、前より難しくなってる？
前と同じようにやると、同じノードが検出できても、前に通った時のインデックスがわからない。
ハッシュテーブル使えばうまくいく？
visited_node_to_iを途中までvisited_nodes_to_iと書いていて、typoでエラーしがち。

あれ、indexでなくnodeを返せば良いのか…であれば簡単。
問題文にもnodeを返せと書いてある。
供養のため、インデックスをprintするコードを残しておく。
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node_to_i = {}
        node = head
        i = 0
        while node:
            if node in visited_node_to_i:
                print(visited_node_to_i[node])
                return node
            if node is None:
                return None
            visited_node_to_i[node] = i
            node = node.next
            i += 1

```

nodeを返すコードは、
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return node
            if node is None:
                return None
            visited_nodes.add(node)
            node = node.next

```

## step.02
### コード
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        visited_nodes = set()
        while node is not None:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None

```
### 過程
フロイドの循環検出法と比較。
https://github.com/M-Satou955/leetcode_arai60/pull/3/files/d434989ba26c80b02cecffa96420555a8a05512f
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        # サイクルが検出された時点でループ処理を終了
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        # サイクルが存在せず上のwhileが終了した場合
        if fast.next is None or fast.next.next is None:
            return None

        # fastを最初に移動させてもう一度追いかけることでサイクルの開始点を検出。
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

```

自分で書き直したもの
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
        
        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return fast

```
メモリ、19.64MB、 Runtime 52ms
空間計算量はO(1)、空間計算量はO(N)。
ループの存在を判定したのち、存在する場合はループ開始点を探索。
探索開始時、fastは初期ノードから、slowは存在判定終了時のノードからスタート。
フロイドの循環検出法に忠実な書き方のようだ。
個人的にはset()を使った書き方のほうがわかりやすい。
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        visited_nodes = set()
        while node is not None:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None

```
メモリ、20.04MB、Runtime 48ms
空間計算量はO(N)、時間計算量はO(N)
空間計算量の制限が厳しければフロイドの方法で、そうでなければset()を使った解法を選べれば良さそう。
空間計算量と時間計算量を自然と思い浮かべられるようにしたい。
### 参照
フロイドの循環検出法：
https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E3%81%AE%E5%BE%AA%E7%92%B0%E6%A4%9C%E5%87%BA%E6%B3%95

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.jfs03xpyyrfl

while-else:(set()を使う場合が、ループ終了時の処理が煩雑でないので使ってない)
https://discord.com/channels/1084280443945353267/1221030192609493053/1225674901445283860

## step.03
3回とも1分半。set()を使った解法を採用。
```Python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        visited_nodes = set()
        while node is not None:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None

```
