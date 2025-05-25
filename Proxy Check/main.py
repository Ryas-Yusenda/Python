import requests
import time
import json


def check_proxy(proxy, url, attempts=3):
    proxies = {"http": proxy, "https": proxy}
    times = []

    for _ in range(attempts):
        try:
            start = time.time()
            response = requests.get(url, proxies=proxies, timeout=5)
            elapsed = time.time() - start
            if response.status_code == 200:
                times.append(elapsed)
        except requests.RequestException:
            pass

    if len(times) == attempts:
        avg_time = sum(times) / attempts
        return proxy, avg_time
    return None


def main():
    url = "https://www.google.com"
    proxy_list = [
        "109.163.231.187:8080",
        "177.234.209.80:999",
        "177.234.209.84:999",
        "177.234.209.87:999",
        "177.234.209.81:999",
        "37.220.139.219:8080",
        "98.8.195.160:443",
        "177.234.209.82:999",
        "35.176.148.8:1080",
        "177.234.209.83:999",
        "177.234.209.85:999",
        "177.234.209.86:999",
        "51.68.175.56:1080",
        "45.186.6.104:3128",
        "120.77.34.183:5980",
    ]

    working_proxies = []
    for proxy in proxy_list:
        result = check_proxy(proxy, url)
        if result and result[1] < 5:
            working_proxies.append(result)

    working_proxies.sort(key=lambda x: x[1])

    with open("working_proxies.json", "w") as f:
        json.dump({"proxies": working_proxies}, f, indent=4)


if __name__ == "__main__":
    main()
