import requests
import os

def download(filename):
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            res = requests.get(URL)
            f.write(res.text)

def main():
    filename = "../weather_146_2020.csv"
    download(filename)

if __name__ == "__main__" :
    main()