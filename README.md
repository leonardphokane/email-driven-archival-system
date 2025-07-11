
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

## 📁 File Structure (with links)
- [`lambdas/`](./lambdas) 
- [`FileUploadNotifier.py`](./lambdas/FileUploadNotifier.py)
- [`DeleteFileMover.py`](./lambdas/DeleteFileMover.py)
- [`deployment-guide.md`](./deployment-guide.md)
- [`README.md`](./README.md)

  
---

## 📬 Example Email Command

To archive a file named `sample-report.pdf`, reply to the email notification with:


- Delete [`sample-report.pdf`](./sample-report.pdf)


## 👨‍💻 Author
**Leonard Phokane** · DevOps + Cloud Developer  
Built with 💡 from AWS documentation and real-world curiosity.


The system automatically moves it to the archive folder.

---

## 👨‍💻 Author

**Leonard Phokane**  
Developer · Cloud Architect in training  
[GitHub Profile](https://github.com/leonardphokane)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).



