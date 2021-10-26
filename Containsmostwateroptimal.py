class Solution:
    def maxArea(self, height: List[int]) -> int:
        #res = 0
        #for l in range(len(height)):
        #    for r in range(l + 1, len(height)):
        #       area = (r - l) * min(height[l] , height[r])
        #       res = min(res, area)
        #return res

        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(area,res)
            if height[l]  < height[r]:
                l = l+1
            else:
                r = r-1
        return res
            
