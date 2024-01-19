# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time    

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas   
# abrir o navegador (chrome)

pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(0.5)
pyautogui.press("enter") 
time.sleep(1.0)


#entrar na conta do google  
pyautogui.click(x=629, y=385)

#entrar na aba de link 
time.sleep(0.5) 
pyautogui.click(x=409, y=65)
time.sleep(2)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(1.5)
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=577, y=411)
time.sleep(0.5) 
# escrever o seu email
pyautogui.write("tikofut07@gmail.com")
time.sleep(0.5) 
# passando pro próximo campo
pyautogui.press("tab") 
pyautogui.write("070404")
time.sleep(0.5)
pyautogui.click(x=739, y=570)       
 # clique no botao de login
time.sleep(3)
#responder aba
pyautogui.click(x=1127, y=364)
time.sleep(1.5)


# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=590, y=292)
    time.sleep(0.2)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha,"codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    time.sleep(0.5)
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    time.sleep(0.5)
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim