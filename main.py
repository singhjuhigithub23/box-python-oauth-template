"""main.py"""

import logging
from app.config import AppConfig

from app.box_client import get_client
import json

logging.basicConfig(level=logging.INFO)
logging.getLogger("boxsdk").setLevel(logging.CRITICAL)

conf = AppConfig()


def main():
    """
    Simple script to demonstrate how to use the Box SDK
    with oAuth2 authentication
    """

    client = get_client(conf)

    user = client.user().get()
    print("==================")
    print(f"Hello, {user.name}")
    print("------------------")
    print("Root folder items:")
    print("------------------")
    items = client.folder("0").get_items()
    # share_link = client.folder("0").get_shared_link()
    # print(share_link)
    print(items)
    for item in items:
        print(item)
        file_id = '1331431851791'

        file_download_url = client.file(file_id).get_download_url()
        modified_at= client.file(file_id).get()
        # user_name=client.user(user_id).get()

        print(file_download_url)
        data = {
            "name":item.name,
            "user":user.name,

            "modified_at":modified_at.content_modified_at,



            "id":item.id,
            "url":item.get_url(),
            "type":item.type,
            "download_url":item.get_download_url()











        }
        # file_id = '1331431851791'
        # file_content = client.file(file_id).content()
        json_string=json.dumps(data,indent=6)
        print(json_string)
        print(f"Type: {item.type} ID: {item.id} Name: {item.name} id: {item.id}")
    print("==================")
    # url = "https://api.box.com/2.0/folders/0/items"


    # response = requests.get(url,cl


if __name__ == "__main__":
    main()
