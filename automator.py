from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

f = open("message.txt", "r")
message = f.read()
f.close()

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number = len(numbers)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install())
print('Sign in to Whatsapp Web')
driver.get('https://web.whatsapp.com')
input("Once whatsapp is open press enter to continue")
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print('{}/{} => Sending message to {}.'.format((idx + 1), total_number, number))
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)

                click_btn = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                sleep(1)
                click_btn.click()
                sent = True
                sleep(3)
                print('Message sent to: ' + number)
    except Exception as e:
        print('Failed to send message to ' + number + str(e))
driver.close()
