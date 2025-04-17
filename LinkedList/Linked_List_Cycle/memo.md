初心者はLinkedListから解いたほうが良いとアドバイスを受け、2問目として取り組む。

## Step.01
Linked Listに触れたことがなかったため、headの挙動をprintして試してみる。
わからないので答えを見る。

答えを動かしてみたものの、Linked Listがそもそもよくわからない。
https://qiita.com/tsudaryo1715/items/12c4848028716ab015bb
この記事を読んでなんとなく理解する。

単連結リストの挙動
Sai_Varma氏の解答をコピペし、print(slow), print(fast)の出力結果を見ながらなんとなく挙動を理解。
slow == fastはどんな場合にTrueなのか？slow.val == fast.valの場合ではないと思うが。

LinkedListを手元で動かしてみる。
https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/linked_list
このサイトのコードを流用。
いまいち動作がわからない。LinkedList.show()したときに小さい値順に表示されており、意図した動作でないように思える。
cycleが生じるLinkedListってなんだ？

Nodeのインスタンスnode1をnode2.nextとすることで、node2 -> node1というリンク構造になることを理解。
参照渡しを理解していれば、この構造は簡単に気づけたと思われる。
(pythonでポインタをどうやって表現するのか理解してなかった)

cycle構造がどうやってできるのかやはりわからない。
nodeのインスタンスで自力でcycleを作ってみて、cycleを含むLinkedListの構造が理解できた気がする。

愚直な解法を考えてみる。ACできた。

## step2
他の解法にも触れる。slowとfastを使った解法を試してみる。
Runtimeが50msだった。自分の愚直な解法が904ms。
これだけ差があれば、速い解法のほうがよさそう。
愚直な解法では反復回数が増えるにつれてリストが長くなっていく。最悪O(n^2)?
Listでなくsetで、過去に訪れたnodeを覚えておく解法があった。

https://github.com/M-Satou955/leetcode_arai60/pull/2/files/8b9f1fd3484b145b29957f3c3fe6f9f7a8602253#diff-c0aa968adfe6bc16cd54711ca6c64330e1341395b612e35c57dbe0d9fd9d2c73

こちらを試すと50ms。わかりやすい内容で速いのでこれにする。
※なぜはやいか：https://qiita.com/kitadakyou/items/6f877edd263f097e78f4

ハッシュ値を参照しているため。ハッシュ法についてもググってみた。
https://daeudaeu.com/hash-search/

while文だと終了条件がわかりにくいので、forとifで書く。
反復回数に上限を設けたほうが良いと思ったが、外からいじれるようにしたほうが良いのか？
迷ったが、上限の回数を引数とした。
やはりwhile文のほうがシンプルになるし、無限ループにならないことは保証されているので、whileで書く。

## step3
1回目：5分ほど。

2回目：2分半

3回目：2分

3回目あたり、半ば丸暗記でコードを再現しているように思えてきた。
時間を置いても再現できるか確かめたい。




