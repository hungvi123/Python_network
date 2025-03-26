import requests
import json
requests.packages.urllib3.disable_warnings() # tắt cảnh báo SSL

base_url = "https://sandboxdnac.cisco.com/" #base_url: đường dẫn cơ sở (ở đây sử dụng sanbox của Cisco)

# tạo một hàm để trả về token khi xác thực thành công
def get_token():
    url = base_url + 'dna/system/api/v1/auth/token'
    header = {
        "Authorization" : "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
        "Content-Type" : "application/json"
    }

    response = requests.post(url, headers=header, verify=False)
    #print(response.json())
    data = response.json()['Token']
    return data
get_token()
def get_network():
    url = base_url + 'dna/intent/api/v1/network-device'
    header = {
        'x-auth-token': get_token()
    }
    response = requests.get(url, headers=header, verify=False)
    data = response.json()
    print(json.dumps(data, indent=4)) # định dạng lại với thông số thích hợp ở đây mình chọn là 4 ( khoảng cách giữa các tab)
get_network()

