# config.py
import os

COGNITO_REGION     = os.environ.get("COGNITO_REGION", "us-east-1")
COGNITO_CLIENT_ID  = os.environ.get("COGNITO_CLIENT_ID", "ve8d0lmgfgdqshb4uphr5g8gj")
API_BASE_URL       = os.environ.get("API_BASE_URL", "https://tvdboyoxti.execute-api.me-south-1.amazonaws.com/prod")

AWS_ACCESS_KEY_ID     = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_SESSION_TOKEN     = os.environ.get("AWS_SESSION_TOKEN", None)
