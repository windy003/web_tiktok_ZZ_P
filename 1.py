from playwright.sync_api import sync_playwright
import time
import traceback
import json

# 使用 Playwright 启动浏览器
with sync_playwright() as p:
    # 创建浏览器实例
    browser = p.chromium.launch_persistent_context(
        user_data_dir='./chrome_data',
        headless=False
    )
    page = browser.new_page()

with open("tiff-5.txt", "r", encoding="utf-8") as f:
    data = {}  # 初始化空字典
    
    for line in f:
        url = line.strip()
        page.goto(url)

        # 获取描述
        desc = page.locator('xpath=//div[@data-e2e="video-desc"]')
        print(desc)
        desc_text = desc.text_content() if desc else None
        print(desc_text)

        # 获取发布时间
        pub_time_link = page.locator('xpath=//a[contains(@class, "css-qvpt8d-StyledAuthorAnchor") and contains(@class, "e1g2yhv81") and contains(@class, "link-a11y-focus")]')
        print(pub_time_link)
        pub_time = pub_time_link.text_content() if pub_time_link else None
        print(pub_time)

        # 将数据存入字典
        data[url] = {
            'desc': desc_text,
            'pub_time': pub_time
        }

with open("1.json", "a", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)  # 添加indent参数使json文件更易读


