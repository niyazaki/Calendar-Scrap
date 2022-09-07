from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

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
tdXpathFirst = '//*[@id="GInterface.Instances[1].Instances[3]_Calendrier"]/table[1]/tbody/tr/td[1]'
tdXpathLast = '//*[@id="GInterface.Instances[1].Instances[3]_Calendrier"]/table[1]/tbody/tr/td[52]'

weeks = {}
for i in range(1, 53):
    driver.find_element(By.XPATH, f"{trXpath}/td[{i}]").click()
    week = driver.find_element(
        By.XPATH, '//*[@id="GInterface.Instances[1].Instances[7]_Grille_Elements"]')
    time.sleep(0.01)
    weeks[i] = week.get_attribute("innerHTML")

with open("weeks.txt", "w", encoding="UTF-8", newline="\n") as file:
    file.write(str(weeks))


#iframe = driver.switch_to.frame("GInterface.Instances")

driver.quit
