from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/ruan_m_vieira/Downloads/Teste_de_sistemas/produtos.html")

nome_input = driver.find_element(By.ID, "id")
nome_input.send_keys("1")

nome_input = driver.find_element(By.ID, "nome")
nome_input.send_keys("Faca de cozinha")

cpf_input = driver.find_element(By.ID, "descricao")
cpf_input.send_keys("Um item util")

endereco_input = driver.find_element(By.ID, "marca")
endereco_input.send_keys("Tramontina")

telefone_input = driver.find_element(By.ID, "quantidade")
telefone_input.send_keys("30")

telefone_input = driver.find_element(By.ID, "preco")
telefone_input.send_keys("2")

#submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#submit_button.click()

time.sleep(10)

driver.quit()