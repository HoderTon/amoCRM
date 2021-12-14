from dataclasses import dataclass
from pathlib import Path
from typing import Union
from configparser import ConfigParser


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
