class Solution:
    def twoSum(self, num: list[int], target: int) -> list[int]:
        low,high=0,len(num)-1
        while low<high:
            sum=num[low]+num[high]
            if sum==target:
                return [low+1,high+1]
            if sum<target:
                low+=1
            else:
                high-=1
            
        return []
        