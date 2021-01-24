# 发送一个请求
import urllib.request
# 转码模块
import chardet

# 抓取并读写
html = urllib.request.urlopen('http://www.baidu.com').read()

# 二进制转字符串
html.decode('utf-8')

# 创建文件并存入
file = open('baidu.html','wb')
file.write(html)
file.close()
