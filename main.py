import get_token
from vpc import create_vpc
from subnet import create_subnet

res = create_vpc(
    name="api-vpc",
    cidr="10.10.0.0/16"
)
sub_res = create_subnet(res['vpc']['id'],'api-sub','10.10.0.0/24')
print(res['vpc']['id'])

print(sub_res)
