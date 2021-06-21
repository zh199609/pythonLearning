from requests import Response

from apiTestP2P.app import BASE_URL


class loginAPI():

    def __init__(self) -> None:
        self.imgCode_rul = imgCode_rul = BASE_URL + '/common/public/verifycode1/'

    def getImgCode(self, session, r) -> Response:
        url = self.imgCode_rul + r
        response = session.get(url)
        return response
