import os
import boto3
from botocore.exceptions import ClientError
import logging

class SESService():
    """
    Class to interact with boto3/SES to send emails.
    """

    CHARSET = "UTF-8"
    EMAIL_SENDER = os.environ["EMAIL_SENDER"]
    NAME_SENDER = os.environ["NAME_SENDER"]
    SERVICE_OBJ = boto3.client(
        "ses",
        aws_access_key_id=os.environ["SES_ACCESS_KEY"],
        aws_secret_access_key=os.environ["SES_SECRET_KEY"],
        region_name=os.environ["AWS_REGION"],
    )

    @classmethod
    def _get_email_body(cls, template_name, **kwargs):
        try:
            template_path = os.path.join(os.path.dirname(__file__), '../../utils/templates', f'{template_name}.html')
            with open(template_path, encoding='utf-8') as f:
                data = f.read()
            for k, v in kwargs.items():
                data = data.replace(f'{{{{ {k} }}}}', v)
            return data
        except FileNotFoundError:
            logging.error("Template file not found: %s", template_path)
            return None
        except Exception as e:
            logging.error("Error reading template file: %s", e)
            return None

    @classmethod
    def send_email(cls, recipient, subject, template_name, **kwargs):
        try:
            body = cls._get_email_body(template_name, **kwargs)
            if body is None:
                raise ValueError("Email body is None. Check the template and parameters.")

            cls.SERVICE_OBJ.send_email(
                Destination={
                    "ToAddresses": [
                        recipient,
                    ],
                },
                Message={
                    "Body": {"Html": {"Charset": cls.CHARSET, "Data": body}},
                    "Subject": {"Charset": cls.CHARSET, "Data": subject},
                },
                Source=f'{cls.NAME_SENDER} <{cls.EMAIL_SENDER}>'
            )
        except (ClientError, ValueError) as e:
            logging.error('Error sending email through SES: %s', e)
            return False
        else:
            logging.info('Email sent to [%s] with template [%s] with subject [%s]', recipient, template_name, subject)
            return True
