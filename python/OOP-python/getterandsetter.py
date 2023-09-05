# getter 
class kter:
    def __init__(self,ho,ten):
        self.ho = ho 
        self.ten = ten 
        self.email = ho + '-'+ ten + '@kteam.com'
    @property
    def ho_va_ten(self):
        return '{}{}'.format(self.ho,self.ten)
    @property
    def emails(self):
        return self.ho + '-'+ self.ten+'@kteam.com'
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi, ten_moi= ten_moi.split(' ')
        self.ho= ho_moi
        self.ten= ten_moi
kter_a = kter('tran ',' long dep trai ')

kter_a.ho= 'nguyen'
kter_a.ten='giau'
print(kter_a.ho)
print(kter_a.ten)
print(kter_a.emails)
print(kter_a.ho_va_ten)
# dùng thêm @ property để có thể đặt trùng và không cần phải gọi method 
print('dùng setter ')
kter_a.ho_va_ten= 'nguyen giau'
print(kter_a.ho_va_ten)

# deleter 

class kter:
    def __init__(self,ho,ten):
        self.ho = ho 
        self.ten = ten 
        self.email = ho + '-'+ ten + '@kteam.com'
    @property
    def ho_va_ten(self):
        return '{}{}'.format(self.ho,self.ten)
    @property
    def emails(self):
        return self.ho + '-'+ self.ten+'@kteam.com'
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi, ten_moi= ten_moi.split(' ')
        self.ho= ho_moi
        self.ten= ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print('da xoa')

kter_a = kter('tran ',' long dep trai ')

kter_a.ho_va_ten= 'nguyen giau'
print(kter_a.ho_va_ten)
del kter_a.ho_va_ten