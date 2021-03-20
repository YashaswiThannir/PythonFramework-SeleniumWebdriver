import pytest

from pytests.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad)
        print(dataLoad)
        log.info(dataLoad[2])
        print(dataLoad[2])
