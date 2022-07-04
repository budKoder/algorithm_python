def solution(new_id):
    answer = ''
    # step1
    new_id = new_id.lower()
    # step2
    slist = set(new_id)
    for s in slist:
        if not s.isdigit() and not s.isalpha() and s not in ['-','_','.']:
            new_id = new_id.replace(s,'')
    # step3
    while new_id.count('..')>0:
        new_id = new_id.replace('..','.')
    # step4
    new_id = new_id.strip('.')
    # step5
    if len(new_id) ==  0:
        new_id = 'a'
    # step6
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    # step7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id

new_id ="abcdefghijklmn.p"
solution(new_id)