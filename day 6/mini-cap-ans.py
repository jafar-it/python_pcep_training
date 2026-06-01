# task management system

from datetime import datetime, date

class AuditMixin:
    def _init_audit(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.change_log = []

    def log_change(self, field, old, new):
        self.updated_at = datetime.now()
        entry = {"time": self.updated_at.isoformat(), "field": field, "from": old, "to": new}
        self.change_log.append(entry)
        print(f"  [Audit] {field}: '{old}' → '{new}'")


class User:
    _counter = 0
    def __init__(self, name, email, role="developer"):
        User._counter += 1
        self.user_id = f"U{User._counter:03d}"
        self.name = name
        self.email = email
        self.role = role
        self.assigned_tasks = []

    def __str__(self): return f"{self.name} ({self.role})"
    def __repr__(self): return f"User({self.user_id}, {self.name!r})"


class Task(AuditMixin):
    _counter = 0
    VALID_TRANSITIONS = {
        "todo": ["in_progress"],
        "in_progress": ["done", "todo"],
        "done": []
    }

    def __init__(self, title, description="", priority=3, due_date=None):
        Task._counter += 1
        self.task_id = f"T{Task._counter:04d}"
        self.title = title
        self.description = description
        self._status = "todo"
        self.priority = max(1, min(5, priority))
        self.due_date = due_date
        self._assignee = None
        self.tags = []
        self._init_audit()

    @property
    def status(self): return self._status

    @status.setter
    def status(self, new_status):
        valid = self.VALID_TRANSITIONS.get(self._status, [])
        if new_status not in valid:
            raise ValueError(f"Cannot transition from '{self._status}' to '{new_status}'")
        self.log_change("status", self._status, new_status)
        self._status = new_status

    @property
    def assignee(self): return self._assignee

    @assignee.setter
    def assignee(self, user):
        old = self._assignee.name if self._assignee else "None"
        new = user.name if user else "None"
        self.log_change("assignee", old, new)
        if self._assignee and self in self._assignee.assigned_tasks:
            self._assignee.assigned_tasks.remove(self)
        self._assignee = user
        if user: user.assigned_tasks.append(self)

    @property
    def is_overdue(self):
        return self.due_date and self.due_date < date.today() and self._status != "done"

    def __lt__(self, other):
        return self.priority > other.priority   # higher priority number = "less" (sort asc)

    def __str__(self):
        assignee = self._assignee.name if self._assignee else "Unassigned"
        overdue = " ⚠️OVERDUE" if self.is_overdue else ""
        return f"[{self.task_id}] P{self.priority} | {self._status.upper():<12} {self.title} → {assignee}{overdue}"


class Project:
    def __init__(self, name, manager: User):
        self.name = name
        self.manager = manager
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        return task

    def assign_task(self, task_id: str, user: User):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task: raise KeyError(f"Task {task_id} not found")
        task.assignee = user

    def get_tasks_by_status(self, status):
        return [t for t in self.tasks if t.status == status]

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue]

    @property
    def summary(self):
        todo = len(self.get_tasks_by_status("todo"))
        wip = len(self.get_tasks_by_status("in_progress"))
        done = len(self.get_tasks_by_status("done"))
        total = len(self.tasks)
        pct = int(done / total * 100) if total else 0
        return f"{self.name} | Manager: {self.manager.name} | {done}/{total} done ({pct}%) | {todo} todo | {wip} in progress"

    def print_board(self):
        print(f"\n{'='*60}")
        print(f"  PROJECT: {self.name}")
        print(f"  {self.summary}")
        print(f"{'='*60}")
        for task in sorted(self.tasks):
            print(f"  {task}")


# --- Demo ---
alice = User("Alice", "alice@co.com", "manager")
bob = User("Bob", "bob@co.com")
carol = User("Carol", "carol@co.com")

project = Project("Mobile App v2", alice)

t1 = project.add_task(Task("Setup CI/CD pipeline", priority=5, due_date=date(2025, 12, 1)))
t2 = project.add_task(Task("Design database schema", priority=5))
t3 = project.add_task(Task("Build user auth module", priority=4))
t4 = project.add_task(Task("Write API documentation", priority=2))
t5 = project.add_task(Task("Performance testing", priority=3))

project.assign_task(t1.task_id, bob)
project.assign_task(t2.task_id, carol)
project.assign_task(t3.task_id, bob)
project.assign_task(t4.task_id, carol)

t1.status = "in_progress"
t2.status = "in_progress"
t2.status = "done"

project.print_board()