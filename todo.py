import argparse
import os
import json
from datetime import datetime

JSON = "data.json"


def jsoncheck():
    if not os.path.exists(JSON):
        with open(JSON, "w") as f:
            json.dump({"name": None, "tasks": []}, f, indent=2)
    try:
        with open(JSON, "r") as f:
            data = json.load(f)

        # Ensure required keys exist
        if not isinstance(data, dict) or "name" not in data or "tasks" not in data:
            raise ValueError("Invalid structure")  # Force reset if structure is incorrect

    except (json.JSONDecodeError, ValueError):
        # If file is corrupted or structure is wrong, reset it
        with open(JSON, "w") as f:
            json.dump({"name": None, "tasks": []}, f, indent=4)


def loadjson():
    with open(JSON, "r") as f:
        return json.load(f)


def savejson(data):
    with open(JSON, "w") as f:
        json.dump(data, f, indent=2)


def set_name():
    name = input("Enter your name: ").strip()
    data = loadjson()
    data["name"] = name
    savejson(data)
    return name


def reset_name():
    """Deletes the stored name and asks for a new one."""
    data = loadjson()
    data["name"] = None
    savejson(data)
    print("Resetting done...")
    return set_name()


def addtask(task_name):
    data = loadjson()
    new_task = {
        "id": get_next_task_id(data["tasks"]),
        "t_name": " ".join(task_name),
        "createdat": datetime.now().isoformat(),
        "updatedat": datetime.now().isoformat(),
        "status": "to do"
    }
    data["tasks"].append(new_task)
    savejson(data)
    print(f"Task '{' '.join(task_name)}' added successfully!")


def get_next_task_id(tasks):
    """Returns the next numerical task ID."""
    if not tasks:
        return 1  # First task starts at 1
    return max(task["id"] for task in tasks) + 1


def updatetasks(args):
    data = loadjson()
    taskid = int(args[0])  # First argument is the task ID
    update = " ".join(args[1:])  # Combine all remaining arguments into a single string
    for task in data["tasks"]:
        if task["id"] == taskid:
            task["t_name"] = update
            task["updatedat"] = datetime.now().isoformat()
            savejson(data)
            print(f"Task '{taskid}' updated successfully!")
            return
    print(f"Task with ID '{taskid}' not found.")


def taskdelete(args):
    data = loadjson()
    taskid = int(args)
    for task in data["tasks"]:
        if task["id"] == taskid:
            data["tasks"].remove(task)
            savejson(data)
            print(f"Task '{taskid}' deleted successfully!")
            return
    print(f"Task with ID '{taskid}' not found.")


def statuschange(taskid, status):
    data = loadjson()
    for task in data["tasks"]:
        if task["id"] == taskid:
            task["status"] = status
            task["updatedat"] = datetime.now().isoformat()
            savejson(data)
            print(f"Task '{taskid}' marked as {status} successfully!")
            return
    print(f"Task with ID '{taskid}' not found.")


def main():
    parser = argparse.ArgumentParser(description="A simple todo list tool")
    parser.add_argument("--reset", action="store_true", help="Reset stored name")
    parser.add_argument("--exit", action="store_true", help="Exit the program")
    parser.add_argument("--add", type=str, nargs='+', help="Add a new task")
    parser.add_argument("--listall", action="store_true", help="List all tasks")
    parser.add_argument("--update", type=str, nargs='+', help="Update a task")
    parser.add_argument("--delete", type=int, help="Delete a task")
    parser.add_argument("--mark_in_progress", type=int, help="Mark a task as in progress")
    parser.add_argument("--mark_done", type=int, help="Mark a task as done")
    parser.add_argument("--mark_to_do", type=int, help="Mark a task as to do")
    parser.add_argument("--list", type=str,nargs="?",default=None, help="List tasks by status")

    jsoncheck()
    data = loadjson()

    if not data["name"]:
        data["name"] = set_name()  # Ask for a name if it doesn't exist

    print(f"Hello, {data['name']}!")  # Greets only once until program is restarted

    while True:  # Keep running until --exit is passed
        command = input("What would you like to do? ").strip()

        if command == "--exit":
            print("Goodbye!")
            break

        try:
            # Parse arguments and include all possible options in the default namespace
            args = parser.parse_args(command.split()) if command else argparse.Namespace(
                 reset=False, add=None, listall=False, update=None, delete=None,
                mark_in_progress=None, mark_done=None, mark_to_do=None )
            data = loadjson()
            if args.reset:
                reset_name()
            elif args.add:
                addtask(args.add)
            elif args.listall:
                data = loadjson()  # Reload data to reflect latest changes
                print("Tasks:")
                for task in data["tasks"]:
                    print(f"  {task['id']}: {task['t_name']} ({task['status']})")
            elif args.update:
                if len(args.update) < 2:
                    print("Error: --update requires exactly two arguments: <task_id> <new_task_name>")
                else:
                    updatetasks(args.update)
            elif args.delete:
                taskdelete(args.delete)
            elif args.mark_in_progress:
                statuschange(args.mark_in_progress, "in progress")
            elif args.mark_done:
                statuschange(args.mark_done, "done")
            elif args.mark_to_do:
                statuschange(args.mark_to_do, "to do")
            elif args.list is not None:  # Ensure the argument is not None
                status = args.list.strip().lower()  # Normalize status input
                matching_tasks = [task for task in data["tasks"] if task["status"].lower() == status]
                if matching_tasks:
                    print(f"Tasks with status '{status}':")
                    for task in matching_tasks:
                        print(f"  {task['id']}: {task['t_name']} ({task['status']})")
                else:
                    print(f"No tasks found with status '{status}'.")
            else:
                print("Invalid command. Please try again.")
        except SystemExit:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()