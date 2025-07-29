from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Configuração do webdriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

#acessa a pagina de cadastro usando o caminho absoluto com o protocolo file://
#certifique-se de que o caminho está apontando para um arquivo HTML especifico

driver.get("file:///C:/Users/ruan_m_vieira/Downloads/Teste_de_sistemas/index.html")

#preenche o campo nome
nome_input = driver.find_element(By.ID, "name")
nome_input.send_keys("Ruan Vieira")

#Preenche o campo CPF
cpf_input = driver.find_element(By.ID, "cpf")
cpf_input.send_keys("12345678901")

#preenche campo endereço
endereco_input = driver.find_element(By.ID, "address")
endereco_input.send_keys("Rua das flores, 123")

#preenche o campo telefone
telefone_input = driver.find_element(By.ID, "phone")
telefone_input.send_keys("11987654321")

#clica no botão de cadastrar
#submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#submit_button.click()

#aguarda alguns segundos para visualizar o resultado (em uma aplicação real você verificaria a resposta)
time.sleep(10)

#fecha o navegador
driver.quit()