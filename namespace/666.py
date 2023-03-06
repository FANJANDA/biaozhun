import os
import requests
from bs4 import BeautifulSoup

# 需要爬取的图片的标签
tag = "landscape"

# 图片保存的路径
folder_path = "wallhaven_images"

# 如果文件夹不存在，则创建一个新的文件夹
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 发送 HTTP 请求并获取 HTML 页面
url = f"https://wallhaven.cc/search?q={tag}&categories=111&purity=100&sorting=random&order=desc"
response = requests.get(url)
html_content = response.content

# 解析 HTML 页面
soup = BeautifulSoup(html_content, 'html.parser')

# 获取所有的图片元素
images = soup.find_all('img', class_='lazyload')

# 遍历每个图片，保存图片到本地
for index, image in enumerate(images):
    # 获取图片的 URL
    image_url = image.get('data-src')

    # 发送 HTTP 请求并获取图片的二进制数据
    image_response = requests.get(image_url)
    image_content = image_response.content

    # 保存图片到本地
    file_path = os.path.join(folder_path, f"{tag}_{index + 1}.jpg")
    with open(file_path, 'wb') as f:
        f.write(image_content)

    print(f"图片 {index + 1} 已保存到 {file_path}。")
