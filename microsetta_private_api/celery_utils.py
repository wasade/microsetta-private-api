from celery import Celery

from microsetta_private_api.config_manager import SERVER_CONFIG

PACKAGE = __name__.split('.')[0]
CELERY_BACKEND_URI = 'celery_backend_uri'
CELERY_BROKER_URI = 'celery_broker_uri'


# derived from
# https://medium.com/@frassetto.stefano/flask-celery-howto-d106958a15fe
def init_celery(celery, app):
    celery.conf.update(app.config)
    celery.conf.task_default_queue = 'microsetta-private-api'
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    celery.autodiscover_tasks([PACKAGE])


def make_celery(app_name):
    celery_backend = SERVER_CONFIG[CELERY_BACKEND_URI]
    celery_broker = SERVER_CONFIG[CELERY_BROKER_URI]
    return Celery(app_name, backend=celery_backend, broker=celery_broker)


celery = make_celery(PACKAGE)
