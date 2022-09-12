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

with open("weekshtml.html", "r") as f:
    soup = BeautifulSoup(f, "html5lib")

courses = soup.find_all("div", {"class", "cours-simple"})

for cours in courses:
    hour = cours.get("title")
    hour_start, hour_end, duration = re.findall("[0-9]{2}h[0-9]{2}", hour)
    print(hour_start, hour_end, duration)
