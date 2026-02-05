from nhn_api_client import nhn_api_call
import nhn_uris as uri

def create_vpc(name: str, cidr: str):
    data = {
        "vpc": {
            "name": name,
            "cidrv4": cidr
        }
    }

    return nhn_api_call(
        method="POST",
        uri=uri.CREATE_VPC,
        data=data
    )
