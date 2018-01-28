"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

talk_time = {}  # 建立一个字典，并以电话号码为键，以通话总时长为值

def talktime_dict(list):
    '''
    对输入的通话记录列表，进行处理，得出每个号码的通话时间：含拨打电话时间及接听电话时间
    把每个号码的通话时间存入字典
    :param list: 通话记录
    :return: 对通话记录处理后的字典，包含了每个号码的通话总时长。
    '''

    for record in list:
        if talk_time.get(record[0]) is None:  #如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
            talk_time[record[0]] = int(record[3])
        else:                                 #如果键已经存在于字典内，为键所对应的值加上对应数值；
            talk_time[record[0]] += int(record[3])
        if talk_time.get(record[1]) is None:
            talk_time[record[1]] = int(record[3])
        else:
            talk_time[record[1]] += int(record[3])

talktime_dict(calls)  #调用函数，返回号码通话时间的字典

number = max(talk_time,key=talk_time.get)  # 得到通话总时间最长的电话号码

print("{} spent the longest time, {} seconds, on the phone during September 2016".format(number, talk_time[number])) # 输出结果



