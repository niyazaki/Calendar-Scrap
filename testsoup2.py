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
import unicodedata

import re
from course import Course
import os

validatedCodes = {"V-LANG-550", "W-DDIV-058", "P-SMSL-091", "P-SEDO-247",
                  "P-SEDO-248", "P-SEDO-253", "P-SEDO-254", "P-SEDO-255",
                  "V-LANG-559", "P-SMSL-213", "P-SEPT-160", "P-SEPT-215",
                  "P-SPCE-099", "P-SPCE-100"}
coursesDic = {}

weekshtml = os.scandir(path="./weeks")
listFile = []
for elem in weekshtml:
    listFile.append(elem.name)

listFile.sort(key=lambda f: int(re.sub('\D', '', f)))
for iteration, fileName in enumerate(listFile):
    with open(f"./weeks/{fileName}", "r") as f:
        soup = BeautifulSoup(f, "html5lib")

    courses = soup.find_all("div", {"class", "EmploiDuTemps_Element"})

    # print("Semaine : ", iteration + 1, courses)
    listOfCourses = []
    hasMemo = False
    for iter, cours in enumerate(courses):
        # print(cours)
        courseTitle = cours.find(
            "label", {"class", "AvecMain SouligneSurvol"}).text.strip("\n -_")

        try:
            courseCode = re.match(
                "[a-zA-Z]-[a-zA-Z]+-[0-9]+", courseTitle).group()
            courseName = courseTitle.replace(courseCode, "").strip("\n -_")
        except:
            courseCode = ""
            courseName = courseTitle

        # Remove all elem in list that has no letter in it
        # finalCourseList = [
            # elem for elem in finalCourseList if elem.lower().islower()]

        if courseCode not in validatedCodes:
            left = re.search(
                "left: [-0-9]+px", cours.get("style")).group().split(" ")[1][:-2]
            width = re.search(
                "width: [-0-9]+px", cours.get("style")).group().split(" ")[1][:-2]
            courseInfos = cours.find("div", {"class", "cours-simple"})
            hours = courseInfos.get("title")
            hourStart, hourEnd, duration = re.findall(
                "[0-9]{2}h[0-9]{2}", hours)
            try:
                location2 = courseInfos.find(
                    "div", {"class", "InlineBlock AlignementHaut NoWrap"}).text.strip("\n ").replace(".", " ")
            except:
                location2 = ""

            cou = Course(left=left, width=width, weekNumber=iteration+1)
            print("\n", "Location : ", repr(location2), "\nWeekNumber : ",
                  cou.weekNumber, "Day : ", cou.day, "Course Name : ", courseName, "Course Code : ", courseCode)
            # time.sleep(5)

            # Not working anymore
            #print("Cours Txt : ", cours.text)
            # if iteration + 1 == 3 and iter >= 3:
            # time.sleep(10)
            exclusionChars = {"", "Cours", "Cours/Exercic", "Cours/Exercice", "Cours/Exercices",
                              hourStart, hourEnd, duration, courseName, courseCode, f"{courseCode} - {courseName}"}
            # location = unicodedata.normalize("NFKD", str(list(set([t.strip("\n ")
            #    for t in cours.text.split("\n") if len(t) > 1]) - exclusionChars)[0])).replace(".", " ")
            cou = Course(left=left, width=width, weekNumber=iteration+1,
                         hourStart=hourStart, hourEnd=hourEnd, duration=duration, courseCode=courseCode, courseName=courseName, location=location2+"\n")
            # print("Location : ", cou.location, "WeekNumber : ",
            #      cou.weekNumber, "Day : ", cou.day)
            listOfCourses.append(cou)
            # print(cou)

    coursesDic[f"{iteration+1}"] = listOfCourses
    # print(courses)
    # print(listOfCourses)

with open("output.txt", "w", encoding="UTF-8", newline="\n") as output:
    output.write(str(coursesDic)+"\n\n")
