from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationModalPage:
    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_text(self):
        # Attendre que la modal soit visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        return self.driver.find_element(By.ID, "example-modal-sizes-title-lg").text
