import requester
import reporter
status_dict = {
    '1': "info",
    '2': "success",
    '3': "redirect",
    '4': "client error",
    '5': "server error"
}

def analyze(response):
    return_dict = {}

    status_number = str(response.status_code)[0]
    content_length = len(response.content)
    


    return_dict.update({"URL": response.url, "Method" : response.request.method, "Status code" : response.status_code, "Time": response.elapsed.total_seconds(), "Status group":status_dict[status_number],"Type" :response.headers.get('content-type'),"Content_lenght" :content_length,"Headers" : response.headers})
    try:
        
        return_dict["body"] = response.json()
        return_dict["is_json"] = True
    except ValueError:
        return_dict["body"] = response.text
        return_dict["is_json"] = False

    reporter.report(return_dict)
    return(return_dict)
    
        