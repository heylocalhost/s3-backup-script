# Automated Backup Script

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![AWS S3](https://img.shields.io/badge/AWS-S3-yellowgreen)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)
![PRs](https://img.shields.io/badge/PRs-welcome-blueviolet)
![GitHub contributors](https://img.shields.io/github/contributors/yourusername/backup-script)
![GitHub forks](https://img.shields.io/github/forks/yourusername/backup-script)
![GitHub issues](https://img.shields.io/github/issues/yourusername/backup-script)

## Overview

This project is a Python-based automated backup script designed to regularly back up important development files or directories to both a local backup location and an Amazon S3 bucket. The script is scheduled to run daily at 11:45 PM IST via a cron job, ensuring that your important files are securely backed up on a consistent basis.

## Features

- **Automated Backups**: Schedule backups to run daily at a specific time.
- **S3 Integration**: Securely upload backups to an Amazon S3 bucket.
- **Local Backup Option**: Optionally store backups locally in addition to S3.
- **Logging**: Detailed logs are maintained for each backup operation.

## Project Structure

```
backup-script/
│
├── src/
│   └── backup_script.py      # Main backup script
│
├── config/
│   └── config.json           # Configuration file (non-sensitive settings)
│
├── logs/
│   └── backup.log            # Log file for backup operations
│
└── README.md                 # Project documentation (this file)
```

## Getting Started

### Prerequisites

Before running the script, ensure you have the following:

- **Python 3**: Installed on your system.
- **AWS Account**: With access to an S3 bucket.
- **boto3 Library**: AWS SDK for Python.
  
  Install `boto3` using pip:
  
  ```bash
  pip install boto3
  ```

- **python-dotenv Library**: To load environment variables from a `.env` file.

  Install `python-dotenv` using pip:
  
  ```bash
  pip install python-dotenv
  ```

### Setup

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/heylocalhost/s3-backup-script.git
   cd backup-script
   ```

2. **Configuration**

   The script uses a `config.json` file to specify directories for backup, the S3 bucket details, and backup schedules. Sensitive information such as AWS credentials should not be stored directly in this file.

   - **Step 1:** Modify the `config/config.json` file to specify your source directories, S3 bucket name, and S3 folder path.

     **Example:**
     ```json
     {
         "source_directories": [
             "/path/to/development/folder1",
             "/path/to/development/folder2"
         ],
         "backup_destination": "/path/to/local/backup/location",  // Optional
         "s3_bucket_name": "your-s3-bucket-name",
         "s3_backup_folder": "your/s3/folder/path"
     }
     ```

   - **Step 2:** Create a `.env` file in the project root to store your sensitive credentials. **Do not** commit this file to version control.

     **File:** `.env`
     ```plaintext
     AWS_ACCESS_KEY_ID=your-access-key-id
     AWS_SECRET_ACCESS_KEY=your-secret-access-key
     ```

### Usage

1. **Run Manually**

   You can run the script manually to test if the backup works correctly:

   ```bash
   python3 src/backup_script.py
   ```

2. **Setup Cron Job**

   To automate the backup, set up a cron job to run the script daily at 11:45 PM IST. 

   - Open the crontab editor:

     ```bash
     crontab -e
     ```

   - Add the following line to schedule the backup:

     ```bash
     15 18 * * * /usr/bin/python3 /path/to/your/project/src/backup_script.py
     ```

   This cron job will execute the script every day at 11:45 PM IST (18:15 UTC).

### Logs

The script maintains a log file at `logs/backup.log` that records each backup operation, including any errors or warnings.

### Security Considerations

- **Sensitive Information**: Ensure that your AWS credentials (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`) are stored securely in environment variables or a `.env` file. **Do not** commit these credentials to your version control system.
- **.gitignore**: The `.env` file and any other sensitive configuration files should be added to `.gitignore` to prevent them from being accidentally pushed to a remote repository.

### Example `.gitignore`

```plaintext
# Ignore .env file containing sensitive credentials
.env

# Ignore config.json if it contains sensitive data
config/config.json

# Ignore logs
logs/backup.log
```

### Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your contributions adhere to the project's coding standards and add value to the project.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Contact

For any issues, questions, or suggestions, please contact the repository owner at [your-email@example.com].
