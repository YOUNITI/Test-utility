import requests

def send_request(url, method,):
    try:
        response = requests.request(method,url, timeout=5)
        
        
        
        return(response)
        
    except OSError:
        return None
    
