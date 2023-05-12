from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    TitleString = (By.XPATH, "//visual-container[@class='visual-container-component ng-star-inserted'][5]/transform/div/div[2]/div/visual-modern/div/div/div/p/span")

    def Title(self):
        return self.driver.find_element(*HomePage.TitleString)

    InstitueDropdown =(By.XPATH,"//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div/i")

    def Institue(self):
        return self.driver.find_element(*HomePage.InstitueDropdown)

    InstituteName=(By.XPATH,"//span[@title='G P Mumbai']")
    def InstituteName1(self):
        return self.driver.find_element(*HomePage.InstituteName)

    institutecheckbox=(By.XPATH,"//div[@class='row'][2]/div")
    def checkbox(self):
        return self.driver.find_element(*HomePage.institutecheckbox)

    slicier= (By.XPATH,"//span[text()='G P Mumbai']/ancestor::div[contains(@class, 'slicerItemContainer')]")
    def slicier1(self):
        return self.driver.find_element(*HomePage.slicier)

    imageBag= (By.XPATH,"//div[@class='imageBackground'][3]")
    def imageBag1(self):
        return self.driver.find_element(*HomePage.imageBag)

    imageBag3=(By.XPATH,"//div[@class='imageBackground'][1]")
    def imageBag2(self):
        return self.driver.find_element(*HomePage.imageBag3)

    student=(By.XPATH,"//h3[normalize-space()='Students'][1]")
    def student1(self):
        return self.driver.find_element(*HomePage.student)

    number=(By.XPATH,"//*[name()='tspan'][normalize-space()='39'][1]")
    def number1(self):
        return self.driver.find_element(*HomePage.number)

    nextPage=(By.XPATH,"//div[@class='imageBackground'][4]")
    def nextPage1(self):
        return self.driver.find_element(*HomePage.nextPage)

    kulkarni=(By.XPATH,"// *[name() = 'tspan'][normalize - space() = 'D B Kulkarni'][1]")
    def kulkarni1(self):
        return self.driver.find_element(*HomePage.kulkarni)
