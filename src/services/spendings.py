from src.clients.drive import Drive


def download_file():
    drive: Drive = Drive()
    drive.download_spreadsheet()
