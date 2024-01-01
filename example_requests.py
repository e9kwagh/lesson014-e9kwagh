"""This will run and execute but will take lot of time need to work on this """
import requests
import random
import re


def extractor(main_link):
    """extractor"""
    try:
        data = requests.get(main_link)
        text_data = data.text
        url_pattern = re.compile(r'https?://[^\s<>"\']+')
        final_list = url_pattern.findall(text_data)
        return final_list

    except Exception as e:
        return []


def check_status(link, status_dict):
    """check status :  check the status code"""
    try:
        check_link = requests.get(link)
        check_val = check_link.status_code
        if check_val in status_dict:
            status_dict[check_val].append(link)
        else:
            status_dict[check_val] = [link]

    except Exception as e:
        if "error" not in status_dict:
            status_dict["error"] = [link]
        else:
            status_dict["error"].append(link)


def scrape_site():
    """generates the random"""
    try:
        main_link = "https://httpbin.org"
        initial_urls = extractor(main_link)

        all_urls = []
        for url in initial_urls:
            additional_urls = extractor(url)
            all_urls.extend(additional_urls)

        num_urls_to_select = max(len(all_urls) // 2, 100)
        selected_urls = random.sample(all_urls, num_urls_to_select)
        return selected_urls
    except Exception as e:
        return []


def catalog_urls(urls):
    """runns iternations"""

    status_dict = {}
    iterations = 1
    for i in range(iterations):
        for url in urls:
            check_status(url, status_dict)

    return status_dict


if __name__ == "__main__":
    urls = scrape_site()
    status_dict = catalog_urls(urls)
    print("Status Dictionary:", status_dict)
