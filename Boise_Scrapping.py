from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
 
website = 'https://permits.cityofboise.org/CitizenAccess/Cap/CapHome.aspx?module=Building&TabName=Building'
# path = 'C:\Users\andre\anaconda3\envs\Python_selenium'
driver = webdriver.Chrome()
driver.get(website)



'THIS IS TO SET ALL THE DROPDOWNS'

# RECORD TYPE DROPDOWN
Record_Type = "502-New or Added Commercial"
dropdown_RecordType = Select(driver.find_element_by_id('ctl00_PlaceHolderMain_generalSearchForm_ddlGSPermitType'))
dropdown_RecordType.select_by_visible_text(Record_Type)
time.sleep(1.5)


# RECORD START DATE
dropdown_StartDate= driver.find_element_by_name('ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate')
driver.execute_script("arguments[0].value = '10/01/2023'", dropdown_StartDate)
time.sleep(1.5)

# RECORD END DATE
# NEED TO ADD TODAY TO VALUE
dropdown_EndDate= driver.find_element_by_name('ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate')
driver.execute_script("arguments[0].value = '10/29/2023'", dropdown_StartDate)
time.sleep(1.5)

#THIS IS TO CLICK ON THE SEARCH BUTTON AT THE ENG
search_button = driver.find_element_by_id("ctl00_PlaceHolderMain_btnNewSearch")
search_button.click()
time.sleep(1.5)


'this is to scrape the data from the table'
#THIS IS TO SCRAPE DATA FROM FIRST TABLE SEARCH
table=driver.find_elements_by_class_name("ACA_AlignLeftOrRightTop")

for TableVal in table:
    print(TableVal.text)
    
date = []
RecordNum = []
Status = []
Description = []
ProjectName = []
Address = []

    
    
# table = get_elements_by_tag("tbody")
# headers = table.get_elements_by_tag("th")

# date = []
# record_number = []
# status = []
# description = []
# project_name = []
# address = []

# for match in matches_odd:
#     print(match.text)

# for match in matches_even:
#     print(match.text)
    

    

# driver.quit()