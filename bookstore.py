import requests
from bs4 import BeautifulSoup
import shutil


res = requests.get('https://www.books.com.tw/web/sys_bbotm/books/020806/?o=1&page=1') #放入要爬取的網頁
soup = BeautifulSoup(res.text, 'html.parser')
#接下來找網頁選取的標的
for pictures in soup.select('.cover'):    #.cover後面的，會被選出來
    fname = pictures['src'].split('/')[-1].split('&')[0]    #取得圖檔名稱
    res2 = requests.get(pictures['src'].split('i=')[1].split('&')[0], stream=True) #處理圖片網址
                                                      							   #新增參數 stream=True 來強制解壓縮，並且可以避免立即將大的 response 內容讀入記憶體內
    pics = open(fname,'wb')    #將取得的圖檔暫存到pics(only寫入電腦沒有create). write binary
    shutil.copyfileobj(res2.raw,pics)。  #import shutil將res2下載的copy檔案到電腦 
    pics.close()    #要有close才會讀到電腦
# test = soup.select('.cover')        #選cover下面的網址
# print(test[0]['src'].split('i=')[1].split('&')[0]) #src後面分離出來。用split(i=)選第一個
# print(test[0]['src'].split('i=')[1]) #src後面分離出來。用split(i=)選第一個
# print(test[0]['src'])               #拿src後面的文字。用split(i=)選第一個
# print(test[0])               #src後面分離出來。用split(i=)選第一個
# print(test)               #src後面分離出來。用split(i=)選第一個


# 	pics = open(fname, 'wb')    #將取得的圖檔名稱寫入資料夾
# 	shutil.copyfileobj(res2, pics)
# 	pics.close()
# print(test = soup.select('.cover'))
# print(test[0]['src'])
# print('\n')
# print(test[0]['src'].split('/'))
# print('\n')
# print(test[0]['src'].split('/')[-1])
# print('\n')
# print(test[0]['src'].split('/')[-1].split('&'))
# print('\n')
# print(test[0]['src'].split('/')[-1].split('&')[0])

