

'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

height = [7,5,6,3,5,4,7,8,2,1,6,5,4,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
#Output: 49

#AREA = max height between containers x width

def maxArea(height):
        R_p=len(height)-1
        L_p=0
        maxA=0
        dist=0
        while L_p<=R_p:
            # print(f'left pointer:{height[L_p]} right pointer: {height[R_p]} , pointer distance:{R_p-L_p}')

            #CALCULATE AREA, MIN HEIGHT OF A POINTER VALUE X DISTANCE
            dist=R_p-L_p
            maxH= min(height[L_p], height[R_p])
            area= maxH * dist
            # print(f'maxH:{maxH} area:{area}')
            maxA=max(area, maxA)

            
            #MOVE SMALLER POINTER
            if height[L_p]<height[R_p]:
                L_p+=1
            else:
                R_p-=1
        return maxA

print(maxArea(height))