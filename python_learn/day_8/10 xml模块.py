# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/5 13:45
@ file:     10 xml模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# xml是实现不同语言或程序之间进行数据交换的协议，和json类似
import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')  # 形成树形结构
root = tree.getroot()  # 得到树的根系
print(root)  # <Element 'data' at 0x03127A78>

# 循环打印
for i in root:
    print(i)
# <Element 'country' at 0x03127AC8>
# <Element 'country' at 0x03127D20>
# <Element 'country' at 0x03127F28>

# 查
# 全文搜索year
print(root.iter('year'))
# <_elementtree._element_iterator object at 0x034B8820>
print([i for i in root.iter('year')])
#[<Element 'year' at 0x02DE7B90>, <Element 'year' at 0x02DE7E10>, <Element 'year' at 0x02DED050>]

# 找到第一个就返回
print(root.find('country'))
# <Element 'country' at 0x035F7B68>

# 在root的子节点找，找所有的
print(root.findall('country'))
# [<Element 'country' at 0x035F7B68>, <Element 'country' at 0x035F7DC0>, <Element 'country' at 0x035F7FC8>]

# 找所有的rank标签，以及 attrib 和 text
print([i for i in root.iter('rank')])
# [<Element 'rank' at 0x02E87B40>, <Element 'rank' at 0x02E87DC0>, <Element 'rank' at 0x02E87FC8>]
print([i.attrib for i in root.iter('rank')])
# [{'updated': 'yes'}, {'updated': 'yes'}, {'updated': 'yes'}]
print([i.text for i in root.iter('rank')])
# ['2', '5', '69']


# 找到第二个country的 neighbor标签以及他的属性
print([tag for tag in root.findall('country')][1].find('neighbor').attrib)
# {'direction': 'N', 'name': 'Malaysia'}

# 增 append
# 给 year 大于2010年的所有标签下面添加一个month标签，属性为name:month 内容为30days

for country in root.findall('country'):
    for year in country.findall('year'):
        if int(year.text) > 2010:
            month = ET.Element('month')
            month.text = '30days'
            month.attrib = {'name': 'month'}
            country.append(month)
tree.write('b.xml')

#改
# 对所有的year属性以及值进行修改
for node in root.iter('year'):
    new_year=int(node.text)+1
    node.text=str(new_year)
    node.set('updated','yes')
    node.set('version','1.0')
tree.write('test.xml')


# 删
# 将 rank值大于50的country标签删除
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')