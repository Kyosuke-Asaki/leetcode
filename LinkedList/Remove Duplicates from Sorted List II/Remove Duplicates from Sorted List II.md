## 問題
今回解いた問題：[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

次に解く問題：[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

## step1
### コード
```Python3
class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current:
            is_duplicate = False
            while current.next and current.val == current.next.val:
                is_duplicate = True
                current = current.next
            
            if is_duplicate:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next

        return dummy.next
```

### 過程
5分ほど考える：

前の問題との差分は、重複したものを1つ残らずすべて消すこと。
重複の有無を判別して一個ずつ消していくと、最後の1個を消すのに苦労する。
重複した回数をカウントして、重複が1以上なら消す？
重複に気づいたときに、2つ前とつなげる必要がある。
最初の値が消す対象だったら、2つ前、という概念がない。ダミーを作るか？

- ダミーのノード作成
- 重複に気づいたら、2つ前のノードを記憶しておく
- 重複が途切れたら、記憶しておいたノードと、途切れた直後のノードをつなげる
- 全部処理が終わったら、最初のダミーのノードだけ除いて出力

ここまでの発想で10分ほど。
さらに15分ほどかけて書いてみる。
コードで書こうとして躓いたので、言葉でフローを書いてみる。
- ダミーのノードを作成
- 1個先と2個先の存在をチェックし、1個先と2個先の値が重複しているか確認。
- 重複してたら、今のノードを覚えておく。重複がなくなるまでノードを進める。

1h弱考えたものの、行き詰ってきたので、動かないコードだけ書いておいて答えを見る。
```Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 最初のノードをダミーとして設定
        node = dummy = ListNode(val=-101, next=head)
        while node is not None:
            temporary = node
            while node.next is not None and node.next.next is not None and node.next.val == node.next.next.val:
                node = node.next
            else:
                if node.next is None:
                    temporary.next = None
                    return dummy.next
                else:
                    temporary.next = node.next.next
            node = node.next
        return dummy.next

```

解答例のコードを読む。
```Python3
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            is_duplicate = False

            while current.next and current.val == current.next.val:
                is_duplicate = True
                current = current.next

            if is_duplicate:
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next
```
基本は前の問題と同じ。二重ループで解き、内側のループは重複のまとまりに対する処理。
is_duplicateというフラグを持っておいて、1回でもwhile文を通過したら記録されるようにする。
currentとcurrent.nextは内側のループでも更新されるが、previousはそのまま。
フラグがあれば、previousとcurrent.nextをつなぐことで、重複分をショートカットする。

手作業でも、重複したか確認すると思う。手作業のイメージをうまくコードに落とし込めていなかった。
また、書く処理としては「1つ前と今のノードを保持し、次のノードを見る」ことと「今のノードと次のノードを保持し、次の次のノードを見る」ことは等価であるが、認知負荷が全然違う。
「2個先を見る」と考えたため、認知負荷が高くなり、コードがうまく書けなかった？

## step2
### コード
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        if head.val == head.next.val:
            val = head.val
            while head is not None and head.val == val:
                head = head.next
            return self.deleteDuplicates(head)

        head.next = self.deleteDuplicates(head.next)
        return head

```

### 過程
https://github.com/garunitule/coding_practice/pull/4/files/2079c17c2d7b65ae67e8b4874d5fa460ceb38104#diff-e3bf5d4b80d8d39cd7a39e0f6717ab977bb46ce042e03b60ce14e507253e1bbd
より。
- フラグを使わない書き方：
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        tail = dummy
        node = head
        while node is not None and node.next is not None:
            val = node.val
            if node.next.val != val:
                tail = node
                node = node.next
                continue
            while node is not None and node.val == val:
                node = node.next
            tail.next = node
        return dummy.next
```
is_duplicateというフラグが必要だったのは、
(i)重複したノードを最後まで進む処理→(ii)途中のノードをスキップする処理
という順番で処理していたから。これを逆にすることで、フラグが不要になっている。
(i')重複してない場合にtailを更新→(ii')重複してたらtailを更新せずノードを進める
という順番。

- 再帰を使う方法：
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        if head.val == head.next.val:
            val = head.val
            while head is not None and head.val == val:
                head = head.next
            return self.deleteDuplicates(head) #(i)
        else:
            head.next = self.deleteDuplicates(head.next) #(ii)
            return head
```
例：[1,2,3,3,4,4,5]
関数呼び出し
    →(ii)へ、[2,3,3,4,4,5]を入れる (head=[1,2,3,3,4,4,5])
        →(ii)へ、[3,3,4,4,5]を入れる(head=[2,3,3,4,4,5])
            →(i)へ、[4,4,5]を入れる
                →(i)へ、[5]を入れる
                ←[5]を出力
            ←[5]を出力
        ←head.next = [5]とつなげて、[2,5]を出力
    ←head.next = [2,5]とつなげて、[1,2,5]を出力　(これが最後のreturn)

同じvalのまとまりを処理するのが関数呼び出しからreturnまで。まとまりのノード数が複数or1の場合で分岐。
コードがすっきりしていて読みやすく見える。
なお、再帰を使わない方法、再帰を使う方法も、ともに時間計算量O(n)、空間計算量O(1)である。
よって今回は再帰を使うコードとする。前の問題では再帰を使わない処理を採用したが、実際のコードでは再帰を使う/使わないは統一したほうが良いだろう。
elseのインデントは下げたほうがわかりやすそう。

https://github.com/tokuhirat/LeetCode/pull/4/files/2e79d596cafd3f44c28e1062fa4d41dde2e9098e#diff-11f6d4802fac885b81d71470b90450c4795a80c8c69b149e99c5ceb9a41ced2b
- 命名はtailよりもcheckedのほうがわかりやすい

https://github.com/tokuhirat/LeetCode/pull/4/files/2e79d596cafd3f44c28e1062fa4d41dde2e9098e
- 切断しておいてつなぐ：新しく空の連結リストを用意して、解と確定したノードをつないでいく
- つないでおいて切断する：引数の連結リストから、重複する分をスキップして解の連結リストを作る。
自覚的に区別するなら、今まで書いていたコードは後者に相当する。前者バージョンでコードを書き直してみる。
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(val=-101, next=None)
        tail = dummy
        node = head
        while 1:
            if node is None or node.next is None:
                tail.next = node
                return dummy.next                
            val = node.val
            if node.next.val != val:
                tail.next = ListNode(val=node.val, next=None)
                node = node.next
                tail = tail.next
                continue
            while node is not None and node.val == val:
                node = node.next

```
うまく書けてはいない気がする。[while-elseの変形](https://discord.com/channels/1084280443945353267/1221030192609493053/1225674901445283860
)も検討はしたものの、continueがあるためややこしい。

## step3
### コード
```Python3
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        if head.val == head.next.val:
            val = head.val
            while head is not None and head.val == val:
                head = head.next
            return self.deleteDuplicates(head)
        
        head.next = self.deleteDuplicates(head.next)
        return head
```
1回目　4分ほど。途中でわからなくなったので仕切り直し。
2回目 3分。
3回目　1分40秒
4回目 1分42秒。

