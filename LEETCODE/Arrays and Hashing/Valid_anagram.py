class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        # Kiểm tra nếu độ dài của hai chuỗi không bằng nhau, thì chúng không thể là anagram
        if len(s) != len(t):
            return False
        
        # Khởi tạo từ điển để đếm số lần xuất hiện của các ký tự trong chuỗi s và t
        countS, countT = {}, {}

        # Lặp qua từng ký tự trong chuỗi s và t
        for i in range(len(s)):
            # Cập nhật số lần xuất hiện của ký tự s[i] trong chuỗi s
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # Cập nhật số lần xuất hiện của ký tự t[i] trong chuỗi t
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Lặp qua từng ký tự trong chuỗi s
        for c in countS:
            # So sánh số lần xuất hiện của ký tự c trong chuỗi s và t
            if countS[c] != countT.get(c, 0):
                return False
        
        # Nếu sau tất cả kiểm tra, chuỗi s và t có cùng số lần xuất hiện của các ký tự, thì chúng là anagram
        return True
    
    # class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        # Kiểm tra nếu độ dài của hai chuỗi không bằng nhau, thì chúng không thể là anagram
        if len(s) != len(t):
            return False
        
        # Khởi tạo từ điển để đếm số lần xuất hiện của các ký tự trong chuỗi s và t
        countS, countT = {}, {}

        # Lặp qua từng ký tự trong chuỗi s và t
        for i in range(len(s)):
            # Cập nhật số lần xuất hiện của ký tự s[i] trong chuỗi s
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # Cập nhật số lần xuất hiện của ký tự t[i] trong chuỗi t
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Lặp qua từng ký tự trong chuỗi s
        for c in countS:
            # So sánh số lần xuất hiện của ký tự c trong chuỗi s và t
            if countS[c] != countT.get(c, 0):
                return False
        
        # Nếu sau tất cả kiểm tra, chuỗi s và t có cùng số lần xuất hiện của các ký tự, thì chúng là anagram
        return True
# https://leetcode.com/problems/valid-anagram/


# 1 dòng 
# return Counter(s) == Counter(t)

# soution with O(1) complex 
#return sorted(s) == sorted(t) ( tự chỉ ra cách mà nó sort )
# use shorted and compare each O(nlongn)