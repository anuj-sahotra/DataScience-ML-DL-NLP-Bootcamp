## Manage A To Do List

# Create a To Do List to keep track of tasks
to_do_list = ["Python", "5 KM Run", "Read 10 pages"]

# Adding task
to_do_list.append("3L Water")
to_do_list.append("Clean My Room")

# Removing a completed task
to_do_list.remove("Python")

# Checking if a task in a list
if "5 KM Run" in to_do_list:
    print("Don't forget to run.\n")
    
print("TO DO LIST Remaining :")
for task in to_do_list:
    print(f"- {task}")     