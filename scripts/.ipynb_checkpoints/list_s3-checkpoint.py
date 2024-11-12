import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def listar_arquivos_no_bucket(nome_do_bucket):
    response = s3.list_objects_v2(Bucket=nome_do_bucket)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("O bucket está vazio ou o nome do bucket está incorreto.")

bucket_nome = 'noaa-ghcn-pds'

if __name__ == "__main__":
    listar_arquivos_no_bucket(bucket_nome)
