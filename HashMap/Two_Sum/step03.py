class solution:
    def twoSum(self, nums: List, target: int) -> List:
        KeyToValue = {}

        # ハッシュテーブルにペアの候補があるかサーチする。
        for i, num in enumerate(nums):
            complement = target - num
            if complement in KeyToValue:
                return [i, KeyToValue[complement]]
            else:
                KeyToValue[num] = i

        print('"nums" has no pair corresponding to the "target".')
        raise KeyError
