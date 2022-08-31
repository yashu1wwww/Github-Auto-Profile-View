from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier

#below code was copied from internet source for script run 

def load_proxies(PATH): # for loading the proxies
    return open(PATH).read().split('\n') 

def load_session(url,proxy): # manage each session
    proxy,port = proxy.split(':')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy)
    profile.set_preference("network.proxy.http_port", port)
    profile.set_preference("network.proxy.ssl", proxy)
    profile.set_preference("network.proxy.ssl_port", port)
    profile.update_preferences()
    
#Below Code Is Copied From Stackoverflow
def func(barrier):
    
    driver = webdriver.Chrome()

    driver.get("https://github.com/xtekky")  #change to your github url

    print('wait for others')
    barrier.wait()

    print('click')
    b.click()

number_of_threads = 10 #how much views you want change to your confort

barrier = Barrier(number_of_threads)

threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,)) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()
