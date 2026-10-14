class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        res=0
        l,r=0,n-1
        while l<r:
            count=r-l
            area=min(height[l],height[r])*count
            res=max(area,res)

            if height[l]>height[r]:
                r-=1
            elif height[r]>height[l]:
                l+=1
            else:
                r-=1
        
        return res
        