# 📧 Serverless Email API (Python)

This is a simple serverless REST API built with the [Serverless Framework](https://www.serverless.com/) in Python. It accepts a `receiver_email`, `subject`, and `body_text`, then sends an email using Gmail's SMTP server.

---

## 🚀 Features

- ✅ Send emails via HTTP POST requests
- ✅ Built with Python
- ✅ Runs locally with `serverless-offline`
- ✅ Error handling for missing or invalid input
- ✅ Uses environment variables for secure credentials

---

## 📁 Project Structure

email-api-serverless/
│
├── main.py # sends mail 
├── serverless.yml # Serverless config
├── .env # Environment variables (NOT pushed to Git)
├── requirements.txt # Python dependencies
└── README.md # This file

yaml
Copy code

---

## ⚙️ Requirements

- Python 3.x
- Node.js & npm
- Serverless Framework
- A Gmail account (for sending emails)
- Less secure apps access enabled on Gmail *(or an App Password if 2FA is on)*

---

## 🔐 Environment Variables

Create a `.env` file in the root with:

MY_EMAIL=your_email@gmail.com
MY_PSW=your_gmail_password_or_app_password

yaml
Copy code

---

## 🛠 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install Serverless globally if not done yet
npm install -g serverless

# Install offline plugin (locally)
npm install serverless-offline
▶️ Run Locally
bash
Copy code
# Start the local server
sls offline
📬 Send a Test Email
Use Postman or curl:

bash
Copy code
curl -X POST http://localhost:3000/dev/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "receiver_email": "example@example.com",
    "subject": "Hello",
    "body_text": "This is a test email from Serverless!"
  }'
✅ Sample Response
json
Copy code
{
  "message": "Email sent successfully!"
}
🚫 Error Responses
Missing receiver_email → 400 Bad Request

Missing subject → 400 Bad Request

Missing body_text → 400 Bad Request

Invalid JSON → 400 Bad Request

Other errors → 500 Internal Server Error
