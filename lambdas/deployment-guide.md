# 📦 Deployment Guide: Email-Driven Archival System

This guide walks you through setting up the AWS-based file archival system triggered via email replies.

---

## 🗃️ 1. S3 Buckets

### A. File Upload Bucket
- Name: `leonard-upload-bucket-2025`
- Create a folder named `uploads/` inside it

### B. Archive Bucket
- Name: `leonard-archive-bucket-2025`
- Create a folder named `archive/` inside it

### C. Email Replies Bucket
- Name: `leonard-email-replies-2025`
- Used to store SES-inbound emails (must enable SES rule to drop messages here)

---

## ✉️ 2. Amazon SES

1. **Verify your email** (e.g. `leonardphokane1@gmail.com`)
2. Create an **email rule set**:
   - Triggered when email is sent to `leonardphokane1@gmail.com`
   - Store the email body in `leonard-email-replies-2025` bucket
   - Trigger `DeleteFileMover` Lambda on new object

---

## ⚙️ 3. Lambda Functions

### A. `FileUploadNotifier`
- Trigger: **S3 "ObjectCreated"** on `uploads/` prefix
- Action: Sends SES email with file name
- Permissions:
  - `s3:GetObject`
  - `ses:SendEmail`

### B. `DeleteFileMover`
- Trigger: **S3 "ObjectCreated"** on `leonard-email-replies-2025`
- Action: Parses email body, checks for `Delete filename.pdf`, moves file
- Permissions:
  - `s3:GetObject`, `s3:PutObject`, `s3:DeleteObject`

---

## 🔐 4. IAM Roles

Create IAM roles for each Lambda:
- **FileUploadNotifierRole**
- **DeleteFileMoverRole**

Assign permissions to access S3 and SES as described above.

---

## ✅ 5. Test Flow

1. Upload a file to `uploads/`
2. Ensure notification email is received
3. Reply with `Delete sample-report.pdf`
4. Confirm file was moved to `archive/`

---

Built with 💡 by Leonard Phokane ☁️
