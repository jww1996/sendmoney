import money

#查询工资
def select_money():
    saved_money = money.saved_money
    if saved_money ==2000:
        print(f"收到工资啦!,账户现有{saved_money}元")
    else:
        print(f"没有收到工资，账户现有{saved_money}元")
