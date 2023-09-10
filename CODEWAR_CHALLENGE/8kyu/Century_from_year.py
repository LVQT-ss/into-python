def century(year):
    # Tính thế kỷ bằng cách chia lấy phần nguyên của năm cho 100
    thoi_ky = year // 100
    
    print(thoi_ky)

    # Kiểm tra nếu năm chia hết cho 100 (năm cuối của một thế kỷ)
    if year % 100 == 0:
        # Trả về giá trị thế kỷ
        return thoi_ky
    
    # Trong trường hợp năm không chia hết cho 100
    else:
        # Trả về giá trị thế kỷ kế tiếp
        return thoi_ky + 1

# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python