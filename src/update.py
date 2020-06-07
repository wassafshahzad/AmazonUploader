import os

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import sys


spreadsheet_filename = 'KDP Spreadsheet.xlsx'
user_name, passwd, spreadsheet_filename,browser = sys.argv[1:]

'''if not os.path.exists(login_file_name):
    print(f"{login_file_name} File Don't Exist. file format\nusername\npassword")
    input("Press enter to exit")
    exit()'''



"""if not os.path.exists(spreadsheet_filename):
    print(f"{spreadsheet_filename} File Don't Exist. file format\nusername\npassword")
    input("Press enter to exit")
    exit()
"""

"""with open(login_file_name, 'r') as stream:
    user_name, passwd = stream.readlines()[:2]
"""

"""
df = pd.read_excel(spreadsheet_filename)
L = df.values.tolist()
"""

# %%

def sign_in():
    driver.get('https://kdp.amazon.com/en_US')
    time.sleep(3)
    Sing_in = driver.find_element_by_xpath('//*[@id="signinButton-announce"]')
    Sing_in.click()
    time.sleep(3)
    Email = driver.find_element_by_xpath('//*[@id="ap_email"]')
    Email.send_keys(user_name)
    Password = driver.find_element_by_xpath('//*[@id="ap_password"]')
    Password.send_keys(passwd)
    #Login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    #input("Enter Captcha And press Enter: ")
    #Login.click()
    #time.sleep(3)


def select_category(category1):
    nodes = category1.split(' > ')
    categories = nodes[:-1]
    category = nodes[-1]
    for i in categories:
        driver.find_element_by_xpath(f'//a[@class="a-link-normal"][contains(text(),"{i}")]').click()
        time.sleep(2)
    el = driver.find_element_by_xpath(f'//span[@class="a-label a-checkbox-label"][contains(text(),"{category}")]/../input')
    driver.execute_script('arguments[0].click();', el)
    time.sleep(2)


def publish(i):
    driver.get('https://kdp.amazon.com/en_US/bookshelf?language=en_US')
    Paper_back = driver.find_element_by_xpath('//*[@id="create-paperback-button"]/span/input')
    Paper_back.click()
    time.sleep(3)
    Book_title = driver.find_element_by_xpath('//*[@id="data-print-book-title"]')
    Book_title.send_keys(i[0])
    Sub_title = driver.find_element_by_xpath('//*[@id="data-print-book-subtitle"]')
    Sub_title.send_keys(i[4])
    First_name = driver.find_element_by_xpath('//*[@id="data-print-book-primary-author-first-name"]')
    First_name.send_keys(i[1])
    Last_name = driver.find_element_by_xpath('//*[@id="data-print-book-primary-author-last-name"]')
    Last_name.send_keys(i[2])
    Discription = driver.find_element_by_xpath('//*[@id="data-print-book-description"]')
    Discription.send_keys(i[3])
    Radio_btn = driver.find_element_by_xpath('//*[@id="non-public-domain"]')
    Radio_btn.click()
    Keyword1 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-0"]')
    Keyword1.send_keys(i[5])
    Keyword2 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-1"]')
    Keyword2.send_keys(i[6])
    Keyword3 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-2"]')
    Keyword3.send_keys(i[7])
    Keyword4 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-3"]')
    Keyword4.send_keys(i[8])
    Keyword5 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-4"]')
    Keyword5.send_keys(i[9])
    Keyword6 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-5"]')
    Keyword6.send_keys(i[10])
    Keyword7 = driver.find_element_by_xpath('//*[@id="data-print-book-keywords-6"]')
    Keyword7.send_keys(i[11])
    Categories = driver.find_element_by_xpath('//*[@id="data-print-book-categories-button-proto-announce"]')
    Categories.click()
    try:
        driver.find_element_by_xpath('//*[@id="category-chooser-remove-2"]').click()
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="category-chooser-remove-1"]').click()
    except:
        pass
    
    time.sleep(2)
    category1 = i[15]

    select_category(category1)

    # driver.execute_script("arguments[0].click();", driver.find_element_by_css_selector(f'input[nodeid="{category1}"]'))
    # time.sleep(5)
    category2 = i[16]

    select_category(category2)
    # driver.execute_script("arguments[0].click();", driver.find_element_by_css_selector(f'input[nodeid="{category2}"]'))
    # time.sleep(3)
    Save = driver.find_element_by_xpath('//*[@id="category-chooser-ok-button"]/span/input')
    Save.click()
    time.sleep(3)
    Adult = driver.find_element_by_xpath('//*[@id="data-print-book-is-adult-content"]/div/div/div[1]/div/label/input')
    Adult.click()
    Save_And_Conti = driver.find_element_by_xpath('//*[@id="save-and-continue-announce"]')
    Save_And_Conti.click()
    time.sleep(3)
    Assign = driver.find_element_by_xpath('//*[@id="free-print-isbn-btn-announce"]')
    Assign.click()
    time.sleep(3)
    ISBN = driver.find_element_by_xpath('//*[@id="print-isbn-confirm-button-announce"]')
    ISBN.click()
    time.sleep(3)
    Interior_p_t = i[17].lower()
    if Interior_p_t == 'a':
        B_W_with_cream = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]').click()
    if Interior_p_t == 'b':
        B_W_with_White_paper = driver.find_element_by_xpath('//*[@id="a-autoid-1-announce"]').click()
    if Interior_p_t == 'c':
        B_W_with_color = driver.find_element_by_xpath('//*[@id="a-autoid-2-announce"]').click()
    # PAPER TRIM SIZE SECTION
    width = i[18]
    height = i[21]
    trim = driver.find_element_by_xpath('//*[@id="trim-size-btn-announce"]').click()
    time.sleep(3)
    trim_width = driver.find_element_by_xpath('//*[@id="inputWidth"]').clear()
    driver.find_element_by_xpath('//*[@id="inputWidth"]').send_keys(str(width))
    trim_height = driver.find_element_by_xpath('//*[@id="inputHeight"]').clear()
    driver.find_element_by_xpath('//*[@id="inputHeight"]').send_keys(str(height))
    select = driver.find_element_by_xpath('//*[@id="a-autoid-10"]/span/input').click()
    # CHOSE BLEED SECTION OPTION A OR B
    Bleed = i[19]
    if Bleed == 'a':
        driver.find_element_by_xpath('//*[@id="a-autoid-3-announce"]').click()
    if Bleed == 'b':
        driver.find_element_by_xpath('//*[@id="a-autoid-4-announce"]').click()
    # PAPER BACK COVER FINISH CODE CHOSE A OR B
    Paper_back_cover_finish = i[20]
    if Paper_back_cover_finish == 'a':
        driver.find_element_by_xpath('//*[@id="a-autoid-5-announce"]').click()
    if Paper_back_cover_finish == 'b':
        driver.find_element_by_xpath('//*[@id="a-autoid-6-announce"]').click()

    Menuscript = driver.find_element_by_xpath('//*[@id="data-print-book-publisher-interior-file-upload-AjaxInput"]')
    Menuscript.send_keys(i[12])
    time.sleep(30)
    Chose = driver.find_element_by_xpath('//*[@id="data-print-book-publisher-cover-choice-accordion"]/div[2]/div/div[1]/a/i')
    Chose.click()
    Cover = driver.find_element_by_xpath('//*[@id="data-print-book-publisher-cover-file-upload-AjaxInput"]')
    Cover.send_keys(i[13])
    time.sleep(300)
    Launch = driver.find_element_by_xpath('//*[@id="print-preview-noconfirm-announce"]')
    time.sleep(2)
    Launch.click()
    WebDriverWait(driver, 320).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="printpreview_approve_button_enabled"]/span/a')))
    Approve = driver.find_element_by_xpath('//*[@id="printpreview_approve_button_enabled"]/span/a')
    Approve.click()
    time.sleep(5)
    Save_Continue = driver.find_element_by_xpath('//*[@id="save-and-continue-announce"]')
    Save_Continue.click()
    WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="data-pricing-print-us-price-input"]/input')))
    Price = driver.find_element_by_xpath('//*[@id="data-pricing-print-us-price-input"]/input')
    Price.send_keys(str(i[14]))
    Checkbox = driver.find_element_by_xpath('//*[@id="data-pricing-print"]/div/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div/label/i')
    Checkbox.click()
    time.sleep(5)
    #Publish = driver.find_element_by_id('save-and-publish-announce')
    #Publish.click()
    print('Done')
    time.sleep(40)

#%%
# 
if(browser == "firefox"):
    driver = webdriver.Firefox(executable_path = "geckodriver")
else:
    driver = webdriver.Chrome()

sign_in()

print(user_name)
for i in L:
    pass
    publish(i)

