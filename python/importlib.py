# lấy toàn bộ nội dung thư viện decimal 
from decimal import*

# lấy tối đa 30 chữ số phần nguyên và phần thập phân 
getcontext().prec= 30

print(10/3)
print(Decimal(10)/Decimal(3))
