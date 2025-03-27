# Todo List CLI

A simple command-line tool for managing a to-do list using a JSON file for storage. This tool allows users to add, update, delete, and list tasks with different statuses.

## Features
- Add tasks with unique IDs
- Update existing tasks
- Delete tasks by ID
- Change task status (`to do`, `in progress`, `done`)
- List all tasks or filter by status
- Persistent task storage in `data.json`

## Installation
Clone this repository:

```sh
git clone https://github.com/yourusername/todo-list-cli.git
cd todo-list-cli
```

Install dependencies (if needed):

```sh
pip install -r requirements.txt  # Only if you add external dependencies
```

## Usage
Run the script using Python:

```sh
python todo.py
```

### Commands

| Command | Description |
|---------|-------------|
| `--reset` | Reset the stored username |
| `--add "Task Name"` | Add a new task |
| `--listall` | List all tasks |
| `--update <task_id> "New Task Name"` | Update a task name |
| `--delete <task_id>` | Delete a task |
| `--mark_in_progress <task_id>` | Mark task as "in progress" |
| `--mark_done <task_id>` | Mark task as "done" |
| `--mark_to_do <task_id>` | Reset task to "to do" |
| `--list <status>` | List tasks by status |
| `--exit` | Exit the program |

### Examples

**Add a Task:**
```sh
python todo.py --add "Buy groceries"
```

**Update a Task:**
```sh
python todo.py --update 1 "Buy vegetables"
```

**Delete a Task:**
```sh
python todo.py --delete 1
```

**Mark Task as Done:**
```sh
python todo.py --mark_done 1
```

**List Tasks by Status:**
```sh
python todo.py --list "done"
```

## File Structure
```
.
├── todo.py         # Main script
├── data.json      # Stores tasks persistently
├── README.md      # Project documentation
```

## Contributing
Feel free to fork the repository and submit pull requests with improvements or new features.

## Project URL
```
https://roadmap.sh/projects/task-tracker
```

