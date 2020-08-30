import re
from urllib import response
import xlwt
import requests
from bs4 import BeautifulSoup
#
# url1 = "https://www.baidu.com/"
# url2 = "www.baidu.com/https://"
# url3 = "https:www.baidu.com/"
#
# print(re.match('https://', url1))
# print(re.match('https://', url2))
# print(re.match('https://', url3))



def send_req(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    for k in soup.find_all('a',class_="news-stream-newsStream-image-link"):
        a = re.findall('title="(.*?)">', str(k))  # 标题
        b = re.findall('href="(.*?)"', str(k))  # 链接
        t = s.join(a)
        l = 'https:' + s.join(b)
        lista.append(t)  # 将标题放入lista中
        listb.append(l)  # 将链接放入listb中
        # print(t,l)
    col1_data = lista
    col2_data = listb
    for m in range(len(col1_data)):
        worksheet.write(m+1,0,col1_data[m])
    for n in range(len(col2_data)):
        worksheet.write(n+1,1,col2_data[n])
    workbook.save("D:\spider1.xls")
    print("爬取成功")



if __name__ == '__main__':
    url = "https://news.ifeng.com/"
    s = " "
    lista = []
    listb = []
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test')
    col1 = worksheet.col(0)
    col1.width = 256 * 38
    col2 = worksheet.col(1)
    col2.width = 256 * 85
    row0 = [u'标题', u'链接']
    for i in range(0, len(row0)):
        worksheet.write(0, i, row0[i])
    send_req(url)
