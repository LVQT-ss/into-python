def correct_tail(body, tail):
        sub = body[len(body)-len(tail)]
        if sub == tail:
            return True
        else:
            return False
        

print(correct_tail("Fox", "x"))