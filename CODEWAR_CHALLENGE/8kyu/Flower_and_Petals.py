def how_much_i_love_you(nb_petals):
    # Danh sách các cụm từ thể hiện tình cảm tương ứng với số hoa bị ném
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    
    # Tính phần dư khi số hoa bị ném chia cho số lượng cụm từ
    remainder = nb_petals % len(phrases)
    
    # Trả về cụm từ tương ứng với phần dư - 1 (để phù hợp với chỉ số của danh sách)
    return phrases[remainder-1]

# Ví dụ: nếu nb_petals là 7, kết quả sẽ là "I love you".
# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python