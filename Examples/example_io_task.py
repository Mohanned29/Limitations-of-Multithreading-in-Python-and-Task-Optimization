from SmartExecutor.core import run
import requests
# web scarping
def fetch_website(url):
    response = requests.get(url)
    return response.status_code, len(response.content)

if __name__ == "__main__":
    url = "https://www.example.com" # url apr nchof m3ah
    status, content_length = run(fetch_website, url)
    print(f"Status: {status}, Taille du contenu: {content_length} octets")
