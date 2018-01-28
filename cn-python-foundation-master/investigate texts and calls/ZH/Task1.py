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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

def count_unique_numbers(list):
    '''
    统计给定列表中唯一的电话号码的个数
    :param list: 通话记录
    :return: 唯一号码的个数
    '''
    unique_numbers_set = set()   #号码集合
    for record in list:
        unique_numbers_set.add(record[0])  # 这是短信发送号码，或者主叫电话号码
        unique_numbers_set.add(record[1])  # 这是短信接收号码，或者被叫电话号码
    return len(unique_numbers_set)

#合并短信和通话记录，调用已定义的统计函数，计算唯一号码的个数
print("There are {} different telephone numbers in the records. ".format(count_unique_numbers(texts + calls)))