import random
import time
import requests

# daftar link tujuan yang akan dijadwalkan
links = ["https://lofiamity-traf1-main-p5wzjz.streamlit.app/", "https://lofiamity-rem1bg-main-owrrs8.streamlit.app/"]

# fungsi untuk mengakses link secara acak
def access_random_link():
    # memilih link secara acak dari daftar links
    link = random.choice(links)
    try:
        # mengakses link menggunakan library requests
        response = requests.get(link)
        print("Accessed link:", link, "with status code:", response.status_code)
    except:
        print("Failed to access link:", link)

# menjadwalkan akses ke link setiap 5 detik
while True:
    access_random_link()
    time.sleep(150)
