from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

name = input("Enter the name of user or group : ")
# msg = input('Enter the message : ')
# count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title="{0}"]'.format(name))
user.click()

footer = driver.find_element_by_xpath('//footer')
all_div = footer.find_elements_by_tag_name("div")

text_inserted = False
for div in all_div:
    if text_inserted is False:
        try:
            msg_box = div.find_element_by_class_name("copyable-text")
            msg_box.send_keys('test')
            # despues de insertar el texto hay que meter un sleep y buscar de nuevo el boton
            div.find_element_by_xpath('//button').click()
            text_inserted = True
        except Exception as exc:
            print(exc)
    else:
        continue
# for i in range(count):
#    msg_box.send_keys(msg)
    # driver.find_element_by_class_name('compose-btn-send').click()
