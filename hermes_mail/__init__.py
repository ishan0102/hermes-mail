from ._src.hermes_mail import Client

# Make the functions accessible with from rsrch import *
__all__ = ["Client"]

# Make the functions directly accessible under the package namespace
Client = Client
