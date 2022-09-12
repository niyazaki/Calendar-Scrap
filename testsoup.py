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
from course import Course

validatedCodes = {"V-LANG-550", "W-DDIV-058", "P-SMSL-091", "P-SEDO-247",
                  "P-SEDO-248", "P-SEDO-253", "P-SEDO-254", "P-SEDO-255",
                  "V-LANG-559", "P-SMSL-213", "P-SEPT-160", "P-SEPT-215",
                  "P-SPCE-099", "P-SPCE-100"}

with open("week2.html", "r") as f:
    soup = BeautifulSoup(f, "html5lib")


# courses = soup.find_all("div", {"class": "EmploiDuTemps_Element"})[0]
courses = soup.find_all("div", {"class", "EmploiDuTemps_Element"})
# courses = soup.find_all("div", {"class", "cours-simple"})

listOfCourses = []
for cours in courses:
    left = re.search(
        "left: [-0-9]+px", cours.get("style")).group().split(" ")[1][:-2]
    width = re.search(
        "width: [-0-9]+px", cours.get("style")).group().split(" ")[1][:-2]
    # print(left, width)
    # print("calcul", int(left)+1, (int(left)+1)//int(width))

    coursInfos = cours.find("div", {"class", "cours-simple"})
    hours = coursInfos.get("title")
    hourStart, hourEnd, duration = re.findall("[0-9]{2}h[0-9]{2}", hours)

    # print(hourStart, hourEnd, duration)
    # print(coursInfos.prettify())

    courseCode, courseName = cours.find(
        "div", {"class", "contenu"}).text.split("\n")
    courseName = courseName.strip(" -")
    # courseCode2 = cours.select("label")
    # print(courseCode)
    # print(courseName)
    if courseCode not in validatedCodes:
        cou = Course(left=left, width=width,
                     hourStart=hourStart, hourEnd=hourEnd, duration=duration, courseCode=courseCode, courseName=courseName)
        listOfCourses.append(cou)

# print(courses)
print(listOfCourses)
