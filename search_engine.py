"""Module uses search engine to search and open selected links."""

import random
import time
import sys
import re
import json
import os
from pprint import pprint
import requests

from urllib.parse import quote
from bs4 import BeautifulSoup
import playwright
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

_SUBSCRIPTION_KEY = os.getenv("BING_KEY")


def url_open_v1(
    target_url,
    proxy_list=None,
    show_log=False,
):
    sleeptime = random.randint(15, 18)
    time.sleep(sleeptime)
    if proxy_list is None:
        proxy_list = [
            "socks5://20.188.24.63:7888",  # u, iot1
            # "socks5://20.210.233.19:7888", # up, block by stackoverflow
            "socks5://20.210.232.178:7888",  # up, iot3
            "socks5://20.40.99.118:7888",  # up, node4
            "socks5://20.210.194.108:7888",  # up, node5
        ]

    with sync_playwright() as playwright:
        try:
            last_time = time.time()

            chromium_browser_type = playwright.chromium
            cur_proxy = random.choice(proxy_list)
            print(cur_proxy)

            if show_log:
                print("\n" + "-" * 40 + "\ncur_page:", target_url)
                print("cur_proxy: ", cur_proxy)
            browser = chromium_browser_type.launch(
                headless=True,
                args=[
                    # "--proxy-server=" + cur_proxy,
                    "--headless",
                    "--disable-setuid-sandbox",
                    "--single-process",
                    "--window-size=1920,1080",
                    "--no-sandbox",
                    "--no-zygote",
                    "--no-first-run",
                    "--window-position=0,0",
                    "--ignore-certificate-errors",
                    "--ignore-certificate-errors-skip-list",
                    "--disable-gpu",
                    "--hide-scrollbars",
                    "--mute-audio",
                    "--enable-features=NetworkService,NetworkServiceInProcess",
                ],
            )
            cur_time = time.time()
            if show_log:
                print(f"browser.launch(): \t\t\t{round(cur_time - last_time, 2)}")
            last_time = cur_time
            context = browser.new_context()
            page = context.new_page()
            stealth_sync(page)  # ------STEALTH------
            page.goto(target_url, timeout=20000)
            # page.goto(target_url)
            cur_time = time.time()
            if show_log:
                print(f"page.goto(): \t\t\t\t{round(cur_time - last_time, 2)}")
            last_time = cur_time
            page.wait_for_load_state(
                # state='networkidle',
                state="domcontentloaded",
                # state='load',
                timeout=5000,
            )
            cur_time = time.time()
            if show_log:
                print(f"wait_for_load_time(): {round(cur_time - last_time, 2)}")
            html_page = page.content()
            # page.wait_for_timeout(1000 * solid_timespan)
            page.close()
            context.close()
            browser.close()
            if show_log:
                print("File len: ", len(html_page))
                if len(html_page) > 200000:
                    print("\tSeems all right.")
                else:
                    print("\t[WARNING!] Maybe detected!")
            return html_page
        except Exception as ex:
            print(ex)
            return ""


def search(query_str):
    try:
        query_str = quote(query_str)
    except Exception:
        query_str = quote(query_str.encode("utf-8", "ignore") + " language:en")
    # remove &lr=lang_en because GPT can handle, more paras: num=20
    url = "https://www.google.com/search?q=%s&hl=en" % query_str
    # In case you want to use Bing as the search engine:
    # url = "https://www.bing.com/search?q=%s&setmkt=en-us&setlang=en-us"
    # more paras:cc=us&setlang=en for Bing
    print("Search Url: ", url)
    res_html = url_open_v1(url)
    return res_html


def random_sleep():
    sleeptime = random.randint(20, 23)
    time.sleep(sleeptime)


def extract_search_results(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    card_section = soup.find("div", {"class": "card-section"})
    if card_section:
        card_text = card_section.getText()
        print(card_text)
        if (
            "did not match any documents" in card_text
            or "No results found" in card_text
        ):
            return [""]

    div = soup.find("div", id="search")

    if type(div) != type(None):
        lis = div.findAll("div", {"class": "MjjYud"})
        if len(lis) > 0:
            for li in lis:
                out = {}
                out["type"] = "webpage"
                h3 = li.find("h3", {"class": "LC20lb MBeuO DKV0Md"})
                if h3 is None:
                    continue
                out["title"] = h3.getText()
                if type(h3) == type(None):
                    continue

                # if you want to get the url
                link = li.find(
                    # "div", {"class": "TbwUpd NJjxre iUh30 ojE3Fb"}
                    # get url class
                    "div",
                    {"class": "yuRUbf"},
                )
                try:
                    link = link.find("a")
                except:
                    print("fail")
                    continue
                if type(link) == type(None):
                    continue
                # print(link)
                out["url"] = link["href"]
                span = li.find(
                    "div",
                    {"class": "VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb"},
                )

                if type(span) != type(None):
                    content = span.getText()
                    out["text"] = content
                    # print content
                else:
                    span = li.find(
                        "div",
                        {"class": "VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf"},
                    )
                    if type(span) != type(None):
                        content = span.getText()
                        out["text"] = content

                results.append(out)
                print(out)

        lis = div.findAll("div", {"class": "XN9cAe"})
        if len(lis) > 0:
            for li in lis:
                out = {}
                out["type"] = "webpage"
                h3 = li.find("h3", {"class": "LC20lb MBeuO DKV0Md"})
                if h3 is None:
                    continue
                out["title"] = h3.getText()
                if type(h3) == type(None):
                    continue

                # In case, you want get the url
                link = li.find("a")
                if type(link) == type(None):
                    continue
                print(link)
                # raise ValueError
                out["url"] = link["href"]

                span = li.find("div", {"class": "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"})
                if type(span) != type(None):
                    content = span.getText()
                    out["text"] = content
                else:
                    span = li.find(
                        "div",
                        {"class": "VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf"},
                    )
                    if type(span) != type(None):
                        content = span.getText()
                        out["text"] = content
                results.append(out)
                print("Google Search Results: ")
                print(out)
    return results


def bing_search(query_str, debug=False):
    """
    This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
    """

    # Add your Bing Search V7 subscription key and endpoint to your environment variables.
    
    endpoint = "https://api.bing.microsoft.com" + "/v7.0/search"

    # Construct a request
    mkt = "en-US"
    params = {"q": query_str, "mkt": mkt}
    headers = {"Ocp-Apim-Subscription-Key": _SUBSCRIPTION_KEY}

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        if debug:
            print("Headers:")
            print(response.headers)
            print("JSON Response:")
            pprint(response.json())
    except Exception as ex:
        raise ex
    out = []
    for page in response.json()["webPages"]["value"]:
        page_info = {}
        page_info["title"] = page["name"]
        page_info["url"] = page["url"]
        page_info["text"] = page["snippet"]
        page_info["type"] = "webpage"
        out.append(page_info)
    return out


def google_web_search(t_keywords):
    if len(t_keywords) > 100:
        return [""]

    html = search(t_keywords)
    res = extract_search_results(html)
    if len(html) > 200000:
        if not res:
            res = [""]
        out = {}
        out["query"] = t_keywords
        out["results"] = res
    else:
        sys.stderr.write("..... search again ...")
        random_sleep()
        html = search(t_keywords)
        res = extract_search_results(html)
        if len(html) > 200000:
            if not res:
                res = [""]
            out = {}
            out["query"] = t_keywords
            out["results"] = res
            # mc.set(t_keywords.replace(" ", "+"), res)
            # file_db.write(json.dumps(out) + "\n")
        return res
    return res


def extract_text(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    return text
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(cleaned_lines)


def remove_html_tags(html_text):
    soup = BeautifulSoup(html_text, "html.parser")

    for tag in soup(["script", "style", "meta"]):
        tag.decompose()

    # Get the cleaned HTML
    cleaned_html = soup.prettify()
    return cleaned_html

    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(cleaned_lines)


def click(num, all_res):
    url_link = all_res[num]["url"]
    print("Click Link: ", url_link)
    res_html = url_open_v1(url_link)
    res = remove_html_tags(res_html)
    print("Raw Page: ", res)
    out = all_res[num]
    out["text"] = res
    return out


def click_into_page(url):
    res_html = url_open_v1(url)
    # print(res_html)
    res = remove_html_tags(res_html)
    res = re.sub(r"\s+", " ", res)
    return res


def click_into_page_original(url):
    res_html = url_open_v1(url)
    # print(res_html)
    res = extract_text(res_html)
    res = re.sub(r"\s+", " ", res)
    return res


def url_open_with_browser(link, headless_flag=False):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless_flag
        )  # or p.firefox.launch() or p.webkit.launch()
        page = browser.new_page()
        try:
            page.goto(link, wait_until="domcontentloaded")
        except playwright._impl._errors.TimeoutError:
            browser.close()
            return ""
        html = page.content()
        browser.close()
        return html


def click_into_page_with_browser(url, is_text=True, headless_flag=False):
    res_html = url_open_with_browser(url, headless_flag=headless_flag)
    if is_text:
        return extract_text(res_html)
    res = remove_html_tags(res_html)
    res = re.sub(r"\s+", " ", res)
    return res


if __name__ == "__main__":
    a = click_into_page_with_browser("https://github.com/DesktopECHO/T95-H616-Malware")
    bing_search("get nccl version")
