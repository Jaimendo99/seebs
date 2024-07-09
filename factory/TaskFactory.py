# factories/task_factory.py

from models import Task


class TaskFactory:
    @staticmethod
    def create_task(job_id, user_id, description, difficulty, estimatetime):
        return Task(job_id=job_id, user_id=user_id, description=description, difficulty=difficulty, estimatetime=estimatetime)
