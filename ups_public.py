import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PyQt5.QtGui import QIcon
from selenium.webdriver.common.by import By
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, \
    QLabel, QPushButton, QFormLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        font2 = QtGui.QFont()
        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(12)

        self.lb_a1 = QLabel()
        self.lb_a1.setText('Hello World')
        self.lb_a1.setFont(font1)
        self.lb_a1.setStyleSheet("border-style: solid; border-width: 1px; border-color: black;")

        self.lb_a2 = QLabel()
        self.lb_a2.setText('Hello World')
        self.lb_a2.setFont(font2)
        

        self.lb_a3 = QLabel()
        self.lb_a3.setText('Hello World')
        self.lb_a3.setFont(font2)
        

        self.lb_a4 = QLabel()
        self.lb_a4.setText('Hello World')
        self.lb_a4.setFont(font2)

        self.lb_a5 = QLabel()
        self.lb_a5.setText('Hello World')
        self.lb_a5.setFont(font2)

        self.lb_a6 = QLabel()
        self.lb_a6.setText('Hello World')
        self.lb_a6.setFont(font2)

        self.lb_a7 = QLabel()
        self.lb_a7.setText('Hello World')
        self.lb_a7.setFont(font2)

        self.lb_a8 = QLabel()
        self.lb_a8.setText('Hello World')
        self.lb_a8.setFont(font2)

        self.lb_a9 = QLabel()
        self.lb_a9.setText('Hello World')
        self.lb_a9.setFont(font2)

        self.lb_a10 = QLabel()
        self.lb_a10.setText('Hello World')
        self.lb_a10.setFont(font2)

        self.lb_a11 = QLabel()
        self.lb_a11.setText('           ')

        self.lb_a12 = QLabel()
        self.lb_a12.setText('           ')

        self.lb_c1 = QLabel()
        self.lb_c1.setText('Hello World')
        self.lb_c1.setFont(font1)
        self.lb_c1.setStyleSheet("border-style: solid; border-width: 1px; border-color: black;")

        self.lb_c2 = QLabel()
        self.lb_c2.setText('Hello World')
        self.lb_c2.setFont(font2)

        self.lb_c3 = QLabel()
        self.lb_c3.setText('Hello World')
        self.lb_c3.setFont(font2)

        self.lb_c4 = QLabel()
        self.lb_c4.setText('Hello World')
        self.lb_c4.setFont(font2)

        self.lb_c5 = QLabel()
        self.lb_c5.setText('Hello World')
        self.lb_c5.setFont(font2)

        self.lb_c6 = QLabel()
        self.lb_c6.setText('Hello World')
        self.lb_c6.setFont(font2)

        self.lb_c7 = QLabel()
        self.lb_c7.setText('Hello World')
        self.lb_c7.setFont(font2)

        self.lb_c8 = QLabel()
        self.lb_c8.setText('Hello World')
        self.lb_c8.setFont(font2)

        self.lb_c9 = QLabel()
        self.lb_c9.setText('Hello World')
        self.lb_c9.setFont(font2)

        self.lb_c10 = QLabel()
        self.lb_c10.setText('Hello World')
        self.lb_c10.setFont(font2)

        self.lb_c11 = QLabel()
        self.lb_c11.setText('Hello World')
        self.lb_c11.setFont(font2)

        self.lb_c12 = QLabel()
        self.lb_c12.setText('Hello World')
        self.lb_c12.setFont(font2)

        fbox = QFormLayout()
        fbox.setHorizontalSpacing(60)
        fbox.setVerticalSpacing(15)
        self.setLayout(fbox)
        self.setFixedSize(720,415)

        fbox.addRow(self.lb_a1,self.lb_c1)
        fbox.addRow(self.lb_a2,self.lb_c2)
        fbox.addRow(self.lb_a3,self.lb_c3)
        fbox.addRow(self.lb_a4,self.lb_c4)
        fbox.addRow(self.lb_a5,self.lb_c5)
        fbox.addRow(self.lb_a6,self.lb_c6)
        fbox.addRow(self.lb_a7,self.lb_c7)
        fbox.addRow(self.lb_a8,self.lb_c8)
        fbox.addRow(self.lb_a9,self.lb_c9)
        fbox.addRow(self.lb_a10,self.lb_c10)
        fbox.addRow(self.lb_a11,self.lb_c11)
        fbox.addRow(self.lb_a12,self.lb_c12)
        
        self.timer = QTimer()                                
        self.timer.setInterval(60000)   # Миллисекунды        
        self.timer.timeout.connect(self.updateInfo) 
        self.app = QtWidgets.QApplication([])
        self.wb_path = QtWidgets.QFileDialog.getOpenFileName()        
        self.updateInfo()
        self.timer.start()

    def updateInfo(self):
        try:
            browser1.get('https://*********')
            time.sleep(1)
            dop3 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[2]')
            dop3.click()
            time.sleep(1)
            dop4 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[3]')
            dop4.click()

            self.lb_a1.setText(browser1.find_element(By.ID,'value_DeviceStatus').text)
            self.lb_a2.setText("Уровень нагрузки:   " + browser1.find_element(By.ID,'value_RealPowerPct').text + " %")
            self.lb_a3.setText("Время работы от батарей   " + browser1.find_element(By.ID,'value_RuntimeRemaining').text + " мин.")
            self.lb_a4.setText("Температура:   " + browser1.find_element(By.ID,'value_InternalTemp').text)
            self.lb_a5.setText("Входное напряжение:   " + browser1.find_element(By.ID,'value_InputVoltage').text + " эВ")
            self.lb_a6.setText("Выходное напряжение:   " + browser1.find_element(By.ID,'value_OutputVoltage').text + " эВ")
            self.lb_a7.setText("Частота входного напряжения:   " + browser1.find_element(By.ID,'value_InputFrequency').text + " Гц")
            self.lb_a8.setText("Частота выходного напряжения:   " + browser1.find_element(By.ID,'value_OutputFrequency').text + " Гц")
            self.lb_a9.setText("Заряд батарей:   " + browser1.find_element(By.ID,'value_BatteryCharge').text + " %")
            self.lb_a10.setText("Вольтаж постоянного тока:   " + browser1.find_element(By.ID,'value_VoltageDC').text + " В")
            #print("считал открытый браузер1")
        except:
            try:  
                browser1.close()
                browser1.quit()                                     
                options1 = webdriver.ChromeOptions()
                options1.add_argument('--ignore-certificate-errors')
                options1.add_argument("headless")
                browser1 = webdriver.Chrome(executable_path=str(self.wb_path[0]), chrome_options=options1)
                browser1.get('https://*********')
                time.sleep(1)
                username_input1 = browser1.find_element(By.NAME,'j_username')
                username_input1.clear()
                username_input1.send_keys('*********')
                time.sleep(1)
                password_input1 = browser1.find_element(By.NAME,'j_password')
                password_input1.clear()
                password_input1.send_keys('*********')
                password_input1.send_keys(Keys.ENTER)
                time.sleep(1)
                dop3 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[2]')
                dop3.click()
                time.sleep(1)
                dop4 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[3]')
                dop4.click()

                self.lb_a1.setText(browser1.find_element(By.ID,'value_DeviceStatus').text)
                self.lb_a2.setText("Уровень нагрузки:   " + browser1.find_element(By.ID,'value_RealPowerPct').text + " %")
                self.lb_a3.setText("Время работы от батарей   " + browser1.find_element(By.ID,'value_RuntimeRemaining').text + " мин.")
                self.lb_a4.setText("Температура:   " + browser1.find_element(By.ID,'value_InternalTemp').text)
                self.lb_a5.setText("Входное напряжение:   " + browser1.find_element(By.ID,'value_InputVoltage').text + " эВ")
                self.lb_a6.setText("Выходное напряжение:   " + browser1.find_element(By.ID,'value_OutputVoltage').text + " эВ")
                self.lb_a7.setText("Частота входного напряжения:   " + browser1.find_element(By.ID,'value_InputFrequency').text + " Гц")
                self.lb_a8.setText("Частота выходного напряжения:   " + browser1.find_element(By.ID,'value_OutputFrequency').text + " Гц")
                self.lb_a9.setText("Заряд батарей:   " + browser1.find_element(By.ID,'value_BatteryCharge').text + " %")
                self.lb_a10.setText("Вольтаж постоянного тока:   " + browser1.find_element(By.ID,'value_VoltageDC').text + " В")
                #print("закрыл старый, открыл новый считал1")
            except:
                options1 = webdriver.ChromeOptions()
                options1.add_argument('--ignore-certificate-errors')
                options1.add_argument("headless")
                browser1 = webdriver.Chrome(executable_path=str(self.wb_path[0]), chrome_options=options1)
                browser1.get('https://1*********')
                time.sleep(1)
                username_input1 = browser1.find_element(By.NAME,'j_username')
                username_input1.clear()
                username_input1.send_keys('*********')
                time.sleep(1)
                password_input1 = browser1.find_element(By.NAME,'j_password')
                password_input1.clear()
                password_input1.send_keys('*********')
                password_input1.send_keys(Keys.ENTER)
                time.sleep(1)
                dop3 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[2]')
                dop3.click()
                time.sleep(1)
                dop4 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[3]')
                dop4.click()

                self.lb_a1.setText(browser1.find_element(By.ID,'value_DeviceStatus').text)
                self.lb_a2.setText("Уровень нагрузки:   " + browser1.find_element(By.ID,'value_RealPowerPct').text + " %")
                self.lb_a3.setText("Время работы от батарей   " + browser1.find_element(By.ID,'value_RuntimeRemaining').text + " мин.")
                self.lb_a4.setText("Температура:   " + browser1.find_element(By.ID,'value_InternalTemp').text)
                self.lb_a5.setText("Входное напряжение:   " + browser1.find_element(By.ID,'value_InputVoltage').text + " эВ")
                self.lb_a6.setText("Выходное напряжение:   " + browser1.find_element(By.ID,'value_OutputVoltage').text + " эВ")
                self.lb_a7.setText("Частота входного напряжения:   " + browser1.find_element(By.ID,'value_InputFrequency').text + " Гц")
                self.lb_a8.setText("Частота выходного напряжения:   " + browser1.find_element(By.ID,'value_OutputFrequency').text + " Гц")
                self.lb_a9.setText("Заряд батарей:   " + browser1.find_element(By.ID,'value_BatteryCharge').text + " %")
                self.lb_a10.setText("Вольтаж постоянного тока:   " + browser1.find_element(By.ID,'value_VoltageDC').text + " В")
                #print("первый раз открыл браузер и считал1")

        
        #___________________________________________________________________________________________________________________________________________________________
        try:
            browser2.get('*********/')
            time.sleep(1) 
            self.lb_c1.setText(browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[6]/td[2]/table/tbody/tr/td[2]').text + " Line")
            self.lb_c2.setText("Напряжение батареи:    " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[1]/td[2]').text) #xpath не полный взятый с копии сайта на рабочем столе
            self.lb_c3.setText("Выходная частота:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[2]/td[2]').text)
            self.lb_c4.setText("Выходное напряжение:    " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[3]/td[2]').text)
            self.lb_c5.setText("Выходной ток:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[4]/td[2]').text)
            self.lb_c6.setText("Общая полная мощность:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[5]/td[2]').text)
            self.lb_c7.setText("Общая активная мощность:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[6]/td[2]').text)
            self.lb_c8.setText("Состояние батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]').text)
            self.lb_c9.setText("Источник питания:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text)
            self.lb_c10.setText("Уровень нагрузки:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text)
            self.lb_c11.setText("Емкость батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td[2]').text)
            self.lb_c12.setText("Время работы от батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[5]/td[2]').text)  
            #print("считал открытый браузер2")
        except:
            try:
                browser2.close()
                browser2.quit()
                options2 = webdriver.ChromeOptions() # Устанавливаем настройки для эмулируемого браузера
                options2.add_argument('--ignore-certificate-errors')
                options2.add_argument("headless") # Режим, при котором окно браузера будет работать в фоновом режиме
                browser2 = webdriver.Chrome(executable_path=str(self.wb_path[0]), chrome_options=options2)
                browser2.get('http://*********/')
                time.sleep(1)   
                username_input2 = browser2.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div[1]/div[1]/input')
                username_input2.clear()
                username_input2.send_keys('*********')
                time.sleep(1)
                password_input2 = browser2.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div[2]/div[1]/input')
                password_input2.clear()
                password_input2.send_keys('*********')
                password_input2.send_keys(Keys.ENTER)
                time.sleep(1)

                self.lb_c1.setText(browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[6]/td[2]/table/tbody/tr/td[2]').text + " Line")
                self.lb_c2.setText("Напряжение батареи:    " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[1]/td[2]').text) #xpath не полный взятый с копии сайта на рабочем столе
                self.lb_c3.setText("Выходная частота:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[2]/td[2]').text)
                self.lb_c4.setText("Выходное напряжение:    " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[3]/td[2]').text)
                self.lb_c5.setText("Выходной ток:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[4]/td[2]').text)
                self.lb_c6.setText("Общая полная мощность:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[5]/td[2]').text)
                self.lb_c7.setText("Общая активная мощность:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[6]/td[2]').text)
                self.lb_c8.setText("Состояние батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c9.setText("Источник питания:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c10.setText("Уровень нагрузки:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c11.setText("Емкость батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c12.setText("Время работы от батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[5]/td[2]').text)
                #print("закрыл старый, открыл новый считал2")
            except:
                options2 = webdriver.ChromeOptions() # Устанавливаем настройки для эмулируемого браузера
                options2.add_argument('--ignore-certificate-errors')
                options2.add_argument("headless") # Режим, при котором окно браузера будет работать в фоновом режиме
                browser2 = webdriver.Chrome(executable_path=str(self.wb_path[0]), chrome_options=options2)
                browser2.get('http://*********/')
                time.sleep(1)   
                username_input2 = browser2.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div[1]/div[1]/input')
                username_input2.clear()
                username_input2.send_keys('*********')
                time.sleep(1)
                password_input2 = browser2.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div[2]/div[1]/input')
                password_input2.clear()
                password_input2.send_keys('*********')
                password_input2.send_keys(Keys.ENTER)
                time.sleep(1)

                self.lb_c1.setText(browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[6]/td[2]/table/tbody/tr/td[2]').text + " Line")
                self.lb_c2.setText("Напряжение батареи:    " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[1]/td[2]').text) #xpath не полный взятый с копии сайта на рабочем столе
                self.lb_c3.setText("Выходная частота:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[2]/td[2]').text)
                self.lb_c4.setText("Выходное напряжение:    " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[3]/td[2]').text)
                self.lb_c5.setText("Выходной ток:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[4]/td[2]').text)
                self.lb_c6.setText("Общая полная мощность:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[5]/td[2]').text)
                self.lb_c7.setText("Общая активная мощность:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[6]/td[2]').text)
                self.lb_c8.setText("Состояние батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c9.setText("Источник питания:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c10.setText("Уровень нагрузки:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c11.setText("Емкость батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td[2]').text)
                self.lb_c12.setText("Время работы от батареи:   " + browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[5]/td[2]').text)
                #print("первый раз открыл браузер и считал2")

        #_______________________________________________________________________________________________________________
        try:
            if(self.lb_c1.text() == "On Line"):
                self.lb_c1.setStyleSheet(f"background-color: rgb(90,255,90);")
                self.lb_c1.setText("ИБП СОТИАССО подключен к сети")
            else:
                self.lb_c1.setStyleSheet(f"background-color: rgb(255,90,90);")
                self.lb_c1.setText("ИБП СОТИАССО отключен от сети")
            if(self.lb_a1.text() == "On Line"):
                self.lb_a1.setStyleSheet(f"background-color: rgb(90,255,90);")
                self.lb_a1.setText("ИБП АИСКУЭ подключен к сети")
            else:
                self.lb_a1.setStyleSheet(f"background-color: rgb(255,90,90);")
                self.lb_a1.setText("ИБП АИСКУЭ отключен от сети")
        except:
            print("")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen()
    #splash.setPixmap(QtGui.QPixmap('C:/Users/Администратор/Desktop/splash.jpg'))
    splash.showMessage('<h1> Пожалуйста подождите, идет сбор данных...</h1>')
    splash.setFixedSize(540,50)
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - 540)//2
    y = (desktop.height() - 50)//2
    splash.move(x, y)
    splash.show()
    window = Example()
    window.setWindowTitle("Статус ИБП")
    window.setWindowIcon(QIcon('ico.png'))  
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())