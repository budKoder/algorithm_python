import datetime

def solution(a, b):
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

    fm_date = '2016'+ str(a).zfill(2) + str(b).zfill(2)
    st = datetime.datetime.strptime('20160101', '%Y%m%d')
    fm = datetime.datetime.strptime(fm_date, '%Y%m%d')

    idx = 5
    diff = (fm-st).days
    return days[(idx+diff)%7]

a = 5
b = 24
print(solution(a,b))