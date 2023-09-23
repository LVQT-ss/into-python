def find_admin(lst, lang): 
    # your code here
    return [x for x in lst if x['language']== lang and x['githubAdmin']== 'yes']
