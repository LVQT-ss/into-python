from math import floor

def cost(mins):
    # Tính phần dư khi chia thời gian học cho 30 (số phút trong một nửa giờ)
    # Nếu phần dư này nhỏ hơn hoặc bằng 5, thì gán giá trị "rem" bằng 0, ngược lại gán bằng 1.
    rem = 0 if mins % 30 <= 5 else 1 
    
    # Tính tổng số nửa giờ. Trước tiên, chia thời gian học cho 30 (để biết có bao nhiêu nửa giờ)
    # và sau đó cộng với "rem" để xác định xem có cần phải làm tròn lên gần nửa giờ gần nhất không.
    total = floor(mins / 30) + rem
    
    # Tính giá cho bài học dựa trên quy tắc đã cho:
    # - Nếu thời gian học là dưới 30 phút, thì giá là $30.
    # - Ngược lại, nếu thời gian học lớn hơn 30 phút, thì giá được tính bằng $30 cộng với $(total - 2) * 10".
    #   Điều này xác định giá cho các nửa giờ tiếp theo sau giờ đầu tiên.
    return max(30, 30 + (total - 2) * 10 )

# https://www.codewars.com/kata/589b1c15081bcbfe6700017a/train/python

def cost(mins):
    price = 0
    print (mins)
    while mins > 0:
        if mins <= 65:
            price += 30
            mins -= 65
        elif mins - 65 > 0:
            price += 10
            mins -= 30
    return price