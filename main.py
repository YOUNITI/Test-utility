import requester
import requests

def main():
        
    url = input("Enter URL: ")
    while True:
        Method = input("Enter method: ")
        if not Method:
            print("Строка пустая")
            continue
        method = Method.strip().upper()
        break
    response = requester.send_request(url, method)
    if response is None:
        print("Ошибка")
    else:
        None
        #print(response.status_code, response.elapsed.total_seconds())



if __name__ == "__main__":
        main()