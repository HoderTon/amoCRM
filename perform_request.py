from configparser import ConfigParser
import httpx
from get_access import refresh_token, access_token, params_auth
from amoCRM_Auth import AmoCrmAPI
from config import AmoCrmConfig, update_config_credentials

payload = {'add': {
      'name': 'Jason Nash',
      'responsible_user_id': 29874463,
      'created_by': 29874463,
      'created_at': "1509051600",
      'tags': "important, delivery",
      'leads_id': [],
      'company_id': 204775,
}}


update_config_credentials('./config.ini', access_token=access_token, refresh_token=refresh_token)


cla = lead_config(**params_auth, refresh_token=refresh_token)
add_contact = httpx.post()
