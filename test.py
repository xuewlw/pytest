'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


my_abs(9)

def add_end(L=[]):
    L.append('end')
    print(L)
    return  L

add_end()
add_end()


def add_end(L = None):
    if L is None:
        L=[]
    L.append('end')
    print(L)
    return  L

add_end()
add_end()


def printcoffee(*coffeename):
    print('\n我喜欢的咖啡有:')
    for item in coffeename:
        print(item)

printcoffee('山')
printcoffee('蓝山','土耳其','巴西')

parm = ['蓝山','土期','大小']
printcoffee(*parm)


def fun_bmi_upgrade(*person):
    for list_person in person:
        for item in list_person:
            person=item[0]
            height=item[1]
            weight=item[2]
            bmi=weight/(height*height)
            print("bmi指数"+str(bmi))



list_w = [('绮梦', 1.7, 65), ('领域', 1.78 , 50)]
list_m = [('心轩', 1.80, 75), ('伊一', 1.75, 70)]

fun_bmi_upgrade(list_w, list_m)
'''

def fun_checkout(money):
    money_old=sum(money)
    money_new=money_old

    if 500 <= money_old < 1000:
        money_new='{:.2f}'.format(money_old*0.9)
    elif 1000<= money_old <2000:
        money_new = '{:.2f}'.format(money_old*0.8)
    elif 2000<= money_old <3000:
        money_new = '{:.2f}'.format(money_old*0.7)

    return money_old,money_new

list_money = []
while True:
    inmoney = float(input("输入金额"))
    if inmoney==0:
        break
    else:
        list_money.append(inmoney)

money = fun_checkout(list_money)
print("合计",money[0],"就付",money[1])


print("gittest")