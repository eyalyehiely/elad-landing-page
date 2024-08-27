from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
# app.secret_key = 'fghdfghdfefbgrgbrgbdfgbndfgndfnrhwrglwehg;qeorghpoeuhrg9q3h39t3y355723yt3giuerhiefvbiaefbgh'

# Configuration for mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'manor.elad1@gmail.com'
app.config['MAIL_PASSWORD'] = 'ubtn fgzf lguy ludg'

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Create message object
        msg = Message(subject=f"You got a new message from {name}, email:{email}",
                      sender=('ההרצאה שלי', 'manor.elad1@gmail.com'),
                      recipients=["manor.elad1@gmail.com"])
        msg.body = message

        # Send email
        mail.send(msg)
        return "Email sent successfully! thank you"
    except:
        return "Error, please try again"


if __name__ == '__main__':
    app.run(debug=True)
