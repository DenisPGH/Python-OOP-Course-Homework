
from .task import Task



class Section():
    def __init__(self,name):
        self.name = name
        self.tasks=[]
    # -	add_task(new_task: Task)
    # o	Adds a new task to the collection and returns "Task {task details} is added to the section"
    # o	If the task is already in the collection, returns "Task is already in the section {section_name}"
    def add_task(self,new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    #-	complete_task(task_name: str)
#o	Changes the task to completed (True) and returns "Completed task {task_name}"
#o	If the task is not found, returns "Could not find task with the name {task_name}"
    def complete_task(self,task_name: str) :
        for each in self.tasks:
            if each.username==task_name:
                each.completed=True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    # -	clean_section()
    # o	Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
    def clean_section(self):
        count_removed_tasks=0
        for each_task in self.tasks:
            if each_task.completed==True:
                count_removed_tasks+=1
                del each_task
        return f"Cleared {count_removed_tasks} tasks."

    #-	view_section()
# o	Returns information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      …
#      {details of the n task}"
    def view_section(self):
        result=f"Section {self.name}:\n"
        for each_task in self.tasks:
            result+=f"{each_task.details()}\n"

        return result








