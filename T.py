from collections import deque

lone = [0,5,300,40,55,159,44,133,12,16,15,111,1888,20,15]

def merge_sort(glist):
    if len(glist)<2:
        return glist
    mid = len(glist)//2
    right= glist[ int(mid):]
    left = glist[:int(mid)]
    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):

    left= deque(left)
    right=deque(right)
    merged=[]
    
    for _ in range( len(left) + len(right)):
        if len(left)<1:                  # FOR CASES WHEN LISTS GET DELETED
            merged.append(right.popleft())
            continue
        elif len(right)<1:
            merged.append(left.popleft())
            continue

        # COMPARE THE LEFT MOST NUMBER IN BOTH LISTS, DELETE AND PUSH THE SMALLER ONE IN THE MERGED LIST. REPEAT UNTIL LISTS ARE DELETED
        if left[0]<right[0] and len(left)>0 and len(right)>0:
            merged.append(left.popleft())
        elif right[0]<left[0] and len(left)>0 and len(right)>0:
            merged.append(right.popleft())

    return merged
    
print(merge_sort(lone))

