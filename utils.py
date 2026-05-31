from datetime import datetime

def convert_time(time_string):

    dt = datetime.fromisoformat(
        time_string
    )

    return dt.hour * 100 + dt.minute