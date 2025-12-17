import pyautogui

try:

    def captura_coord():
        x,y = pyautogui.position()
        print(f"{x}, {y}")

    def navega_tela():
        pyautogui.click(-1226, 834)
        pyautogui.click(-1813, 18)
        pyautogui.click(-1710, 336)
        pyautogui.click(-1203, 774)

    def escreve_tela()


    if __name__ == "__main__":

        captura_coord()
        navega_tela()

except:

    print("Não foi possível executar")

