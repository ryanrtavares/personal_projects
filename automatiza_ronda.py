import pyautogui
import time

try:

    def captura_coord():
        x,y = pyautogui.position()
        print(f"{x}, {y}")

    def abre_navegdor():
        pyautogui.click(-1593, 838)
        time.sleep(2)
        pyautogui.doubleClick(697, 669)
        time.sleep(2)
        pyautogui.click(-1676, 101)
        time.sleep(5)

    def abre_conversa():
        pyautogui.click(-1580, 350)

    def escreve_tela():
        pyautogui.click(-1102, 783)
        pyautogui.write('teste')


    if __name__ == "__main__":

        captura_coord()
        abre_navegdor()
        abre_conversa()
        escreve_tela()

except:

    print("Não foi possível executar")

