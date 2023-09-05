# class là  một bản mẫu, khuôn mẫu, khai báo các thuộc tính và phương thức để miêu tả để từ đó tạo ra những object 
# object có thể ghi là instance | objects are instances of types 42 is an instance of the type int is equivalent to 42 is an int object 
# class là một kiểu dữ liệu tự định nghĩa 

class Siunhan:

    pass 


Siu_nhan_a = Siunhan()

Siu_nhan_a.ten = ' SIÊU NHÂN ĐỎ '
Siu_nhan_a.vu_khi= ' KIẾM '
Siu_nhan_a.mau_sac=  ' ĐỎ  '


print('ten cua siu nhan la : ',Siu_nhan_a.ten )
print('sieu nhan mau',Siu_nhan_a.mau_sac)
print('su dung vu khi :', Siu_nhan_a.vu_khi)


# contructor initialize method 
# lưu dấu gạch '_' bắt đầu và kết thúc
# # giải thích một vài điều đây là tên hàm được quy ước nếu bạn đặt tên hàm như vậy bạn mặc định nói với chương trình đây là một contructor 
# $ trong python một số hàm trong lớp sẻ được tự động gọi khi ta khai báo một đối tượng và contructor là một trong những hàm đó 
# từ khóa self hay cục thể đây là parameter self là một quy uốc , bạn có thể dùng một từ khóa khác. tuy nhiên từ trước với giờ chưa ai dùng từ khác ngoài self 
# nên sử dụng từ khóa self 
# self ý nghĩa là đối tượng đó 
print('--------------contruc tor=----------- ')
class siunhan1: 
    def __init__(self,para_ten,para_vu_khi,para_mausac):
        self.ten = 'siu nhan '+ para_ten
        self.vu_khi= para_vu_khi
        self.mausac= para_mausac 
    def xin_chao(self):
        return' xin chao ta chinh la ' + self.ten

siunhan_A = siunhan1('do','kiem','do')
print('ten cua siu nhan la ',siunhan_A.ten)
print('siu nhan mau : ' ,siunhan_A.vu_khi)
print('su dung vu khi ',siunhan_A.mausac)

print(siunhan_A.xin_chao())
print(siunhan1.xin_chao(siunhan_A))