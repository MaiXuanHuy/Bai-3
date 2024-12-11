print("Mai Xuân Huy")
print("MSSV:235752021610062")
def get_sum(*num):
    tmp=0
    # duyệt các tham số
    for i in num:
        tmp +=i
    return tmp
result = get_sum(1,2,3,4,5)
print(result)
