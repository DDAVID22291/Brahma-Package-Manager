from hashlib import sha256
import sys
import requests


def http_download(url, expected_hash=None):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    if expected_hash:
        actual_hash = sha256(response.content).hexdigest()
        if expected_hash != actual_hash:
            print("Expected hash:\t", expected_hash)
            print("Actual hash:\t", actual_hash)
            print("File", file_name, "may be corrupted")
            sys.exit("Error: hash mismatch")

    with open(file_name, "wb") as output_file:
        output_file.write(response.content)


# def git_download(url):
