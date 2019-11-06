import time
from selenium import webdriver
 
#ChromeDriverのパスを引数に指定しChromeを起動
driver = webdriver.Chrome(
    r"C:\Users\kazuk\OneDrive\デスクトップ\chromedriver_win32\chromedriver.exe")
#Googleページに移行
while True:
    driver.get("https://atcoder.jp/contests/agc040/standings")
    #検索テキストボックスの要素を取得
    #「Test」とテキストボックスに入力されていることを確認
    time.sleep(60)
    #ページを更新(ブラウザのリフレッシュ)
    driver.refresh()
