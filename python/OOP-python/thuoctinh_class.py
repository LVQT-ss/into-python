

class siunhan: 
    stt= 1;
    so_thu_tu = 1 
    suc_manh = 50 
    def __init__(self,para_ten,para_vu_khi,para_mausac):
        self.ten = 'siu nhan '+ para_ten
        self.vu_khi= para_vu_khi
        self.mausac= para_mausac 

        self.stt = siunhan.so_thu_tu 
        siunhan.so_thu_tu+=1
 

siunhan_A = siunhan('do','kiem','do') 
siunhan_B = siunhan('vang','bua','vang') 

print(siunhan.suc_manh)
print(siunhan_B.suc_manh)

print(siunhan_A.stt)
print(siunhan_B.stt)
print(siunhan.so_thu_tu)



class siunhan: 
    suc_manh = 50 
    def __init__(self,para_ten,para_vu_khi,para_mausac):
        self.ten = 'siu nhan '+ para_ten
        self.vu_khi= para_vu_khi
        self.mausac= para_mausac 
    def xin_chao(self):
        print(' xin chao ta chinh la ', self.ten)
        print('suc mah cua ta la',self.suc_manh)

siu_nhanA  = siunhan('do ', ' kiem ', ' do ')

siu_nhanA.xin_chao()