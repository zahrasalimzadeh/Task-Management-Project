list_employees = []
list_task = []
undone_tasks = []
doing_tasks = []
done_tasks = []

while True:
    print(
        "Select the desired number: [1,2,3,4,0]\n"
        "1:creat new employee \n"
        "2:creat new task \n"
        "3:change task state \n"
        "4:show task list \n"
        "0:exit \n \n"
    )
    select_number = int(input("Please select one of the items:"))
    print("--------------------")

    match select_number:
        case 1:
            new_employee = {
                "first_name": input("first_name:"),
                "last_name": input("last_name:"),
                "personnel_code": input("personnel_code:")
            }
            print()
            list_employees.append(new_employee)
            print(list_employees)
            print("--------------------")

        case 2:
            new_task = {
                "title_task": input("title_task:"),
                "description_task": input("description_task:"),
                "deadline_task": input("deadline_task(hour):"),
                "responsible_task": None,
                "status": "undone"
            }

            assignment_statusinput = input("Do you want this task assigned to someone?: (yes/no)")

            if assignment_statusinput == "no":
                list_task.append(new_task)
                undone_tasks.append(new_task)
                print("Task without an owner was added to the undone list")
                print("--------------------")

            elif assignment_statusinput == "yes":
                responsible_task = input("responsible_personnel_code:")
                for employee in list_employees:
                    if employee["personnel_code"] == responsible_task:
                        new_task["responsible_task"] = responsible_task
                        list_task.append(new_task)
                        undone_tasks.append(new_task)
                        print("Task successfully assigned.")
                        print()
                        print(f"Task_list {list_task}")
                        print("--------------------")
                        break
                else:
                    print("such an employee does not exist and is not defined.")
                    print("--------------------")
            else:
                print("Invalid choice.")
                print("--------------------")

        case 3:
            task_name = input("Enter the task name to update: ")
            for task in list_task:
                if task["title_task"] == task_name:
                    print("Select status: 1:undone, 2:doing, 3:done")
                    status_choice = int(input("choice:"))

                    if task in undone_tasks:
                        undone_tasks.remove(task)
                    if task in doing_tasks:
                        doing_tasks.remove(task)
                    if task in done_tasks:
                        done_tasks.remove(task)

                    if status_choice == 1:
                        task["status"] = "undone"
                        undone_tasks.append(task)
                        print("Task status updated.")
                        print("--------------------")
                        break

                    elif status_choice == 2:
                        task["status"] = "doing"
                        doing_tasks.append(task)
                        print("Task status updated.")
                        print("--------------------")
                        break

                    elif status_choice == 3:
                        task["status"] = "done"
                        done_tasks.append(task)
                        print("Task status updated.")
                        print("--------------------")
                        break

                    else:
                        print("Invalid status choice.")
                        print("--------------------")
                        break
            else:
                print("Task not found!")
                print("--------------------")

        case 4:
            print("Employees list:", list_employees)
            print("Tasks list:", list_task)
            print("Undone tasks:", undone_tasks)
            print("Doing tasks:", doing_tasks)
            print("Done tasks:", done_tasks)
            print("--------------------")

        case 0:
            break
