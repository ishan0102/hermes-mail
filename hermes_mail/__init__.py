from ._src.hermes_mail import EmailClient

# Make the functions accessible with from rsrch import *
__all__ = ["EmailClient"]

# Make the functions directly accessible under the package namespace
EmailClient = EmailClient
