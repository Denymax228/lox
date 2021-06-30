from selenium import webdriver
import pyautogui as pg



driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=hCODBIQnbH0")
# btn=driver.find_element_by_class_name("ytd-searchbox-spt ")
# btn.click()
# pg.typewrite("A4\n",0.5)

# дальше смотри на ютубе как пользоваться. ок. докачивай дискорд. а ещё лучше сервер создать и добавить тебя иеня и Кириллаю А он согласен ?да. Он сможет сейччас с нами
height, width = pg.size()
while True:
    try:
        pg.moveTo(530,550)
        if pg.position() == [height, 0]:
            quit()
    except:
        input('Press ENTER to exit')
        quit()




