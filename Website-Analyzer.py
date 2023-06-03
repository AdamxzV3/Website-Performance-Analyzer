import requests
import time

def analyze_website_performance():
    url = input("Enter the website URL: ")

    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        load_time = end_time - start_time

        num_requests = len(response.history) + 1

        resource_sizes = []
        for url in response.history + [response.url]:
            resource_sizes.append(len(requests.get(url).content))

        print("Website Performance Metrics:")
        print("URL:", response.url)
        print("Page Load Time:", round(load_time, 2), "seconds")
        print("Number of Requests:", num_requests)
        print("Resource Sizes:", resource_sizes)
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

analyze_website_performance()
