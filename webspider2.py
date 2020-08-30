from urllib.parse import urlencode
from tqdm import tqdm
from time import sleep
import time
import requests
import re
import os
import time
import sys
save_dir = r'E:\Projects\Information\video/'

url = "http://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/75/36/140153675/140153675-1-30033.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1578287443&gen=playurl&os=kodobv&oi=1912288006&trid=ecb22ab653a94ee08a97621384915475u&platform=pc&upsig=e45a5c15abe2f514535393c6fe586229&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=22235846"
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
   "Connection": "keep-alive",
   "Origin": "null",
   "Referer": "https://www.bilibili.com/video/av81907143?spm_id_from=333.851.b_7265706f7274466972737431.9",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   "Accept-Language": "zh-CN,zh;q=0.9"}
def download(url,av):
    try:
        data=requests.get(url=url,headers=headers,stream=True)
        content_size=int(data.headers['Content-Length'])/1024
        file_path = save_dir + '{}.{}'.format(av,'m4s')
        if not os.path.exists(file_path):
            with open(file_path,'wb') as d:
                print("下载中")
                for data in tqdm(iterable=data.iter_content(1024),total=content_size,unit='k'):
                    d.write(data)
                    d.flush()
                print("下载成功")
    except requests.ConnectionError:
        print("下载失败")

if __name__=='__main__':
    av='3'
    download(url,av)