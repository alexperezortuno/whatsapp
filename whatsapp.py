from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Whatsapp:
    name: str
    message: str
    count: int
    url: str
    driver: webdriver
    continue_app: str
    app_loop: bool

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', None)
        self.message = kwargs.get('message', None)
        self.count = kwargs.get('count', None)
        self.url = kwargs.get('url', 'https://web.whatsapp.com')
        self.app_loop = False

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)
        self.continue_app = False

    def start(self):
        print('When you want finish the script, key CTRL + C')

        if self.name is None:
            self.name = input('Enter the name of user or group : ')

        if self.message is None:
            self.message = input('Enter the message : ')

        if self.count is None:
            self.count = int(input('Enter the count : '))

        if self.app_loop == False:
            input('Enter anything after scanning QR code')

        user = self.driver.find_element_by_xpath('//span[@title="{0}"]'.format(self.name))
        user.click()

        self.insert_text()

        self.continue_app = input('You want to send another message [y/N] : ')

        if self.continue_app[0].lower() == 'y':
            self.app_loop = True
            self.clean()
            self.start()

    def insert_text(self):
        footer = self.driver.find_element_by_xpath('//footer')

        try:
            for x in range(self.count):
                msg_box = footer.find_element_by_css_selector('div > div.copyable-text.selectable-text')
                msg_box.send_keys(self.message)

                self.send_msg()
                print('Send message {0}'.format(x))
        except Exception as exc:
            print(exc)

    def send_msg(self):
        footer = self.driver.find_element_by_xpath('//footer')

        try:
            element = WebDriverWait(footer, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button > span[data-icon='send']"))
            )
            element.click()
        except Exception as exc:
            print(exc)

    def clean(self):
        self.count = None
        self.name = None
        self.message = None


start_app = Whatsapp()
start_app.start()
