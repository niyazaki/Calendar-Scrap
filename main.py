from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import html5lib

import re


class Course:
    def __init__(self, *args, **kwargs):
        self.courseCode = kwargs.get("courseCode", None)
        self.courseName = kwargs.get("courseName", None)
        self.date = kwargs.get("date", None)
        self.weekNumber = kwargs.get("weekNumber", None)
        self.dayNumber = kwargs.get("dayNumber", None)
        self.start_hour = kwargs.get("start_hour", None)
        self.end_hour = kwargs.get("end_hour", None)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hplanning2022.umons.ac.be/invite")
driver.implicitly_wait(5)

# Formations
driver.find_element(
    By.XPATH, '//*[@id="GInterface.Instances[0].Instances[1]_Combo0"]').click()
# Saisie du nom
driver.find_element(
    By.XPATH, '//*[@id="GInterface.Instances[1].Instances[1].bouton"]/div/div').click()
# Selection du cursus
driver.find_element(
    By.XPATH, '//*[@id="GInterface.Instances[1].Instances[1]_21"]').click()


trXpath = '//*[@id="GInterface.Instances[1].Instances[3]_Calendrier"]/table[1]/tbody/tr'
# tdXpathFirst = '//*[@id="GInterface.Instances[1].Instances[3]_j_1"]'
# tdXpathLast = '//*[@id="GInterface.Instances[1].Instances[3]_j_52"]'
# tdXpathFirst = '//*[@id="GInterface.Instances[1].Instances[3]_Calendrier"]/table[1]/tbody/tr/td[1]'
# tdXpathLast = '//*[@id="GInterface.Instances[1].Instances[3]_Calendrier"]/table[1]/tbody/tr/td[52]'

weeks = {}
weeksHtml = ""
for i in range(1, 53):
    # Week number
    driver.find_element(
        By.XPATH, f'//*[@id="GInterface.Instances[1].Instances[3]_j_{i}"]').click()
    # Content of schedule
    week = driver.find_element(
        By.XPATH, '//*[@id="GInterface.Instances[1].Instances[7]_Grille_Elements"]').get_attribute("innerHTML")
    soup = BeautifulSoup(week, 'html5lib')
    weeksHtml += week
    # print(soup.prettify())
    # courses = soup.find_all('<div class="cours-simple"')
    # print(courses)
    if i != 1:
        #print(i-1, soup.prettify)
        weeks[i-1] = soup
    # print(week.get_attribute("innerHTML"))
    # time.sleep(5)


with open("weeks.txt", "w", encoding="UTF-8", newline="\n") as file:
    file.write(str(weeks))

soup2 = BeautifulSoup(weeksHtml, "html5lib")

with open("weekshtml.html", "w", encoding="UTF-8", newline="\n") as file2:
    file2.write(soup2.prettify())
    print("Yes let's go")

#iframe = driver.switch_to.frame("GInterface.Instances")

driver.quit()
