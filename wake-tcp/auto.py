import pyautogui, time

# move to hyperterminal icon
print("İmleç HyperTerminal ikonuna götürülüyor")
pyautogui.moveTo(25, 867)

# run hyperterminal
print("HyperTerminal çalıştırılıyor")
pyautogui.doubleClick()

# wait for HyperTerminal to open
print("HyperTerminal'in açılması bekleniyor")
time.sleep(15)

# enter modem name
print("Modem ismi giriliyor")
pyautogui.write('a')

# enter tuşuna basılıyor
print("Enter tuşuna basılıyor")
pyautogui.press('enter')

# wait for Connect To window to open
print("Bağlantı penceresinin açılması bekleniyor")
time.sleep(10)

# move to dropdown menu
print("Dropdown menüye hareket ediliyor")
pyautogui.moveTo(712, 524)

# click dropdown menu
print("Dropdown menüye tıklanıyor")
pyautogui.click()

# wait for menu to load
print("Menünün yüklenmesi bekleniyor")
time.sleep(5)

# move to TCP option
print("TCP seçeneğine hareket ediliyor")
pyautogui.moveTo(635, 554)

# click TCP option
print("TCP seçeneğine tıklanıyor")
pyautogui.click()

# wait for new inputs to load
print("Yeni inputların yüklenmesi bekleniyor")
time.sleep(5)

# enter host address
print("Host adresi giriliyor")
pyautogui.write('192.168.10.212', interval=0.1)

# move to port number input
print("Port numarası inputuna hareket ediliyor")
pyautogui.moveTo(567, 456)

# click port number input
print("Port numara inputuna tıklanıyor")
pyautogui.click()

# remove 2 digits
print("Placeholder siliniyor")
pyautogui.press('backspace')
pyautogui.press('backspace')

# enter port number
print("Port numarası giriliyor")
pyautogui.write("9090", interval=0.1)

# move to OK Button
print("OK butonuna hareket ediliyor")
pyautogui.moveTo(600, 566)

# click OK button
print("OK Butonuna tıklanıyor")
pyautogui.click()

# wait for connection
print("Bağlantı için bekleniyor")
time.sleep(3)

# move to Transfer dropdown menu
print("Transfer dropdown menüsüne hareket ediliyor")
pyautogui.moveTo(330, 195)

# click Transfer dropdown
print("Transfer dropdown menüsüne tıklanıyor")
pyautogui.click()

# wait for options to load
print("Seçeneklerin yüklenmesi bekleniyor")
time.sleep(3)

# move to Send Text file
print("Send Text File seçeneğine hareket ediliyor")
pyautogui.moveTo(392, 286)

# click Send Text File
print("Send Text File seçeneğine tıklanıyor")
pyautogui.click()

# wait for file dialog to load
print("Dosya diyalogunun yüklenmesi bekleniyor")
time.sleep(10)

# move to filename input
print("Dosya ismi inputuna hareket ediliyor")
pyautogui.moveTo(515, 680)

# click filename input
print("Dosya ismi inputuna tıklanıyor")
pyautogui.click()

# enter filename
print("Dosya ismi giriliyor")
pyautogui.write("open.txt", interval=0.1)

# move to OK button
print("OK butonuna hareket ediliyor")
pyautogui.moveTo(950, 714)

# click OK button
print("OK butonuna tıklanıyor")
pyautogui.click()

print("İşlem tamamlandı")