class Solution:
  def sortPeople(self, names, height):
        for i in range(len(height)-1):
           for j in range(len(height)-i-1):
                if height[j]<height[j+1]:
                    height[j],height[j+1]=height[j+1],height[j]
                    names[j],names[j+1]=names[j+1],names[j]  
        return names   
    
print(Solution().sortPeople(["Mary", "John","Emma"],[180,165,170]))
