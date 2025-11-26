# config.py
import os

COGNITO_REGION     = os.environ.get("COGNITO_REGION", "us-east-1")
COGNITO_CLIENT_ID  = os.environ.get("COGNITO_CLIENT_ID", "")
API_BASE_URL       = os.environ.get("API_BASE_URL", "")

AWS_ACCESS_KEY_ID     = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_SESSION_TOKEN     = os.environ.get("AWS_SESSION_TOKEN", None)
