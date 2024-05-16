import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from aws_credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

class SNSService:
    def __init__(self, region_name='us-west-2'):
        try:
            self.sns_client = boto3.client(
                'sns',
                region_name=AWS_REGION,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError("Credenciales de AWS no encontradas o incompletas:", e)

    def enviar_notificacion(self, mensaje, numero_telefono):
        try:
            response = self.sns_client.publish(
                PhoneNumber=numero_telefono,
                Message=mensaje
            )
            return response
        except Exception as e:
            raise ValueError("Error al enviar notificación:", e)