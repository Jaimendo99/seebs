# services/task_service.py

from models import Task, User, Job, Status
from utils.database import db


class TaskService:
    @staticmethod
    def create_task(job_id, user_id, description, difficulty, estimatetime):
        new_task = Task(job_id=job_id, user_id=user_id, description=description,
                        difficulty=difficulty, estimatetime=estimatetime)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def update_task(task_id, job_id, user_id, description, difficulty, estimatetime, status, donetime):
        task = Task.query.get_or_404(task_id)
        task.job_id = job_id
        task.user_id = user_id
        task.description = description
        task.difficulty = difficulty
        task.estimatetime = estimatetime
        task.status_id = status
        status = int(status)
        if status == 3:
            task.donetime = donetime
        db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
