import datetime
from pathlib import Path

import extract_msg


def rename_msg_file(filepath):
    """Rename .msg files in the given directory using the date sent in the msg file

    Args:
        filepath: str = path to the directory containing .msg files. Needs to be absolute path.
    Returns:
        None
    """
    target_dir = Path(filepath)

    for file in target_dir.iterdir():
        if file.suffix == ".msg":

            msg = extract_msg.openMsg(file)

            date_sent = msg.date
            try:
                formatted_date = date_sent.strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Error: {e}. Defaulting to today's date")
                formatted_date = datetime.datetime.now(tz=datetime.UTC).strftime("%Y-%m-%d")

            new_name = f"{formatted_date} - {file.name}"
            new_path = target_dir / new_name

            folder_to_save_attachments = target_dir / f"{new_name} attachments"

            for attachment in msg.attachments:
                folder_to_save_attachments.mkdir(exist_ok=True)
                attachment.save(customPath=folder_to_save_attachments)
                print(f"Attachment has been saved from {file.name}")

            file.rename(new_path)
            print(f"File has been renamed to {new_name}")
