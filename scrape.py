from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
hackathons = []
driver = None

def scrape_data():
    global hackathons, driver

    # Update this path with the correct path of your system
    # chrome_path = "/usr/bin/google-chrome" - # Linux and MacOS
    chrome_path="/path/to/google-chrome"
    # install chromedriver version compatible with yoyr google-chrome version

    # Update this path with the correct path of your system
    
    #chromedriver_path = "/usr/local/bin/chromedriver" - # Linux and MacOS
    chromedriver_path = "/path/to/chromedriver"

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        
        driver = webdriver.Chrome(options=options)
        
        driver.get("https://mlh.io/seasons/2024/events")
        links = driver.find_elements(By.CLASS_NAME, "event-link") # Fetching links of hackathon websites
        images = driver.find_elements(By.CSS_SELECTOR, ".image-wrap img") # Fetching images of hackathons
        names = driver.find_elements(By.CLASS_NAME, "event-name") # Fetching names of hackathons
        dates = driver.find_elements(By.CLASS_NAME, "event-date") # Fetching dates
        locs = driver.find_elements(By.CLASS_NAME, "event-location") # Fetching location
        modes = driver.find_elements(By.CLASS_NAME,"event-hybrid-notes") # Fetching modes
        hackathons = []
        for i in range(len(links)):
            hackathon = {
                "name": names[i].text,
                "link": links[i].get_attribute("href"),
                "image": images[i].get_attribute("src"),
                "date": dates[i].text,
                "location": locs[i].text,
                "mode":modes[i].text
            }
            hackathons.append(hackathon)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            if driver:
                with open("hackathons.json","w") as f:
                    json.dump(hackathons,f,indent=4); 
                driver.quit()
                print("Webdriver quit successfully")
                exit()
        except Exception as e:
            print(f"Error in final block: {e}")

while True:
    scrape_data()
    time.sleep(86400)
