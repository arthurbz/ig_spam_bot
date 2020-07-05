from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome()


def login(username, password):
    """Basically login into Instagram"""
    driver.get('https://instagram.com')
    sleep(3)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    print(username + ' logged in')


def spam_post(post_url, times, comment):
    """Dismiss the popups about login and notifications then starts posting"""
    driver.get(post_url)
    sleep(3)
    i = 0
    while times > i:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/ \
        div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/ \
        div/form/textarea').send_keys(comment)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section \
        [3]/div/form/button').click()
        i += 1
        random_num = random.randint(17, 23)  # cooldown
        print('#{} comment: {}'.format(i, comment))
        print('waiting {} sec'.format(random_num))
        sleep(random_num)


def everything(username, password, post_url, comment, times):
    """username, password, post URL, how many times you want to comment"""
    login(username, password)
    spam_post(post_url, times, comment)


print('waiting for logs... :P')
sleep(10)
uname = input('Username: ')
pw = input('Pass: ')
url = input('Post URL: ')
text = input('Comment: ')
everything(uname, pw, url, text, 10000)

