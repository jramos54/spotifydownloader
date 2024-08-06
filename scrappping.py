import requests, time
import psutil

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# importar webdriver manager
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def close_webdriver_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'chromedriver':
            print(f"Killing chromedriver process with PID {proc.info['pid']}")
            for child in proc.children(recursive=True):
                print(f"Killing child process {child.info['name']} with PID {child.info['pid']}")
                child.kill()
            proc.kill()

def get_links(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-urlfetcher-cert-requests")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Instalar o cargar el controlador Chrome WebDriver
    driver_manager = ChromeDriverManager()
    driver = webdriver.Chrome(service=Service(executable_path=driver_manager.install()), options=chrome_options)

    try:
        print(link)
        driver.get(link)
        time.sleep(10)
        path='//*[@id="main"]/div/div[2]/div[3]/div[1]'
        # path='//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div[4]/div[1]'
        body=driver.find_element(By.XPATH,path)
        
        html = body.get_attribute('outerHTML')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')

        urls=soup.find_all('a', {'draggable': 'false'})
        print(f"\n urls extraidos \n {len(urls)}\n")
        driver.quit()
        return urls
    except Exception as e :
        print("error al hacer scrapping")
        print(f"\n{e}\n")
        driver.quit()
        return []
    finally:
        if driver:
            try:
                driver.quit()
                print("WebDriver closed successfully.")
            except Exception as e:
                print(f"Error while quitting driver: {e}", exc_info=True)
        close_webdriver_processes()

if __name__=="__main__":
    link="https://open.spotify.com/album/5tftehUS6uzufwwQ5QBwQC?si=e059OKhXQCW6jAIBDfEkpA"
    urls=get_links(link)
    print(len(urls))
    for url in urls:
        print(type(url))