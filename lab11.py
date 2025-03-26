import requests #Import thư viện
import json #Import thư viện JSON

def get_ticket(): #Khai báo tên hàm
    url = "http://10.215.26.60/api/v1/ticket" #Khai báo thông tin địa chỉ nguồn truy cập lấy Ticket.
    header = {
        "content-type" : "application/json"
    }
    body = json.dumps({ #ép kiểu dict -> json
        "username": "admin",
        "password" : "vnpro@123"
    })

    #Lấy ticket
    responses = requests.post(url, headers = header, data= body, verify= False) #thực hiện gửi yêu cầu tạo ticket và trả về kết quả
    data = responses.json()
    print(json.dumps(data, indent=4))
    ticket = data['response']['serviceTicket'] #Truy cập vào dữ liệu bên trong để lấy ticket.
    print(ticket) 
    return ticket

#get_ticket()

def get_list_device():
    url1 = "http://10.215.26.60/api/v1/network-device"

    header = {
        "x-auth-token": get_ticket()
    }

    #Lấy danh sách thiết bị
    responses_device = requests.get(url1, headers = header, verify = False)
    print (responses_device)
    data = responses_device.json()
    print(json.dumps(data, indent = 4))
    return data

get_list_device()
