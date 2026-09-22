from pathlib import Path
from datetime import datetime
import extract_msg


def rename_msg_file(filepath):
    target_dir = Path(filepath)
    abs_path = target_dir.absolute()

    for file in abs_path.iterdir():
        if file.suffix == ".msg":
            file_name = file.name
            msg = extract_msg.openMsg(file)

            date_sent = msg.date
            try:
                formatted_date = date_sent.strftime("%Y-%m-%d")
            except Exception as e:
                formatted_date = None
            print(type(date_sent))
            print(formatted_date)
