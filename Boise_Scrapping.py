from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
# from selenium.webdriver.common.keys import Keys3
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
# options.add_argument("window-size=1920x1080")

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
 
website = 'https://permits.cityofboise.org/CitizenAccess/Cap/CapHome.aspx?module=Building&TabName=Building'
# path = 'C:\Users\andre\anaconda3\envs\Python_selenium'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()


'THIS IS TO SET ALL THE DROPDOWNS'

# RECORD TYPE DROPDOWN
Record_Type = "502-New or Added Commercial"
dropdown_RecordType = Select(driver.find_element_by_id('ctl00_PlaceHolderMain_generalSearchForm_ddlGSPermitType'))
dropdown_RecordType.select_by_visible_text(Record_Type)
time.sleep(1.5)


# RECORD START DATE
dropdown_StartDate= driver.find_element_by_name('ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate')
driver.execute_script("arguments[0].value = '05/01/2023'", dropdown_StartDate)
time.sleep(1.5)

# RECORD END DATE
# NEED TO ADD TODAY TO VALUE
dropdown_EndDate= driver.find_element_by_name('ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate')
driver.execute_script("arguments[0].value = '11/22/2023'", dropdown_EndDate)
time.sleep(1.5)

#THIS IS TO CLICK ON THE SEARCH BUTTON AT THE ENG
search_button = driver.find_element_by_id("ctl00_PlaceHolderMain_btnNewSearch")
search_button.click()
time.sleep(1.5)

"Pagination"

pagination = driver.find_element_by_xpath('//table[contains(@class, "aca_pagination")]')
pages = len(pagination.find_elements_by_class_name("aca_pagination_td"))
last_page= pages -2





current_page=1 

date = []
record_number = []
status = []
description = []
project_name = []
address = []


while current_page <= last_page:
    time.sleep(3)

    'this is to scrape the data from the table'
    #THIS IS TO SCRAPE DATA FROM FIRST TABLE SEARCH
    table=driver.find_elements_by_class_name("ACA_AlignLeftOrRightTop")
    
    
    indexes = {
        "date": 1,
        "record_number": 2,
        "status": 3,
        "description":  4,
        "project_name":  5,
        "address":  6
        }
    
    
    for index, value in enumerate(table):
        cellposition = index%9
        celltext = value.text
        if cellposition == indexes["date"]:
            date.append(celltext)
        if cellposition == indexes["record_number"]:
            record_number.append(celltext)
        if cellposition == indexes["status"]:
            formattedStatus = "NO STATUS" 
            if celltext != "":
                formattedStatus=celltext
            status.append(formattedStatus)
        if cellposition == indexes["description"]:
            description.append(celltext)
        if cellposition == indexes["project_name"]:
            project_name.append(celltext)
        if cellposition == indexes["address"]:
            address.append(celltext)
            
    # for index in range(len(date)):
    #     print(date[index])
    #     print(record_number[index])
    #     print(status[index])
    #     print(description[index])
    #     print(project_name[index])
    #     print(address[index])
    #     print("")
        
    current_page= current_page +1
    
    try:
        next_page = driver.find_elements_by_xpath('//a[contains(@class, "aca_simple_text font11px")]')
        next_page_last = next_page[-1] if next_page else None
        next_page_last.click()
    except:
        pass
    
df=pd.DataFrame({'date':date,'record_number':record_number,'status':status,'description':description,'project_name':project_name,'address':address})  
df.to_csv('Boise_list.csv')
print(df)

    

# driver.quit()