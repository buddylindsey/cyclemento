from fabric.api import env, cd, sudo, task, run, prefix

env.hosts = ['root@cyclemento.com']
site_root = '/var/www/mento/mento'

def stop_celery():
    run('service celeryd stop')
    run('service celerybeat stop')

def pull_code():
    run('git pull origin master')

def install_requirements():
    run('pip install -r ../requirements.txt')

def migrate():
    run('./manage.py migrate --noinput')

def build_static():
    run('./manage.py collectstatic --noinput')

def start_celery():
    run('service celeryd start')
    run('service celerybeat start')

def restart_gunicorn():
    run('supervisorctl restart gunicorn')

@task
def deploy():
    stop_celery()
    with prefix('source /var/www/venv/mento/bin/activate'):
        with cd(site_root):
            pull_code()
            install_requirements()
            migrate()
            build_static()

    start_celery()
    restart_gunicorn()
