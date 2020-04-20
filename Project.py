import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from pynput.keyboard import Key, Controller
keyboard = Controller()


#User_Input_Parameters
from_date = 13
from_month = 4
from_year = 2020

to_date = 19
to_month = 4
to_year = 2020

file_general_type = "標題類別"
file_specific_type = "關連交易"


#Basic setup
options = webdriver.ChromeOptions()
preferences = {"download.default_directory":"C:\使用者\\tom\Desktop\Yr4 Sem2\ECON 3086 - Python\For project"}
options.add_experimental_option("prefs",preferences)
driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=zh")
driver.maximize_window()


#Open the general types of files_table
open_file_type_table = driver.find_element_by_id('tier1-select').click()
time.sleep(0.5)

# Determine the general type for "標題類別"
if file_general_type == "標題類別":
    if file_specific_type == "關連交易":
        file_general = driver.find_element_by_link_text("標題類別").click()
        time.sleep(0.5)
        file_specific_1 = driver.find_element_by_link_text("所有").click()
        time.sleep(0.5)
        file_specific_2 = driver.find_element_by_link_text("通函").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(u"(//a[contains(text(),'關連交易')])[6]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(u"(//a[contains(text(),'所有')])[18]").click()
        time.sleep(0.5)

# Determine the general type for "文件類別"
elif file_general_type == "文件類別":
    file_general = driver.find_element_by_link_text("文件類別").click()
    time.sleep(0.5)
    file_specific_1 = driver.find_element_by_link_text("所有").click()



##Step 1: setting up the range of time - from
#Select the from_table
open_from_table = driver.find_element_by_id('searchDate-From').click()

#Select the from_date
dum_from_date = '//b[@class="day"]/ul[1]/li[{}]'.format(from_date)
select_from_date = driver.find_element_by_xpath(dum_from_date).click()
time.sleep(0.5)

#Select the from_month
dum_from_month = '//b[@class="month"]/ul[1]/li[{}]'.format(from_month)
select_from_month = driver.find_element_by_xpath(dum_from_month).click()
time.sleep(0.5)

#Select the from_year
dum_from_year = '//b[@class="year"]/ul[1]/li[{}]'.format(2021 - from_year)
select_from_year = driver.find_element_by_xpath(dum_from_year).click()
time.sleep(0.5)


#Save the from_selection
close_from_table = driver.find_element_by_id('searchTitle').click()
time.sleep(0.5)

##Step 2: setting up the range of time - To
#Select the To_table
open_to_table = driver.find_element_by_id('searchDate-To').click()
time.sleep(0.5)

#Select the to_date
dum_to_date = '//b[@class="day"]/ul[1]/li[{}]'.format(to_date)
select_to_date = driver.find_element_by_xpath(dum_to_date).click()
time.sleep(0.5)

#Select the to_month
dum_to_month = '//b[@class="month"]/ul[1]/li[{}]'.format(to_month)
select_to_month = driver.find_element_by_xpath(dum_to_month).click()
time.sleep(0.5)

#Select the to_year
dum_to_year = '//b[@class="year"]/ul[1]/li[{}]'.format(2021 - to_year)
select_to_year = driver.find_element_by_xpath(dum_to_year).click()
time.sleep(0.5)

#Save the from_selection
close_to_table = driver.find_element_by_id('searchTitle').click()
time.sleep(0.5)

#Actually works - search
search_click = driver.find_element_by_link_text("搜尋").click()

#Getting_ALL_documents_title
Doc_title = driver.find_elements_by_xpath('//div[@class="table-scroller"]/table/tbody/tr/td[4]/div[2]/a')

for i in Doc_title:
    #Right_click the doc_title
    ActionChains(driver).context_click(i).perform()
    time.sleep(1.5)

    #Press and release ("K") to save as the file
    keyboard.press('k')
    time.sleep(1.5)

    # Press "enter" to actually to save
    keyboard.press(Key.enter)
    time.sleep(1.5)

#Try to get every element shown on the table
date_1 = driver.find_elements_by_xpath('//div[@class="table-scroller"]/table/tbody/tr/td[1]')
stock_code_2 = driver.find_elements_by_xpath('//div[@class="table-scroller"]/table/tbody/tr/td[2]')
stock_name_3 = driver.find_elements_by_xpath('//div[@class="table-scroller"]/table/tbody/tr/td[3]')
doc_name_4 = driver.find_elements_by_xpath('//div[@class="table-scroller"]/table/tbody/tr/td[4]')

#Try to print the summary of the table I clicked
for a,b,c,d in zip(date_1,stock_code_2,stock_name_3,doc_name_4):
    try:
        raw = "{} - {} - {} - {}".format(a.text,b.text,c.text,d.text)
        print(raw)

    except AttributeError:
        pass




import quandl
quandl.ApiConfig.api_key = 'y4h68UcnaJDbwnmMXzQs'
df = quandl.get('CHRIS/MGEX_IH1', start_date='2019-04-01', end_date='2020-04-02')

df.plot()
df.head(10)
df.describe()

