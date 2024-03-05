# Passo a Passo do projeto
# 1- entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2- fazer login
# 3- importar a base de dados
# 4- cadastrar 1 produto
# 5- repetir o processo de cadastro até acabar

# biblioteca
import pyautogui
import time
import pandas

# pausa entre os comandos pyautogui

pyautogui.PAUSE = 0.4


# -----------------abrir o link no navegador-------------------------

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(url)
pyautogui.press("enter")

time.sleep(1.5)

# ----------------------------login--------------------------
pyautogui.click(x=573, y=411)
pyautogui.write('email')
pyautogui.press("tab")
pyautogui.write("senha123456")
pyautogui.click(x=654, y=599)

time.sleep(1)

# ---------------------- cadastrando produto --------------------
# importando banco de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=465, y=288)

    # código
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, "obs"])

    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    # rolar a tela para cima(inicio)
    pyautogui.scroll(5000)  