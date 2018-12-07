import io
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from googleapiclient.discovery import Resource
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient import discovery

from src.config import conf


API_NAME = 'drive'
API_VERSION = 'v3'
FILE_NAME = 'sorties'


class GoogleAut:
    @property
    def google_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=conf.client_secret_file,
            scopes=conf.google_scopes)
        return flow.run_local_server(
            host='localhost',
            port=8123,
            authorization_prompt_message='Please visit this url: {url}',
            open_browser=True)


class Drive(GoogleAut):
    _google_api_service: Resource

    def __init__(self):
        self._google_api_service = discovery.build(
            serviceName=API_NAME,
            version=API_VERSION,
            credentials=self.google_credentials)

    def download_spreadsheet(self):
        request = self._google_api_service.files().export_media(
            fileId=conf.sheet_id,
            mimeType='text/csv')
        fh = io.FileIO('resources/data/{file_name}.csv'.format(file_name=FILE_NAME), "wb")
        downloader: MediaIoBaseDownload = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()