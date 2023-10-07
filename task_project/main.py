class Task():
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def get_cmd(self):
        return str(self.id)+" "+self.name


class_list = []
def add_task(task):
    class_list.append(task)
    return True

def remove_task(id):
    for i in class_list:
        if i.id == id:
            class_list.remove(i)
            return True

def show_task():
    print("======最新任务信息======")
    print("id"+" "+"name")
    for i in class_list:
        print(i.get_cmd())
    print("======================\n")

if __name__ =="__main__":
    while True:
        print("1.添加任务\n2.删除任务\n3.显示任务\n4.退出")
        func_num = int(input())
        if func_num==1:
            task = Task(int(input("请输入任务id：")),input("请输入任务名称："))
            add_task(task)
            show_task()
        elif func_num==2:
            remove_task(int(input("请输入要删除的任务id：")))
            show_task()
        elif func_num==3:
            show_task()
        elif func_num==4:
            print("谢谢使用")
            break