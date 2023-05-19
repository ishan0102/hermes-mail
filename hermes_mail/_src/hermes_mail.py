import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

# Set up logging with metadata
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def validate_email(email: str) -> bool:
    """Validate an email address.

    Args:
        email (str): An email address.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    import re

    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return True if pattern.match(email) else False


class Client:
    """
    A class for sending emails via Gmail.

    Args:
        sender_email (str): The sender's email address.
        password (str): The password for the sender's email account.

    Attributes:
        sender_email (str): The sender's email address.
        password (str): The password for the sender's email account.

    """

    def __init__(self, sender_email: str, password: str):
        self.logger = logging.getLogger(__name__)
        self.sender_email = sender_email
        if not self.sender_email:
            raise ValueError("No sender email provided during initialization.")

        if not validate_email(self.sender_email):
            raise ValueError("Invalid sender email provided. Must be a valid email address.")

        self.password = password
        if not self.password:
            raise ValueError("No password provided during initialization.")

    def send_email(self, receiver_emails: List[str], subject: str = "Empty subject", body: str = "Empty body"):
        """Send an email via Gmail.

        Args:
            receiver_email (List[str]): A list of receiver's email addresses.
            subject (str): The subject line of the email.
            body (str): The body text of the email.

        Returns:
            None.
        """
        # Validate inputs
        if not type(receiver_emails) == list:
            raise ValueError("receiver_emails must be a list of receiver emails.")

        if not receiver_emails:
            raise ValueError("No receiver emails provided.")

        for receiver_email in receiver_emails:
            if not validate_email(receiver_email):
                raise ValueError("Invalid receiver email provided. Must be valid email addresses.")

        # Create email
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = ", ".join(receiver_emails)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_emails, text)
                self.logger.info("\033[32mEmail sent successfully to {}\033[0m".format(", ".join(receiver_emails)))
        except Exception as e:
            self.logger.error("\033[31mFailed to send email. Error: {}\033[0m".format(str(e)))
