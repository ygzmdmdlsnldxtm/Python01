import demo_tools
global time
flag = True #TODO 退出最终循环的标志
time = 3
# TODO 显示界面
demo_tools.show_menu()
while flag:
    pass_word = input("请输入账户：")
    if pass_word in ["12306"]:
        while True:
            action_str = input("请输入要执行的操作：")
            print("您选择的操作是【{}】".format(action_str))
            if action_str in ["1", "2", "3"]:
                if action_str == "1":
                    demo_tools.new_mess()
                elif action_str == "2":
                    demo_tools.show_all()
                elif action_str == "3":
                    demo_tools.search_mess()
            elif action_str == "0":
                print("欢迎再次使用[信息管理系统]")
                flag = False
                break
            else:
                print("您输入操作有误，请重新操作......")

    else:
        print("输入账户有误，输入次数为{}".format(time))
        if time <= 0:
            break
        time = time - 1