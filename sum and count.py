def count_positives_sum_negatives(arr):
    if arr==[] or arr==[0,0]:
        return []
    else:
        sum=0
        count=0
        for i in arr:
            if i>0:
                count+=1
            else:
                sum+=i
        return [count,sum]