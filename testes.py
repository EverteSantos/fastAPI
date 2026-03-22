import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3IiwiZXhwIjoxNzc0NzU1NTcyfQ.GEXTxFUtqaRxTcu8OVL8x-LGeX07NT3YELhmvmxgE2Y"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())