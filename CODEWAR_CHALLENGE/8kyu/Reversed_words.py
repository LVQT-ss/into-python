def reverse_words(s):
    # 'foo bar' => ['foo','bar']
    words = s.split(' ')
    # ['bar','foo']
    reversed_words= words[::-1]
    return ' '.join(reversed_words)