from selenium import webdriver
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
driver.get('https://www.facebook.com')

wait = WebDriverWait(driver, 10)

# login_elem = browser.find_element_by_xpath(
#    '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_elements_by_class_name("_6ltg")[0]
username.send_keys(sys.argv[1])
password.send_keys(sys.argv[2])
# Step 4) Click Login
submit.click()

time.sleep(5)
driver.get(sys.argv[3])

time.sleep(6)

pub = driver.find_elements_by_class_name('oh7imozk')[0]


likeIcon = pub.find_elements_by_class_name('pcp91wgn')[0]

#time.sleep(5)
driver.execute_script("arguments[0].click();", likeIcon)
time.sleep(2)
# pic = likeIcon.find_elements_by_tag_name('img')[0]
# pic.click()
#likeIcon.click()

#model = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div')
model = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div.q5bimw55.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.eg9m0zos.l9j0dhe7.du4w35lb.ofs802cu.pohlnb88.dkue75c7.mb9wzai9.l56l04vs.r57mb794.kh7kg01d.c3g1iek1.otl40fxz.cxgpxx05.rz4wbd8a.sj5x9vvc.a8nywdso')
#model.send_keys(Keys.END)
#driver.execute_script("arguments[0].send_keys(arguments[1]);", model, Keys.END)
#model.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model)

time.sleep(2)

last_height = driver.execute_script("return arguments[0].scrollHeight", model)


while True:
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model)

    time.sleep(4)

    new_height = driver.execute_script("return arguments[0].scrollHeight", model)
    if new_height == last_height:
        # If heights are the same it will exit the function
        break
    last_height = new_height



botons = model.find_elements_by_css_selector('.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5')

if len(botons) > 0:
    for b in botons:

        if b.text == "Invitar":
            time.sleep(3)
            driver.execute_script("arguments[0].click();", b)


driver.close()