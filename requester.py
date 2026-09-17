import requests
import analyzer
def send_request(url, method,):
    try:
        response = requests.request(method,url, timeout=5)
        
        
        analyzer.analyze(response)
        
        return(response)
        
    except OSError:
        return(None)
    
