import pytest

from BaseDriver.Base_Page import BasePage
from Test_Case import read_yaml


class PortalMenu(BasePage):
    def LoginPage(self):
        pass

    def RegisterPage(self):
        pass

    def AppDownloadPage(self):
        pass

    def AboutUsPage(self):
        pass

    def EnergyInformationPage(self):
        pass

    def TypicalCasePage(self):
        pass

    def SolutionPage(self):
        pass

    # @pytest.mark.parametrize('args', read_yaml(f'Data.yaml'))
    # def HomePage(self, args):
    #     self.do_clickElement(*args['PortalPage']['HomePageElement'])
    #
    #     from Page.BrowserClient.PortalMenu.HomePage.HomePage import HomePage
    #     return HomePage(self.driver)

    @pytest.mark.parametrize('args', read_yaml(f'Data.yaml'))
    def HomePage(self, args):
        self.do_clickElement(args['PortalPage']['HomePageElement'])

        from Page.BrowserClient.PortalMenu.HomePage.HomePage import HomePage
        return HomePage(self.driver)
