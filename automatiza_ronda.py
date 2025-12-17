import pyautogui

try:

    def captura_coord():
        x,y = pyautogui.position()
        return x,y

    def navega_tela():
        pyautogui.moveTo(-1715, 4)

    def clica_tela():
        pyautogui.click()


    if __name__ == "__main__":

        captura_coord()
        navega_tela()
        clica_tela()

except:

    print("Não foi possível executar")

