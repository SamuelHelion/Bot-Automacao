import pyautogui
import time

time.PAUSE = 4.5

# #Abrir a ferramenta/ o sistema/ programa
pyautogui.press("win")
pyautogui.write("escolaweb")
pyautogui.press("enter")

#INSERINDO LOGIN
pyautogui.sleep(6.8)
pyautogui.click(x=723, y=273)
pyautogui.sleep(1)
pyautogui.hotkey("ctrl","a")
pyautogui.press("delete")
pyautogui.write("Estudante@gmail.com")#USUARIO
pyautogui.press("tab")
pyautogui.write("***********")#SENHA
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.sleep(12.5)

#ENTRANDO NO CORRETOR DE PROVAS
pyautogui.click(x=123, y=322)
pyautogui.press('tab')
pyautogui.write('cent')
pyautogui.press('enter')
pyautogui.leftClick(x=909, y=493)
pyautogui.click(x=102, y=313)
pyautogui.click(x=1053, y=153)
pyautogui.write('329')
pyautogui.sleep(6)
pyautogui.leftClick(x=789, y=264)# Centro da prova selecionada
time.sleep(3)

#Questão 1 a 45
pyautogui.leftClick(x=630, y=237) #BOTÃO DE NOVA QUESTÃO
pyautogui.press('tab')
pyautogui.write('45')
pyautogui.press('tab')
pyautogui.write('Comp')#DISCIPLINA QUE RECEBERÁ DEPOIS O GABARITO
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('avaliação 2')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')#SALVANDO CONFIGURAÇÃO
pyautogui.sleep(5)

#Questão de 46 a 90
pyautogui.leftClick(x=680, y=233)#BOTÃO DE NOVA QUESTÃO
pyautogui.write('46')
pyautogui.press('tab')
pyautogui.write('90')
pyautogui.press('tab')
pyautogui.write('Hist')#DISCIPLINA QUE RECEBERÁ DEPOIS O GABARITO
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('av2')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')#SALVANDO CONFIGURAÇÃO

pyautogui.click(x=1232, y=278)
pyautogui.scroll(150000)
pyautogui.sleep(2)   
pyautogui.click(x=973, y=309)
pyautogui.press('backspace')
pyautogui.sleep(1)


#ACESSANDO ARQUIVOS E ALIMENTANDO SISTEMA

import pandas as pd

documento = pd.read_csv('gabaritoav2-1.csv')#ARQUIVO RECEBIDO

#print(documento)

for linha in documento.index:
   
   codigo = documento.loc[linha, "Gabarito"]

   pyautogui.write(codigo)

   pyautogui.press('down')

pyautogui.leftClick(x=531, y=68)
pyautogui.hotkey('alt','f4')
