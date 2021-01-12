from selenium import webdriver
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.instagram.com')

wait = WebDriverWait(driver, 10)

# login_elem = browser.find_element_by_xpath(
#    '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')

second_page_flag = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "KPnG0")))  # util login page appear


user = driver.find_element_by_name("username")

passw = driver.find_element_by_name('password')

ActionChains(driver)\
    .move_to_element(user).click()\
    .send_keys('ingresarUsuario')\
    .move_to_element(passw).click()\
    .send_keys('ingresarContrasena')\
    .perform()

login_button_ = driver.find_element_by_class_name(
    "L3NKy")

login_button_.click()

time.sleep(10)
driver.get("https://www.instagram.com/p/B166OkVBPJR/")


time.sleep(3)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed():
        load_more_comment.click()
        time.sleep(7.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1


except Exception as e:
    print(e)
    pass

try:
    test = driver.find_elements_by_class_name('EizgU')
    for box in test:

        while box.text != "Hide replies":
            time.sleep(3.5)
            box.click()

except Exception as e:
    print(e)
    pass

import pandas as pd

df = pd.DataFrame(columns = ['Post','Caption','Date','likesComment','IdFatherComment','IdChildComment','Username'])

user_names = []
user_comments = []

box = driver.find_elements_by_class_name('Mr508')
posicion = 0
for b in box:
    comment = b.find_elements_by_class_name('gElp9 ')

    elemen_number = 0
    pather_id = 0
    idFath = ''
    for c in comment:
        container = c.find_element_by_class_name('C4VMK')
        ide = container.id
        name = container.find_element_by_class_name('_6lAjh').text
        r = container.find_elements_by_tag_name('span')[-1]
        content = container.find_elements_by_tag_name('span')[-1].text
        content = content.replace('\n', ' ').strip().rstrip()
        date = container.find_elements_by_tag_name('time')[0].get_attribute('title')
        likesLits = container.find_elements_by_class_name('FH9sR')
        likes = ''
        if(len(likesLits) == 3):
            likes = likesLits[1].text
        else:
            likes = '0 likes'
        user_names.append(name)
        user_comments.append(content)

        if(elemen_number == 0):
            idFath = ide
            df.loc[posicion] = ['https://www.instagram.com/p/B166OkVBPJR/', content, date, likes, idFath, '', name]
        else:
            df.loc[posicion] = ['https://www.instagram.com/p/B166OkVBPJR/',content,date,likes,idFath,ide,name]
        posicion +=1
        elemen_number += 1
    time.sleep(1)


print(df)
writes = pd.ExcelWriter('test.xlsx')
df.to_excel(writes,'df')
df.to_csv('instagram.csv')
writes.save()



#
#
# comment = driver.find_elements_by_class_name('gElp9 ')
# posicion = 0
# for c in comment:
#     container = c.find_element_by_class_name('C4VMK')
#     name = container.find_element_by_class_name('_6lAjh').text
#     r = container.find_elements_by_tag_name('span')[-1]
#     content = container.find_elements_by_tag_name('span')[-1].text
#     content = content.replace('\n', ' ').strip().rstrip()
#     date = container.find_elements_by_tag_name('time')[0].get_attribute('title')
#     likesLits = container.find_elements_by_class_name('FH9sR')
#     likes = ''
#     if(len(likesLits) == 3):
#         likes = likesLits[1].text
#     else:
#         likes = '0 likes'
#     user_names.append(name)
#     user_comments.append(content)
#     df.loc[posicion] = [name,content,date,likes,name,name,name]
#     posicion +=1
#
# print(df)
# writes = pd.ExcelWriter('test.xlsx')
# df.to_excel(writes,'df')
# writes.save()


# user_names.pop(0)
# user_comments.pop(0)
# import excel_exporter
# excel_exporter.export(user_names, user_comments)
# 
driver.close()








# driver = webdriver.Chrome()
# driver.get("https://www.instagram.com/p/CBHH2KjI6BW/")
# time.sleep(3)
#
# #if user not logined
# try:
#     close_button = driver.find_element_by_class_name('xqRnw')
#     close_button.click()
# except:
#     pass
#
#
# try:
#     load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
#     print("Found {}".format(str(load_more_comment)))
#     i = 0
#     while load_more_comment.is_displayed() and i < int(sys.argv[2]):
#         load_more_comment.click()
#         time.sleep(1.5)
#         load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
#         print("Found {}".format(str(load_more_comment)))
#         i += 1
# except Exception as e:
#     print(e)
#     pass
#
# user_names = []
# user_comments = []
# comment = driver.find_elements_by_class_name('gElp9 ')
# for c in comment:
#     container = c.find_element_by_class_name('C4VMK')
#     name = container.find_element_by_class_name('_6lAjh').text
#     content = container.find_element_by_tag_name('span').text
#     content = content.replace('\n', ' ').strip().rstrip()
#     user_names.append(name)
#     user_comments.append(content)
#
# user_names.pop(0)
# user_comments.pop(0)
# import excel_exporter
# excel_exporter.export(user_names, user_comments)
#
# driver.close()