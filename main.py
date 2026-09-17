import requester
import analyzer
import reporter

def main():
        
    url = input("Enter URL: ")
    while True:
        Method = input("Enter method: ")
        if not Method:
            print("Строка пустая")
            continue
        method = Method.strip().upper()
        break

    print(f"\n Sending {method} response on {url}")

    response = requester.send_request(url,method)
    
    if response is None:
        print("Error: problem with connect")
    else:
        report_dict = analyzer.analyze(response)

        reporter.report(report_dict)
        



if __name__ == "__main__":
        main()