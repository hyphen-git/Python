import requests

web_url = [
    "https://vercel.com/",
    "https://www.python.org/",
    "https://www.apple.com/in/"
]

web_status = {

    200: "websites available",
    301: "permenant redirect",
    404: "not found"

}


for url in web_url:
    try:
        web_responses = requests.get(url)
        print(url, web_status[web_responses.status_code])
    except:
        print(url, web_status[web_responses.status_code])
