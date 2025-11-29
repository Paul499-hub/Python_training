nums = [1]

target = 1


def search(nums, target):
        

            
        i=0
        mid=len(nums)//2
        l=0
        r=len(nums)-1


        if nums[mid]==target:
            print(f'mid found:[{mid}], {nums[mid]}')
            return mid
        if nums[l]==target:
            print(f'l found:[{l}], {nums[l]}')
            return l
        if nums[r]==target:
            #print(f'r found:[{r}], {nums[r]}')
            return r
        
        if len(nums)<4:
            return -1

        while l<r and (r-l)>=2:
            i+=1
            if i>10:
                #print(f'EMERGENCY BREAK')
                break
            temp=''
            mid=(r+l)//2
            
            if nums[mid]==target:
                print(f'mid found:[{mid}], {nums[mid]}')
                return mid
            if nums[l]==target:
                print(f'l found:[{l}], {nums[l]}')
                return l
            if nums[r]==target:
                #print(f'r found:[{r}], {nums[r]}')
                return r

            # FIND SORTED SIDE< CHECK IF ITS IN THE RANGE TO BE THERE
            if nums[l]<nums[mid]:
                temp+='S'
            else:
                temp+='U'
            if nums[mid]<nums[r]:
                temp+='S'
            else:
                temp+='U'

            #print(f'sort:{temp}')

            if temp=='SU': # LEFT SIDE SORTED CHECK IF IT IS THERE, IF NOT ASSUME ITS ON RIGHT SIDE
                #print(f'LEFT SIDE SORTED')
                if nums[l]<target<nums[mid]:
                    #print(f'TARGET IS ON THIS SIDE')
                    r=mid
                else:
                    #print(f'TARGET IS ON unsorted SIDE')
                    l=mid+1
            elif temp=='US':
                #print(f'RIGHT SIDE SORTED')
                if nums[mid]<target<nums[r]:
                    #print(f'TARGET IS ON THIS SIDE')
                    l=mid+1
                else:
                    #print(f'TARGET IS ON unsorted SIDE')
                    r=mid
            elif temp=='SS':
                #print(f'BOTH SORTED')
                if target>nums[mid]:
                    l=mid+1
                else:
                    r=mid

        #print(f'l:{l} r:{r}')
        if nums[mid]==target:
            print(f'mid found:[{mid}], {nums[mid]}')
            return mid
        if nums[l]==target:
            print(f'l found:[{l}], {nums[l]}')
            return l
        if nums[r]==target:
            #print(f'r found:[{r}], {nums[r]}')
            return r
        return -1
    
            

print(search(nums,target))



    

def verify_trg(target,mid,l,r,nums):
    print(f'vt')
    if nums[mid]==target:
        print(f'mid found:[{mid}], {nums[mid]}')
        return mid
    if nums[l]==target:
        print(f'l found:[{l}], {nums[l]}')
        return l
    if nums[r]==target:
        #print(f'r found:[{r}], {nums[r]}')
        return r

# ASSUME LAST NUMBER iS ALWAYS LOWER THAN FIRST 




