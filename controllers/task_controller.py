# controllers/task_controller.py

from flask import Blueprint, request, render_template
from flask_login import login_required
from services.taskService import TaskService
from models import User, Status, Task, Job

task_blueprint = Blueprint('tasks', __name__)


@task_blueprint.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    task_data = []
    for task in tasks:
        job = Job.query.get(task.job_id)
        user = User.query.get(task.user_id)
        status = Status.query.get(task.status_id)
        task_data.append({
            'id': task.id,
            'job_name': job.name,
            'user_name': f"{user.first_name} {user.last_name}",
            'description': task.description,
            'difficulty': task.difficulty,
            'estimatetime': task.estimatetime,
            'donetime': task.donetime,
            'status': status.status_description
        })
    return render_template('task.html', tasks=task_data)


@task_blueprint.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'GET':
        users = User.query.filter_by(role='ROLE_USER').all()
        return render_template('add_task.html', tasks=Task.query.all(), users=users)

    if request.method == 'POST':
        job_id = request.form.get('job_id')
        user_id = request.form.get('user_id')
        description = request.form.get('description')
        difficulty = request.form.get('difficulty')
        estimatetime = request.form.get('estimatetime')

        if not all([job_id, description, estimatetime]):
            return render_template('add_task.html', tasks=Task.query.all())

        task = TaskService.create_task(
            job_id, user_id, description, difficulty, estimatetime)
        return render_template('task.html', tasks=Task.query.all())


@task_blueprint.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def update_task(task_id):
    if request.method == 'GET':
        users = User.query.filter_by(role='ROLE_USER').all()
        task = Task.query.get_or_404(task_id)
        return render_template('edit_task.html', task=task, users=users, status=Status.query.all())

    if request.method == 'POST':
        job_id = request.form.get('job_id')
        user_id = request.form.get('user_id')
        description = request.form.get('description')
        difficulty = request.form.get('difficulty')
        estimatetime = request.form.get('estimatetime')
        status = request.form.get('status')
        donetime = request.form.get('donetime')

        task = TaskService.update_task(
            task_id, job_id, user_id, description, difficulty, estimatetime, status, donetime)
        return render_template('task.html', tasks=Task.query.all())


@task_blueprint.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    TaskService.delete_task(task_id)
    return render_template('task.html', tasks=Task.query.all())
