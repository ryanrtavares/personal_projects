import pyautogui
import time
from pyautogui import ImageNotFoundException

try:

    def captura_coord():
        x,y = pyautogui.position()
        print(f"{x}, {y}")

    def abre_navegdor():
        pyautogui.click(-1593, 838)
        time.sleep(2)
        pyautogui.doubleClick(697, 669)

    def acessa_site():
        time.sleep(3)
        pyautogui.click(320, 72)
        pyautogui.write('https://www.google.com/recaptcha/api2/demo')
        pyautogui.press('enter')

    def faz_captcha():
        time.sleep(3)
        pyautogui.click(56, 466)
        time.sleep(2)
        pyautogui.click(58, 524)
        time.sleep(4)
        
    def acessa_bnotas():
        with pyautogui.hold('win'):
            pyautogui.press('r')
        pyautogui.doubleClick(105, 916)
        pyautogui.press('backspace')
        pyautogui.write('notepad')
        pyautogui.click(175, 998)

    def escreve_msg():
        time.sleep(2)
        with pyautogui.hold('ctrl'):
            pyautogui.press('a')
        time.sleep(1)
        pyautogui.press("backspace")
        pyautogui.write('Lorem Ipsum', interval=0.05)
        pyautogui.press("space")
        pyautogui.write('-')
        pyautogui.press("space")
        pyautogui.write('deliberadamente lento', interval=0.15)

    def localiza_caixa():
        loc = pyautogui.locateOnScreen('teste_print.png', confidence=0.8)
        if loc:
            print(f"Localiza-se em: {loc}")
        else:
            print("Não localizado")
        
        left, top, width, height = loc

        centro_x = left + (width / 2)
        centro_y = top + (height / 2)

        pyautogui.moveTo(centro_x, centro_y, duration=2)


    if __name__ == "__main__":

            # captura_coord()
            # abre_navegdor()
            # acessa_site()
            # faz_captcha()
            acessa_bnotas()
            escreve_msg()
            localiza_caixa()

except ImageNotFoundException:

    print("Não foi possível localizar o objeto")