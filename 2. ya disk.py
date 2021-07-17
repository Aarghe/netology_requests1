import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headers(self, token):
        return {
            'Content-Type': 'application/json',
            'Authorization': token
        }

    def upload(self):
        ya_token = ''
        get_link_to_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': 'test/testfile.txt', 'overwrite': 'true'}

        headers = self.get_headers(ya_token)
        response = requests.get(get_link_to_upload, headers=headers, params=params)
        link_to_upload = response.json()['href']

        upload_file = requests.put(link_to_upload, data=open(r'files\txt.txt', 'rb'))
        upload_file.raise_for_status()

        if upload_file.status_code == 201:
            print('file upload successfully')
        else:
            print('Error')


if __name__ == '__main__':
    uploader = YaUploader(r'files\file.txt')
    result = uploader.upload()


a = YaUploader
