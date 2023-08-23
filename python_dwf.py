import pyautogui
import pyperclip
import time
from unidecode import unidecode

def a():
    pyautogui.hotkey('win', 'e')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')

def b(caminho_dwf_para_abrir):
    pyperclip.copy(caminho_dwf_para_abrir)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

def abrir_o_dwf_indicado_pelo_usuario():
    caminho_dwf_para_abrir = input("Qual o caminho do dwf que deseja abrir:\n ")
    a()
    time.sleep(1)
    b(caminho_dwf_para_abrir)

abrir_o_dwf_indicado_pelo_usuario()
