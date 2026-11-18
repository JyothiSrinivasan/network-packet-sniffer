import subprocess
import time

TEST_URLS = [
    "http://example.com/",
    "http://example.com/test-one",
    "http://example.com/test-two",
    "http://neverssl.com/",
    "http://httpbin.org/get",
]

for url in TEST_URLS:
    print(f"\nRequesting: {url}")

    subprocess.run([
        "curl.exe",
        "-4",                 # Use IPv4, which our sniffer checks
        "--max-time", "10",
        "-sS",
        "-o", "NUL",          # Don't print the webpage
        "-w", "HTTP status: %{http_code}\n",
        url,
    ])

    time.sleep(2)