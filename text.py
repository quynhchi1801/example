# viết chương trình tính tổng các số từ 1 đến n là giá trị được nhập từ bàn phím
n = int(input("nhập n:"))

def tinhtong(n):
    s = 0
    for i in range(1,n,1):
        s = s + i
    return s
print("kết quả:",tinhtong(n))