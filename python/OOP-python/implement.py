# tạo lớp kế thừa 
class sieunhan: 
    suc_manh = 50 
    def __init__(self,para_ten,para_vu_khi,para_mausac):
        self.ten = 'siu nhan '+ para_ten
        self.vu_khi= para_vu_khi
        self.mausac= para_mausac 

class sieunhangao(sieunhan):
    suc_manh = 40
    def __init__(self,para_ten,para_vu_khi,para_mausac,para_su_thu):
        #self.ten = 'siu nhan '+ para_ten
        #self.vu_khi= para_vu_khi
        #self.mausac= para_mausac 
        #self.su_thu= para_su_thu
        # cách ngắn hơn dùng super khả năng tái sử dụng code 

        super().__init__(para_ten,para_vu_khi,para_mausac) 
        self.su_thu= para_su_thu
        # kế thừa phương thức 
        
kteam_do = sieunhangao('do ', '  cung ', ' do ','tho beu ')
print(kteam_do.__dict__)
print(kteam_do.suc_manh) 