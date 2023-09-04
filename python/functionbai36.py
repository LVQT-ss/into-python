# đệ quy 
def cal_sum (lst ):
    if not lst:
        return 0 
    else:
        return lst[0] + cal_sum(lst[1:])
    
print(cal_sum([1,2,3,4]))
print(cal_sum([1,2,3,4,5]))
print(cal_sum([]))

def cal_s(lst):
     idx0 , *r = lst 
     return idx0 if not r else idx0 +cal_s(r)
print(cal_s([[1,2],[3,4]]))


def cal_sum(lst):
    if not lst: return 0
    return call_cal_sum(lst)
def call_cal_sum(lst):
     return lst[0] + cal_sum(lst[1:])
print(cal_s([[1,2],[3,4]]))