import requests
from config import BASE_URL, HEADERS

def nhn_api_call(
    method: str,
    uri: str,
    data: dict | None = None,
    params: dict | None = None
):
    """
    NHN Cloud 공통 API 호출 함수
    """
    url = f"{BASE_URL}{uri}"

    response = requests.request(
        method=method,
        url=url,
        headers=HEADERS,
        json=data,
        params=params
    )

    if not response.ok:
        raise Exception(
            f"NHN API Error [{response.status_code}]: {response.text}"
        )

    return response.json()
