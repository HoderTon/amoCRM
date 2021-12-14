from httpx import Client
from typing import Optional, Union, Dict
from pathlib import Path

from config import AmoCrmConfig, load_config


class NoCredentialsException(Exception):
    pass


class AmoCrmAPI:
    def __init__(self,
                 /, session: Client,
                 *, config: Optional[AmoCrmConfig] = None,
                 subdomain: Optional[str] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 refresh_token: Optional[str] = None,
                 redirect_uri: Optional[str] = None
                 ):
        self._config = config or AmoCrmConfig(
            subdomain=subdomain, client_id=client_id, client_secret=client_secret,
            redirect_uri=redirect_uri, refresh_token=refresh_token
        )
        if not self._config.inited:
            raise NoCredentialsException

        self._session = session
        self._session.base_uri = f'https://{self._config.subdomain}.amocrm.com'
        self._session.headers.update({'Authorization': f'Bearer {self._config.access_token}'})

    @classmethod
    def from_config_file(cls, session: Client, config_path: Union[str, Path]):
        config = load_config(config_path)
        return cls(session, config=config)

    @property
    def tokens(self) -> Dict[str, str]:
        return {
            'refresh_token': self._config.refresh_token,
            'access_token': self._config.access_token,
        }

    @property
    def access_ok(self) -> bool:
        return 200 <= self._session.get('/api/v4/account').status_code < 300

    def _get_access_token(self, grant_type, code=None) -> None:
        json_ = {
            'grant_type': grant_type,
            'client_id': self._config.client_secret,
            'client_secret': self._config.client_secret,
            'redirect_uri': self._config.redirect_uri,
        }
        if code is not None:
            json_['code'] = code
        elif self._config.refresh_token:
            json_['refresh_token'] = self._config.refresh_token
            result = self._session.post('/oauth2/access_token', json=json_).json()
            access_token, refresh_token = result['access_token'], result['refresh_token']

            self._config.access_token = access_token
            self._config.refresh_token = refresh_token

        def get_refresh_token_via_code(self, code) -> None:
            '''
            Метод для получения refresh и access токенов, если предыдущие отозвали
            :param code: Код авторизации из лич. кабинета amocrm
            :return:
            '''

            grant_type = 'authorization_code'
            self._get_access_token(grant_type, code)

        def update_access_token(self) -> None:
            grant_type = 'refresh_token'
            self._get_access_token(grant_type)

        def get_auth(self):
            if not self.access_ok:
                self.update_access_token()
                self._session.headers.update({'Authorization': f'Bearer {self._config.access_token}'})
