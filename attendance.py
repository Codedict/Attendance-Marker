from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
while True:
  username =""  #enter username here#
  password ="" #enter password here#
  browser = webdriver.Chrome(ChromeDriverManager().install())
  browser.get('https://saintgitsengineering.linways.com/student/student.php?menu=online_meet&action=list')

  username_sniv = browser.find_element_by_name('studentAccount')
  username_sniv.send_keys(username)

  password_sniv =browser.find_element_by_name('studentPassword')
  password_sniv.send_keys(password)

  login_sniv = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/div/button')
  login_sniv.click()
  time.sleep(10)
  class_link = browser.find_element_by_xpath('//*[@id="liveNow"]/table/tbody/tr/td[5]/button')
  class_link.click()
  time.sleep(10)
  browser.close()
  time.sleep(20)