from flask import Flask, render_template, request, redirect
from azure.communication.email import EmailClient
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-feedback', methods=['POST'])
def send_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    send_email(name, email, message)
    return redirect('/')

def send_email(name, email, message):
    try:
        # Azure Communication Services setup
        connection_string = os.getenv('AZURE_EMAIL_CONNECTION_STRING')
        client = EmailClient.from_connection_string(connection_string)
        
        message = {
            "senderAddress": "DoNotReply@fd42e661-b94d-4d0d-9d9c-692c9273a2be.azurecomm.net",
            "recipients":  {
                "to": [{"address": "jdowns06@gmail.com" }],
            },
            "content": {
                "subject": "Flask App Feedback",
                "plainText": f"Name: {name} \nEmail: {email} \nMessage: {message}",
            }
        }

        print(f"Sending email message: {message}")
        poller = client.begin_send(message)
        result = poller.result()
        print(f"Email sent result: {result}")

    except Exception as ex:
        print(f"Exception: {ex}")    

if __name__ == '__main__':
    app.run(debug=True)
