# coding: utf-8
# Author：quzard
from Tui import *
from selenium import webdriver
import random
import time
import datetime
import os
import sys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


def main():
    global t
    global t
    global msg
    global error
    global username
    global password
    global name
    global teacher
    try:
        date_time = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        print("时间:", date_time)
        msg += "时间:\t" + str(date_time) + '\n\n'

        driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)

        url = "http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1583641506865#/dailyReport"
        driver.get(url)
        print(name + '\t' + username + '\t' + password + '\t' + "开始体温上报")
        time.sleep(t)

        checkUrl = driver.current_url
        if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
            driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
        time.sleep(t)

        checkUrl = driver.current_url
        if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
            print(name + '\t' + username + '\t' + password + '\t登录失败')
            msg += name + '\t' + username + '\t' + password + '\t登录失败\n\n'
            error = True
            driver.quit()
            return

        print("成功登录")
        driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div[1]').click()
        time.sleep(t)

        if '今日已填报！' in driver.page_source:
            print(name + '\t' + '今日已填报！')
            msg += name + '\t' + '今日已填报！' + '\n\n'
            driver.quit()
            return

        elif '每日健康申报截止时间15:00' in driver.page_source:
            print(name + '\t' + '每日健康申报截止时间15:00')
            msg += name + '\t' + '每日健康申报截止时间15:00' + '\n\n'
            driver.quit()
            return

        print("添加")
        time.sleep(t)
        if "English Name" in  driver.page_source:
            driver.find_element_by_xpath(
                '/html/body/div[11]/div/div[1]/section/div[2]/div/div[3]/div[2]/div[8]/div[1]/div/input').send_keys(
                "36.7")
        else:
            driver.find_element_by_xpath(
                '/html/body/div[11]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys(
                "36.7")
        print("输入体温")
        time.sleep(t)

        div = driver.find_element_by_xpath('//*[@id="save"]')
        # 滑动滚动条到某个指定的元素
        js4 = "arguments[0].scrollIntoView();"
        # 将下拉滑动条滑动到当前div区域
        driver.execute_script(js4, div)
        time.sleep(t)

        driver.find_element_by_xpath('//*[@id="save"]').click()
        print("点击保存")
        time.sleep(t)
        if "确定数据无误并提交数据" in driver.page_source:
            driver.find_element_by_xpath('/html/body/div[61]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
            print(name + '\t体温上报成功')
            msg += name + '\t体温上报成功' + '\n\n'
        else:
           print(name + '\t未主动上报一次来完善疫苗信息')
           msg += name + '\t未主动上报一次来完善疫苗信息' + '\n\n'
        driver.quit()
        return

    except Exception as e:
        msg += name + '\t' + username + '\t' + password + '\t体温上报失败' + '\n\n' + str(e) + '\n\n'
        print(name + '\t' + username + '\t' + password + '\t体温上报失败' + '\n' + str(e))
        error = True
        driver.quit()
        return


if __name__ == '__main__':
    if "ID" in os.environ:
        username = os.environ["ID"]
    else:
        sys.exit()

    if "PASSWORD" in os.environ:
        password = os.environ["PASSWORD"]
    else:
        sys.exit() 

    if "NAME" in os.environ:
        name = os.environ["NAME"]
    else:
        name = "无名氏"

    if "KU" in os.environ:
        kutui_key = os.environ["KU"]
    else:
        kutui_key = ""

    if "SERVERCHAN" in os.environ:
        serverchan_sckey = os.environ["SERVERCHAN"]
    else:
        serverchan_sckey = ""

    time.sleep(random.randint(0, 300))
    
    
    error = False
    t = 30

    msg = '体温上报' + '\n\n'
    main()
    while error:
        error = False
        t += 10
        msg = '体温上报' + '\n\n'
        main()
        if t > 80:
            break

    if error:
        subject = '体温上报\t失败'
        server_post(subject, msg, serverchan_sckey)
        kutui_post(subject, msg, kutui_key)

    else:
        subject = '体温上报\t成功'
        server_post(subject, msg, serverchan_sckey)
        kutui_post(subject, msg, kutui_key)
