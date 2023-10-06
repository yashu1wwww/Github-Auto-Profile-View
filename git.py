from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier
import requests

def func(barrier):
    options = webdriver.ChromeOptions()
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

number_of_threads = 10 #how much views you want change to your needed number
barrier = Barrier(number_of_threads)
threads = []
for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
