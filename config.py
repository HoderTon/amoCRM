from dataclasses import dataclass
from pathlib import Path
from typing import Union
from configparser import ConfigParser

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjIzNGVjNGM3MDRlYWUwMzM4ZDgwNTM2NjBmODE5ZDgyOWIyMTFlNDMxM2Y0OTM1MDQ0MjViODBlM2ZhZWVkOTkyM2IzMzVmYWVhMTZhNDI4In0.eyJhdWQiOiJhYTNjM2Q4OC01YWU0LTQ4ZDYtOWVlYy1kYzczYTA3MjhhZGMiLCJqdGkiOiIyMzRlYzRjNzA0ZWFlMDMzOGQ4MDUzNjYwZjgxOWQ4MjliMjExZTQzMTNmNDkzNTA0NDI1YjgwZTNmYWVlZDk5MjNiMzM1ZmFlYTE2YTQyOCIsImlhdCI6MTYzOTM5MTU1MCwibmJmIjoxNjM5MzkxNTUwLCJleHAiOjE2Mzk0Nzc5NTAsInN1YiI6Ijc3MjM2MzkiLCJhY2NvdW50X2lkIjoyOTg3NDQ2Mywic2NvcGVzIjpbInB1c2hfbm90aWZpY2F0aW9ucyIsImNybSIsIm5vdGlmaWNhdGlvbnMiXX0.sHgLADg22kwOcxo5g078c5yK2ZQM5fJQiMNDbEJt_LnhXYW-qMessUzFPMumwL0kPps1cxmLegV8P5I5UCxxFvPrxNh0pchkT8Rf_cc9yvvlzk9QpZ80-IBPGNFQu2UEiiuxpOnb0hHcRACCTmnNiBsCJREaCd8wPPpDKy82EGSMxco7VusJ9o1-NlajlggUDYdO1SUSRoXpXXN9vF2KwkSkZ7DsMObOuflG3Fyp6ZZ-3i7e0_ELX9F58_CDRxAB3zEa--tQRrzxEHcJ34tUN2CHr-nJJvVvpnWzDfjRlISmrmGLeyhvicuxxm8IbwSTbuz2MYXCb84sVD_VvtLv5g'
refresh_token = 'def502000ff9136875efb4e5a9c4999f01712a7715b2a41bd3072fe5def11a2c431a2cd0036fa52ac177f8f146a2026872e79bfc921999daafb0fb65999e06f54eadc13fdbae6b698ddad5517a54488ad1053835bea6a4b2e7c16382d5c73d893735b2423f4a0fcdaba5f40aed5f08d455a4b1e1e88099fa46b78a5c1187978d615dc6c1f70d466accfeab39d808a65289d152af484ea7a78e48d2dcb2cd941e8a0f69183ee4fa22e30b3964b2e28aea0433451684ae14851973856c8a2468c377fa5b6273b33771c3f6d1daf6b4e5810fc94f50ca6769074e6b7a4b65e68c9da52d27b84b170f9d810830e28f3a238bf8a3fb3eb78bf7071d6af2369552cbafdec0d7368e3075e166e1b535f9ff1e1db0c7efc208ad0186f24df875599059a53e04ffac1e01b0d15600fb99554c3574c15028a408f1dd35798eab337f11848d702f77be6265d301de7d92b3a43b2b1247a6398d47d395f87da710e97d60673ccb84a014675a5581987b156ca3301e6f03d99ecd161eb8baa9aa888c210dc8672e4b2a6fc804c8c41cd597d7c45a67d93c7fb17b35c4cfd5f5972e0141a8ab7cdac54b8c286665ca13f8da8d3fc08c0f0f7d195bf9d8db0b794a180df813687e17a76a54de4236d14e25'

URL_ADD_CONTACT = 'https://diotonepl.amocrm.com/api/v2/contacts/add'


@dataclass
class AmoCrmConfig:
    client_id: str
    client_secret: str
    redirect_uri: str = 'https://google.com.ua'
    access_token: str = ""
    refresh_token: str = ""
    subdomain: str = 'diotonepl.'

    def __post_init__(self):
        self.inited = all((self.subdomain, self.client_secret, self.client_id, self.redirect_uri))


def update_config_credentials(path: Union[str, Path], *, refresh_token, access_token):
    config = ConfigParser()
    config.read(path)
    config.set('amocrm', 'access_token', access_token)
    config.set('amocrm', 'refresh_token', refresh_token)

    with open(path, 'w') as file:
        config.write(file)


def load_config(path: Union['str', Path]) -> AmoCrmConfig:
    config = ConfigParser()
    config.read(path)
    return AmoCrmConfig(**config['amocrm'])




# headers_ac = {"Authorization": f'Bearer {access_token}'}
# contact = dict()
# contact['add'] = {
#     'name': 'Jason',
#     'responsible_user_id': 504141,
#     'created_by': 504141,
#     'tags': 'important',
#     'leads_id': ['45615', '43510'],
#     'company_id': 30615,
#     'custom_fields': 'df',
# }
# print(contact)
# add_contact = requests.post(URL_ADD_CONTACT, headers=headers_ac, params=params)
# print(add_contact.text)
