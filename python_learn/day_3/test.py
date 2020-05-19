# v = {}
#
# for index in range(0, 10):
#     v["users"] = index
# print(v)

goods = [{"name":"电脑","price":1990},{"name":"鼠标","price":10},{"name":"游艇","price":1990000},{"name":"水果","price":9.9}]
# count = 1
# for index in goods:
#     print(count, index["name"], index["price"])
#     count += 1
#
# for index in enumerate(goods, start=1):
#     print(index[0], index[1]["name"], index[1]["price"])
#
# for num,dic in enumerate(goods, start=1):
#     print(num, dic["name"], dic["price"])

while(1):
    for num, dic in enumerate(goods, start=1):
        print(num, dic["name"], dic["price"])
    choice_num = input("请输入商品序号：").strip()
    if choice_num.isdecimal():
        choice_num = int(choice_num)
        if 0 < choice_num <= len(goods):
            print("你选择的商品名称是{0}， 价格是{1}".format(goods[choice_num-1]["name"], goods[choice_num-1]["price"]))
        else:
            print("输入商品序号不存在，请重新输入")
    elif choice_num.upper() == 'Q':
        break
    else:
        print("输入商品序号不是序号，请重新输入")

