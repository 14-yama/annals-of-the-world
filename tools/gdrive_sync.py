from google.oauth2 import service_account
from googleapiclient.discovery import build
import os


def authenticate(service_account_file: str = None):
    SERVICE_ACCOUNT_FILE = service_account_file or os.getenv("GDRIVE_SERVICE_ACCOUNT", "credentials.json")
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    service = build('drive', 'v3', credentials=credentials)
    return service


def main():
    service = authenticate()

    # Test the connection by listing the first 10 files
    try:
        results = service.files().list(pageSize=10).execute()
        files = results.get('files', [])

        if not files:
            print("No files found.")
        else:
            print("Files:")
            for file in files:
                print(f"{file['name']} ({file['id']})")
    except Exception as e:
        print("Error accessing Drive:", str(e))


if __name__ == '__main__':
    main()
