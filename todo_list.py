import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
        return
    print("\n📝 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(f"[ ] {task}")
        print("✅ Task added!")
    else:
        print("⚠️  Empty task not added.")
    return tasks

def mark_done(tasks):
    display_tasks(tasks)
    if not tasks:
        return tasks
    try:
        idx = int(input("Enter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            if tasks[idx].startswith("[✓]"):
                print("⚠️  Already marked done.")
            else:
                tasks[idx] = tasks[idx].replace("[ ]", "[✓]", 1)
                print("✅ Task marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")
    return tasks

def update_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return tasks
    try:
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_task = input("Enter updated task: ").strip()
            if new_task:
                done_mark = "[✓]" if tasks[idx].startswith("[✓]") else "[ ]"
                tasks[idx] = f"{done_mark} {new_task}"
                print("✏️  Task updated!")
            else:
                print("⚠️  Empty task ignored.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")
    return tasks

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return tasks
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"🗑️  Deleted: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")
    return tasks

def main():
    print("✨ CodSoft Internship - To-Do List (Day 3) ✨")
    tasks = load_tasks()

    while True:
        print("\nChoose an option:")
        print("1 ➝ View Tasks")
        print("2 ➝ Add Task")
        print("3 ➝ Mark Task as Done")
        print("4 ➝ Update Task")
        print("5 ➝ Delete Task")
        print("0 ➝ Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            tasks = mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            tasks = update_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            tasks = delete_task(tasks)
            save_tasks(tasks)
        elif choice == "0":
            print("\n💾 Tasks saved. Goodbye Master 🫡!")
            save_tasks(tasks)
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
