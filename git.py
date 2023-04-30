from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier
import requests

#Below Code Is Copied From Stackoverflow
def func(barrier):
    # Get a new proxy from the proxy pool
    proxy = requests.get('http://proxy_pool_url/get').text.strip()
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server={}'.format(proxy))
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(300,400)
    time.sleep(5)
    size = driver.get_window_size()
    driver.get("https://github.com/google") #change to your github url
    time.sleep(20)
    driver.close()
    print('wait for others')
    barrier.wait()
    print('click')
    b.click()

number_of_threads = 2 #how much views you want change to your needed number
barrier = Barrier(number_of_threads)
threads = []
for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
