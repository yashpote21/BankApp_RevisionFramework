import time

from Utilities.readProperties import ReadConfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.Search_User_Page import Search_User_Class


class Test_Search_User:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()


    def test_search_user_004(self,setup):
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.lp.Click_Login_Link()
        self.lp.Enter_Username(self.Username)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login_Button()
        self.su = Search_User_Class(self.driver)
        self.su.Click_Link_User_Management()
        self.su.Enter_UserName("Tushar1")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(5)
        self.su.Click_Search_User_Button()
        time.sleep(3)
        if self.su.Validate_Search_User() == "pass":
            assert True
        else:
            assert False


