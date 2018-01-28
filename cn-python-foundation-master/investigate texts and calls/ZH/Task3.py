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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。


第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
#

# 第一部分

def from_Bangalore_landline(call_list):
    '''
    找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀
    :param list: 电话记录
    :return: 区号和移动前缀的集合
    '''
    from_Bangalore_set = set()
    for record in call_list:
        if record[0][1:4] == "080": # 主叫为班加罗尔的固定电话
            if record[1][0] == "(":   # 被叫号码是固定电话，取区号
                area_code = record[1].find(")")
                from_Bangalore_set.add(record[1][1:area_code])
            if record[1][0] in ['7', '8', '9']: # 被叫号码是移动电话，取前四个数字
                from_Bangalore_set.add(record[1][:4])
    return sorted(list(from_Bangalore_set))  # 对结果排序

print('The numbers called by people in Bangalore have codes:')
for r in from_Bangalore_landline(calls):   # 逐行打印
    print(r)

# 第二部分

def count_Bangalore(call_list):
    '''
    统计由班加罗尔固话打往班加罗尔的电话所占比例
    :param call_list: 通话记录
    :return: 返回百分比
    '''
    m = 0  # 所有(080)拨出的通话计数
    n = 0  # 所有080)拨出，并且打往(080) 的通话计数
    for record in call_list:
        if record[0][1:4] == "080":
            m = m + 1
            if record[1][1:4] == "080":
                n = n + 1
    return round(n/m * 100, 2)     # 求百分比，含2位小数
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(count_Bangalore(calls)))