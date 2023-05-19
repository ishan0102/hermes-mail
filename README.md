# Hermes Mail
Send Python job alerts via email.

```python
from hermes_mail import Client

hermes = Client(sender_email="mlguy@gmail.com", password=os.getenv("GMAIL_PASSWORD"))
hermes.send_email(
    receiver_emails=["foo@gmail.com", "bar@gmail.com"], 
    subject="cuda:0 is free", 
    body="I finished training my models on cuda:0 so feel free to use it.")
```
`hermes_mail` works seamlessly within Python code to send emails. It is designed for sending job alerts upon completion of long-running jobs. This currently only works when the sender is a Gmail account.

## Installation
```bash
pip install hermes-mail
```

1. Navigate to [Google Account Security](https://myaccount.google.com/security) and ensure that 2-Step Verification is enabled.
2. Create a [Google Account App Password](https://myaccount.google.com/apppasswords) for `hermes_mail` and save it somewhere. This is the password that you will use to initialize `hermes_mail.Client`.

Now you should be able to send emails using `hermes_mail`!