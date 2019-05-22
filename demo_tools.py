mess_list = []
mess_dict = {}
def show_menu():
    print("*"*50)
    print("欢迎使用【信息管理系统】V 1.0")
    print()
    print("1. 新增信息")
    print("2. 显示全部")
    print("3. 搜索信息")
    print()
    print("0. 退出系统")
    print("*"*50)


def new_mess():
    print("-"*50)
    print("新增信息")
    name_str = input("请输入姓名：")
    iphone_str = input("请输入电话：")
    email_str = input("请输入邮箱：")
    mess_dict = {
        "name":name_str,
        "iphone":iphone_str,
        "email":email_str
    }
    mess_list.append(mess_dict)
    #print(mess_list)
    print("{}信息添加成功....".format(name_str))

def show_all():
    print("-"*50)
    print("显示全部信息")
    if len(mess_list) == 0:
        print("当前没有信息记录为空，请执行操作1.......")
        return
    #打印表头
    for str in ["姓名","电话","邮箱"]:
        print(str,end='\t\t\t')
    print()
    #遍历字典
    for mess_dict in mess_list:
        print("{}\t\t{}\t\t{}".format(mess_dict["name"],mess_dict["iphone"],mess_dict["email"]))

def search_mess():
    print("-"*50)
    print("搜索信息")
    action_mess = input("请输入姓名：")
    for mess_dict in mess_list:
        if mess_dict["name"] == action_mess:
            print("姓名\t\t\t电话\t\t\t邮箱")
            print("*"*40)
            print("{}\t\t{}\t\t{}".format(mess_dict["name"],mess_dict["iphone"],mess_dict["email"]))

            deal_mess(mess_dict)
            break
        else:
            print("对不起没有找到{}该用户.....".format(action_mess))

def deal_mess(find_dict):

    action_str = input("请输入要执行的操作 [1]修改信息 [2]删除消息 [0] 返回主界面")
    if action_str == "1":
        find_dict["name"] = input_info(find_dict["name"],"请输入姓名：")
        find_dict["iphone"] = input_info(find_dict["iphone"],"请输入电话：")
        find_dict["email"] = input_info(find_dict["email"],"请输入邮箱：")
        print("已经完修改操作......")
    elif action_str == "2":
        mess_list.remove(find_dict)
        print("已经完成删除操作......")

def input_info(pre_value,tip_message):
    result_str = input(tip_message+"[如果不修改按回车]")
    if len(result_str) > 0:
        return result_str
    else:
        return pre_value