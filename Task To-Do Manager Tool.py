import json

DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"pending": [], "completed": []}

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks["pending"].append(task)
    print(f"任务已添加：{task}")

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks["pending"]):
        task = tasks["pending"].pop(index)
        tasks["completed"].append(task)
        print(f"任务已标记为完成：{task}")
    else:
        print("无效的任务编号。")

def view_tasks(tasks):
    print("\n未完成任务：")
    if tasks["pending"]:
        for i, task in enumerate(tasks["pending"], 1):
            print(f"{i}. {task}")
    else:
        print("无未完成任务。")

    print("\n已完成任务：")
    if tasks["completed"]:
        for i, task in enumerate(tasks["completed"], 1):
            print(f"{i}. {task}")
    else:
        print("无已完成任务。")

def delete_task(tasks, index, completed=False):
    if completed:
        if 0 <= index < len(tasks["completed"]):
            removed_task = tasks["completed"].pop(index)
            print(f"已删除已完成任务：{removed_task}")
        else:
            print("无效的任务编号。")
    else:
        if 0 <= index < len(tasks["pending"]):
            removed_task = tasks["pending"].pop(index)
            print(f"已删除未完成任务：{removed_task}")
        else:
            print("无效的任务编号。")

if __name__ == "__main__":
    tasks = load_tasks()
    print("欢迎使用任务待办管理器！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加新任务")
        print("2. 查看所有任务")
        print("3. 标记任务为完成")
        print("4. 删除任务")
        print("5. 退出")

        choice = input("请输入选项（1/2/3/4/5）：")

        if choice == "1":
            task = input("请输入任务描述：")
            add_task(tasks, task)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("请输入要标记为完成的任务编号：")) - 1
                mark_task_completed(tasks, index)
                save_tasks(tasks)
            except ValueError:
                print("请输入有效的编号。")
        elif choice == "4":
            view_tasks(tasks)
            try:
                task_type = input("请选择任务类型（未完成：p，已完成：c）：").lower()
                if task_type == "p":
                    index = int(input("请输入要删除的未完成任务编号：")) - 1
                    delete_task(tasks, index, completed=False)
                elif task_type == "c":
                    index = int(input("请输入要删除的已完成任务编号：")) - 1
                    delete_task(tasks, index, completed=True)
                else:
                    print("无效的任务类型。")
                save_tasks(tasks)
            except ValueError:
                print("请输入有效的编号。")
        elif choice == "5":
            print("感谢使用任务待办管理器，再见！")
            break
        else:
            print("无效选项，请重新选择。")
