import pyautogui
import time
import pandas
pyautogui.PAUSE = 1.2
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1001, y=580)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1028, y=374)
pyautogui.write("Login")
pyautogui.press("tab")
pyautogui.write("Senha")
pyautogui.press("tab")
pyautogui.press("enter")
tabela = pandas.read_csv("Hashtag\Lives\Aula 1 - Automação Cadastro de Produtos05052026\produtos.csv")
print(tabela)
for linha in tabela.index:
    # codigo
    pyautogui.click(x=1002, y=257)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
