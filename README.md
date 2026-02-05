# nhnCloudMaker

NHN Cloud Network API(VPC, Subnet 등)를  
Python 코드로 쉽게 제어하기 위한 경량 SDK / 자동화 도구입니다.

Terraform처럼 무겁지 않고,  
교육·실습·사내 자동화 스크립트 용도로 사용하기 좋도록 설계되었습니다.

복잡한 네트워크 설정을 한번에 생성할 수 있도록 구현했습니다. 

---

## Features

- VPC 생성
- Subnet 생성
- 공통 API Client 구조
- Token 기반 인증
- 확장 가능한 URI / API 구조

---

## Project Structure

```text
nhncloudmaker/
├── api_client.py    # 공통 API 호출 로직
├── config.py        # 환경 설정
├── auth.py          # 인증 / 토큰 처리
├── uris.py          # API Endpoint 모음
├── vpc.py           # VPC 관련 API
└── subnet.py        # Subnet 관련 API

examples/
└── create_vpc_and_subnet.py
