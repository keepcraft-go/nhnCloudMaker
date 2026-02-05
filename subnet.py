from nhn_api_client import nhn_api_call
import uris as uri

def create_subnet(vpc_id: str, name: str, cidr: str):
    data = {
        "vpcsubnet": {
            "vpc_id": vpc_id,
            "name": name,
            "cidr": cidr
        }
    }

    return nhn_api_call(
        method="POST",
        uri=uri.CREATE_SUBNET,
        data=data
    )
