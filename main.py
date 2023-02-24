import random
import time
import requests

# daftar link tujuan yang akan dijadwalkan
links = ["https://lofiamity-traf1-main-p5wzjz.streamlit.app/", "https://lofiamity-rem1bg-main-owrrs8.streamlit.app/"]

# daftar useragent yang akan digunakan secara acak
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]

# fungsi untuk mengakses link secara acak dengan useragent acak
def access_random_link():
    # memilih link secara acak dari daftar links
    link = random.choice(links)
    # memilih useragent secara acak dari daftar user_agents
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    try:
        # mengakses link menggunakan library requests
        response = requests.get(link, headers=headers)
        print("Accessed link:", link, "with status code:", response.status_code)
    except:
        print("Failed to access link:", link)

# menjadwalkan akses ke link setiap 100 detik
while True:
    access_random_link()
    time.sleep(100)
