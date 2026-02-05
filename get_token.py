import requests
import base64
from dotenv import load_dotenv
import os
import random

load_dotenv() #.env 일을 찾아 그 안에 정의된 변수들을 시스템 환경 변수로 등록

tenantId = os.getenv("NHNCloud_tenantID")
nhnClouduserId = os.getenv("NHNCloud_ID")
nhnClouduserPass = os.getenv("NHNCloudpass")

if not tenantId :
    raise RuntimeError("CSP API credentials not set")

url = "https://api-identity-infrastructure.nhncloudservice.com"
uri = "/v2.0/tokens"

data = {
    "auth": {
        "tenantId": tenantId ,
        "passwordCredentials": {
            "username": nhnClouduserId,
            "password": nhnClouduserPass
        }
    }
}

response = requests.post(url + uri,json=data)
token_info = response.json()
access_token = token_info['access']['token']['id']  
