
def report(return_dict):


    print(f"Testing URL: {return_dict.get("URL")}\n")
    print(f"Testing method: {return_dict.get("Method")}\n")
    print("Test Output\n")
    print(f"Status group: {return_dict.get("Status group")}\n")
    print(f"Status code: {return_dict.get("Status code")}\n")
    print(f"Time: {return_dict.get("Time")}\n")
    print(f"Type content: {return_dict.get("Type")}\n")
    print(f"Content_lenght: {return_dict.get("Content_lenght")}\n")
    print(f"Headers: {return_dict.get("Headers")}\n")
    print(f"Json: {return_dict.get("is_json")}\n")
    body = return_dict.get("body")
    short_body = body[:50] + "..." if body else "[Тело отсутсвует]"
    print(f"Body: {short_body}\n")

    