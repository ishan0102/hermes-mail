# Hermes Mail
Get an email when your Python jobs are done instead of checking your terminal.

```python
from hermes_mail import EmailClient

# Set up the email client
hermes = EmailClient(sender_email="mlguy@gmail.com", sender_password="12345678")

# Call this function when your job is done
hermes.send_email(
    receiver_emails=["foo@gmail.com", "bar@gmail.com"], 
    subject="cuda:0 is free", 
    body="I finished training my models on cuda:0 so feel free to use it."
)
```
`hermes_mail` integrates seamlessly with Python, saving you the hassle of SSH-ing into your server to check on your jobs. As of now, this package is only available for Gmail accounts.

## Quick Start
```bash
pip install hermes-mail
```

To get started:
1. Navigate to [Google Account Security](https://myaccount.google.com/security) and ensure that 2-Step Verification is enabled.
2. Create a [Google Account App Password](https://myaccount.google.com/apppasswords) for `hermes_mail` and save it somewhere. This is the password that you will use to initialize `hermes_mail.Client`.

With these two easy steps, you're ready to start sending notifications from `hermes_mail`!