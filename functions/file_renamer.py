from datetime import datetime
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
            file_name = file.name
            msg = extract_msg.openMsg(file)

            date_sent = msg.date
            try:
                formatted_date = date_sent.strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Error: {e}. Defaulting to None")
                formatted_date = None

            if formatted_date:
                new_path = target_dir / f"{formatted_date} - {file_name}"
                file.rename(new_path)
