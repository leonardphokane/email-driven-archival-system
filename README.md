## ✉️ Email-Driven Archival System
_A serverless AWS workflow that..._

## 🚀 How It Works
1. **File Upload to S3**
2. **Email Notification**
3. **User Reply**
4. **Email Parsed & Triggered**

# ✉️ Email-Driven Archival System

A serverless AWS workflow that reacts to email replies by archiving uploaded files. Built using **Amazon S3**, **Lambda**, **SES**, and **IAM**, this system allows users to upload files and later trigger file movement to an archive location just by replying to notification emails with a simple command.

---

## 🚀 How It Works

1. **File Upload to S3**
   - Users upload files to `leonard-upload-bucket-2025/uploads/`
2. **Email Notification**
   - `FileUploadNotifier` Lambda sends a SES email about the upload
3. **User Reply**
   - User replies with a subject like `Delete sample-report.pdf`
4. **Email Parsed & Triggered**
   - SES routes reply to `leonard-email-replies-2025`
   - `DeleteFileMover` Lambda scans the reply and moves the file to:
     ```
     leonard-archive-bucket-2025/archive/
     ```

---

## 🧠 Tech Stack

- **AWS Lambda** — serverless function logic
- **Amazon S3** — storage for uploads, email replies, and archived files
- **Amazon SES** — notification and reply flow via email
- **IAM Roles** — permission control for S3 access

---

## 🛠 File Structure
email-driven-archival-system/ ├── lambdas/ │ ├── FileUploadNotifier.py │ └── DeleteFileMover.py ├── deployment-guide.md ├── README.md
