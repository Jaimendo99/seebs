# decorators/task_decorator.py

class TaskDecorator:
    def __init__(self, task):
        self._task = task

    def add_bonus(self, bonus_percentage):
        self._task.bonus_percentage = bonus_percentage
        return self._task

    def add_status(self, status):
        self._task.status = status
        return self._task
