# các loại method : class method và static method  
# nếu regualar method có argument đầu tiên tự động đưa vào là đối tượng đó và được phân bởi parameter self thì với class method 
# đầu tiên tự động đưa vào chính lớp gọi phương thức đó hoặc là lớp của đối tượng gọi phương thức đó 
# para nhận này là cls 
class siunhan1: 
    sub_manh=50
    def __init__(self,para_ten,para_vu_khi,para_mausac):
        self.ten = 'siu nhan '+ para_ten
        self.vu_khi= para_vu_khi
        self.mausac= para_mausac 
    @classmethod
    def from_string(cls,s):
        lst = s.split('-')
        new_lst = [ st.strip() for st in lst ]
        ten,vu_khi,mausac = new_lst
        return cls(ten,vu_khi,mausac)

infor_str = ' siu nhan do - kiem - do '
siu_nhan_A = siunhan1.from_string(infor_str)
print(siu_nhan_A.__dict__)

# static method 
class SieuNhan: 
    sub_manh=50
    def __init__(self,para_ten,para_vu_khi,para_mausac):
        self.ten = 'siu nhan '+ para_ten
        self.vu_khi= para_vu_khi
        self.mausac= para_mausac 
    @staticmethod
    def bienhinh():
        print('1,2,3. sieu nhan bien hinh')

siu_nhan = SieuNhan('siu nhan do ','kiem', ' do ')
siu_nhan.bienhinh()