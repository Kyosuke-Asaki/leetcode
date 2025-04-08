class Solution:
    def twoSum(self, nums:List, target: int) -> List:
        hash_table = {}
        n = len(nums)

        # ハッシュテーブルを作る
        for i in range(n):
            hash_table[nums[i]] = i

        # ハッシュテーブル内に所望の値があるか
        for i in range(n):
            complement = target - nums[i]
            # 同じ値のペアが解になるケースでは、異なる2つのインデックスを出力する必要がある
            if (complement in hash_table) and (hash_table[complement] != i):
                return [i, hash_table[complement]]

        # 解なしの場合の処理
        return []