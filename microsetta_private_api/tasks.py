from microsetta_private_api.celery_utils import celery
from microsetta_private_api.util.email import SendEmail
from microsetta_private_api.admin.email_templates import EmailMessage


@celery.task(ignore_result=True)
def send_email(email, template_name, template_args):
    template = EmailMessage[template_name]
    SendEmail.send(email, template, template_args)
