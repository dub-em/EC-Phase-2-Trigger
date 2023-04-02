from config import settings
import smtplib, requests, schedule, time
from email.message import EmailMessage

def app():
    '''Function for triggering the prediction API and forwarding 
    an indication of successful operation to a personal email.'''
    msg = EmailMessage()

    msg['Subject'] = 'Update on Daily Prediction'
    msg['From'] = settings.email_address
    msg['To'] = "michaeligbomezie@gmail.com"

    response = requests.get("http://127.0.0.1:8000/predict")
    message = response.json()
    msg.set_content(message["message"])

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(settings.email_address, settings.email_password)
        smtp.send_message(msg)

    print("Daily Prediction Sucessful!")


def trigger():
    '''Trigger function for the task schedule.'''
    
    app()
    
    schedule.every(2).minutes.do(app)
    #schedule.every(24).hours.do(app)

    while True:
        # Checks whether a scheduled task is pending to run or not
        schedule.run_pending()
        time.sleep(5)


trigger()


