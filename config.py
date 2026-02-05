import nhn_get_token

BASE_URL = "https://kr1-api-network-infrastructure.nhncloudservice.com"

TENANT_ID = nhn_get_token.tenantId
ACCESS_TOKEN = nhn_get_token.access_token

HEADERS = {
    "X-Auth-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
