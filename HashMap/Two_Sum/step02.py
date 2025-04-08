class Solution:
    def twoSum(self, nums: List, target: int) -> List:
        hashTable = {}
        n = len(nums)

        # ハッシュテーブルを作る
        for i in range(n):
            hashTable[nums[i]] = i

        # ほしいキーを逆算し、あればnumsのインデックスのペアを出力
        for i in range(n):
            complement = target - nums[i]
            if (complement in hashTable) and (hashTable[complement] != i):
                return [hashTable[complement], i]

        # 解が見つからなかったとき
        return []