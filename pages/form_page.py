from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    URL = "https://demoqa.com/automation-practice-form"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))

    def fill_name(self, firstname, lastname):
        self.driver.find_element(By.ID, "firstName").send_keys(firstname)
        self.driver.find_element(By.ID, "lastName").send_keys(lastname)

    def fill_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def select_gender(self, gender):
        gender = gender.lower()
        if gender == "male":
            locator = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
        elif gender == "female":
            locator = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
        else:
            locator = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
        self.safe_click(locator)

    def fill_phone(self, phone_number):
        self.driver.find_element(By.ID, "userNumber").send_keys(phone_number)

    def select_date_of_birth(self, day, month, year):
        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        month_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_select.select_by_visible_text(month)
        year_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_select.select_by_visible_text(str(year))
        days = self.driver.find_elements(By.CSS_SELECTOR, ".react-datepicker__day:not(.react-datepicker__day--outside-month)")
        for d in days:
            if d.text == str(day):
                d.click()
                break

    def add_subject(self, subject):
        subject_input = self.driver.find_element(By.ID, "subjectsInput")
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)

    def select_hobbies(self, hobbies_list):
        hobby_map = {
            "Sports": "hobbies-checkbox-1",
            "Reading": "hobbies-checkbox-2",
            "Music": "hobbies-checkbox-3"
        }
        for hobby in hobbies_list:
            checkbox_for = hobby_map[hobby]
            locator = (By.CSS_SELECTOR, f"label[for='{checkbox_for}']")
            self.safe_click(locator)

    def upload_picture(self, file_path):
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    def fill_address(self, address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)

    def select_state(self, state):
        self.safe_click((By.ID, "state"))
        # Attendre l'option correspondante dans le menu
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@id='stateCity-wrapper']//div[@role='option' and text()='{state}']"))
        )
        option_locator = (By.XPATH, f"//div[@id='stateCity-wrapper']//div[@role='option' and text()='{state}']")
        self.safe_click(option_locator)

    def select_city(self, city):
        self.safe_click((By.ID, "city"))
        # Attendre l'option correspondante dans le menu
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@id='stateCity-wrapper']//div[@role='option' and text()='{city}']"))
        )
        option_locator = (By.XPATH, f"//div[@id='stateCity-wrapper']//div[@role='option' and text()='{city}']")
        self.safe_click(option_locator)

    def submit_form(self):
        locator = (By.ID, "submit")
        self.safe_click(locator, js_click=True)

    def safe_click(self, locator, js_click=False):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)

        try:
            elem.click()
        except:
            if js_click:
                self.driver.execute_script("arguments[0].click();", elem)
            else:
                ActionChains(self.driver).move_to_element(elem).click().perform()
