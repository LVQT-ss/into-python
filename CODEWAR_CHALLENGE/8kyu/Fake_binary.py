def fake_bin(number_string):
    binary_string = ''  # Khởi tạo chuỗi nhị phân trống để lưu kết quả

    for number in number_string:
        # Duyệt qua từng ký tự số trong chuỗi đầu vào
        if int(number) < 5:
            # Kiểm tra nếu số hiện tại nhỏ hơn 5
            binary_string += '0'  # Thêm '0' vào chuỗi nhị phân
        else:
            binary_string += '1'  # Nếu số lớn hơn hoặc bằng 5, thêm '1' vào chuỗi nhị phân

    return binary_string  # Trả về chuỗi nhị phân kết quả

# Ví dụ:
# fake_bin("12345") sẽ trả về "01111"
# fake_bin("9876543210") sẽ trả về "1111111111"
# https://www.codewars.com/kata/57eae65a4321032ce000002d/solutions/python