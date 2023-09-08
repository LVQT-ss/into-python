def find_difference(a, b):
    # thể tích của hình thứ nhất 
    volume_a = a[0] * a[1] * a[2]
    # thể tích của hình thứ 2 
    volume_b = b[0] * b[1] * b[2]
    # chênh lệch
    diff = volume_a - volume_b
    # nếu như chênh lệch bé hơn 0 ( là số âm ) thì chênh lệch nhân với số âm để trả về 1 số dương phù hợp 
    if diff < 0:
        return diff* -1 
    # còn lại thì trả đúng về số dương chính xác 
    return diff

# chương trình này là đang xét về độ chênh lệch của hai hình hộp chữ nhật được truyền vào bởi 2 danh sách 
# đầu tiên thì bạn tính thể thích của hình hộp thứ nhất và sau đó trừ đi thể tích của hình hộp thứ 2 và in ra số chênh lệch của 2 hình hộp 
