from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/Teste_de_sistemas/login.html")

# aguarda carregar
time.sleep(2)

# Preenche os campos
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso")
else:
    print("Falha no login ou redirecionamento.")
