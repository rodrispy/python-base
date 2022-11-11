from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

navegador.get("https://www.hashtagtreinamentos.com/")