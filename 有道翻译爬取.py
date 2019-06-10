from selenium import webdriver
import time

options= webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.get("http://fanyi.youdao.com/")
word = input("请输入需翻译的文本：")
input = browser.find_element_by_id("inputOriginal")
input.send_keys(word)
time.sleep(1)
output = browser.find_element_by_id("transTarget")
print("该文本经有道翻译为：%s" % output.text)
browser.close()