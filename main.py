import json
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
sender_email=os.getenv("MY_EMAIL")
sender_psw=os.getenv("MY_PSW")

def send_email(event,context):
    try:
        print("Received event:",event)
        body=json.loads(event.get('body')or '{}' )
   
        receiver_email=body.get('receiver_email')
        subject=body.get('subject')
        body_text=body.get('body_text')
        if not receiver_email:
            return{
                "statusCode":400,
                "body":json.dumps({"error":"Missing receiver's email. "})
            }
        elif not subject:

            return{
                "statusCode":400,
                "body":json.dumps({"error":"Missing subject of email. "})
            }
        
        elif not body_text:
            return{
                "statusCode":400,
                "body":json.dumps({"error":"Missing body text of email. "})
            }
        
        else:
            with smtplib.SMTP("smtp.gmail.com",port =587) as connection:
                connection.starttls()
                print("logging in.....")
                connection.login(sender_email,sender_psw)
                print("sending email .....")
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=receiver_email,
                    msg=f"Subject:{subject}\n\n{body_text}"
                )
            
            return {
                "statusCode":200,
                "body":json.dumps({"message":"Email sent successfully !"})
            }
    except json.JSONDecodeError:
        return {
        "statusCode": 400,
        "body": json.dumps({"error": "Invalid JSON in request body."})
    }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }     
    


