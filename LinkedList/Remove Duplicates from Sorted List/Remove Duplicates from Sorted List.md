## 問題
今回解いた問題：[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

次に解く予定：[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

## step.01
### コード
```Python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return res

```

### 過程
すでにソートされている。前と番号が重複すれば番号とノードを覚えておき、重複が途切れたら覚えておいたノードと新しい番号のノードをつなぐ。
日本語で処理を考える。状態の遷移は以下の通り。

(i)初期：
現在のノードとその番号を控える。
ノードを一つ変えて、番号が重複→(ii)、番号変わった→(iii)

(ii)前と重複した場合：
何もしない。
ノードを一つ変えて、番号が重複→(ii)、番号変わった→(iii)

(iii)番号が変わった場合：
控えておいたノードと現在のノードをつなげる。
現在のノードとその番号を控える。
ノードを一つ変えて、番号が重複→(ii)、番号変わった→(iii)

最後に返すLinkedListは、ノードがheadのときでなければならない。
B.next = C
A.next = B
...
のように、遡って定義する必要がある。これまで通過したノードを全方向リストで保存すれば容易に実現できるが、最後まで行って逆に戻るのはめんどくさそう。
苦肉の策として、これまで通過したノードをディクショナリで記録し、有無の判定だけでも速くする。
ディクショナリはpython3.7以降であれば入れた順序でソートされている。sortedで逆順にソートする計算量はわからないが、とりあえず動かしてみる。
ACまで1時間以上かかった。引き際を間違えたと思うが、勉強と思ってACを目指した。
```Python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_to_node = {}
        current_node = head

        while current_node is not None:
            if current_node.val not in val_to_node:
                val_to_node[current_node.val] = current_node
            current_node = current_node.next
        
        reversed_vals = sorted(val_to_node, reverse=True)
        unique_nodes = None
        for val in reversed_vals:
            current_node = val_to_node[val]
            current_node.next = unique_nodes
            unique_nodes = current_node
        return unique_nodes
```
動かした結果：Runtime 3ms, Memory 17.95MB。変数名がいまいち。

LeetCodeサイト内の解答例。現在ノードとその次のノードの値が等しければ、現在ノードと次の次のノードとをつなげる。
シンプルなやり方なのになぜか思いつかなかった。
```Python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return res
```

## step.02
### コード
二重ループのコードを採用。
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        
        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

```
### 過程

二重ループの解法:
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next

            current = current.next
        return head
```
一重ループでは場合分けを明確に書いて一つ一つ扱うイメージ。
二重ループは場合分けをwhileに受け持ってもらい、valが重複するノードたちをまとめて処理するイメージ。
二重ループのほうが直観的に思える。どちらも時間計算量はO(n)、空間計算量はO(1)。
なおcurrentという単語は別の意味合いを含むので、scopeとかnodeとかを使ったほうが良いらしい。

step1での考察から、再帰的な解法ができそうな気がする。
自力で書くのは難しいため調べてみる。
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 終了条件
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
```
終了条件を満たすまで再帰的に実行する。
再帰的に呼び出し続けると、連結リストのheadがNoneである状態でreturnしてしまっていないのか？
再帰的な書き方は、各ノードに人を立たせて実行してもらうときにどうマニュアルを渡すかを考えると良い、というコメントがあった。
イメージがわかりやすい。再帰呼び出しの挙動はイメージがつくので、後は再帰呼び出し時に連結リストのポインタがどう推移するか整理すればよさそう。
とりあえず後回しにして、二重ループの解法を書けるようにする。

### 参照
https://peps.python.org/pep-0008/#naming-conventions
・英単語の省略形は避ける
https://github.com/ichika0615/arai60/pull/3/files/28df61b2ca99221343677e87772e020872fb1a79#diff-40c411826970ac79885bd91d376b424610f627f9e514b507095c691ec83d22a0
↑いろいろな解法が書いてある。眺める。
```Python3
current = head
while current is not None:
    # DO SOMETHING
    current = current.next
```
はイディオムとして捉える
https://github.com/rieuky/arai60/pull/3

## step.03
### コード
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

```
1回目：0m 47s, 2回目：1m 04s, 3回目: 0m 51s





