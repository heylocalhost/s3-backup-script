import os
import shutil
import json
import datetime
import logging
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configuration
with open('../config/config.json', 'r') as config_file:
    config = json.load(config_file)

source_directories = config['source_directories']
backup_destination = config['backup_destination']
s3_bucket_name = config['s3_bucket_name']
s3_backup_folder = config['s3_backup_folder']
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Setup logging
logging.basicConfig(filename='../logs/backup.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Setup S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

def backup():
    for directory in source_directories:
        if os.path.exists(directory):
            # Create a local backup
            if backup_destination:
                dest_dir = os.path.join(backup_destination, os.path.basename(directory) + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                shutil.copytree(directory, dest_dir)
                logging.info(f"Backed up {directory} to {dest_dir}")
            
            # Upload backup to S3
            for root, dirs, files in os.walk(directory):
                for file in files:
                    full_path = os.path.join(root, file)
                    s3_key = os.path.join(s3_backup_folder, os.path.relpath(full_path, directory))
                    s3_client.upload_file(full_path, s3_bucket_name, s3_key)
                    logging.info(f"Uploaded {full_path} to s3://{s3_bucket_name}/{s3_key}")
        else:
            logging.warning(f"Directory {directory} does not exist. Skipping.")

if __name__ == "__main__":
    backup()
