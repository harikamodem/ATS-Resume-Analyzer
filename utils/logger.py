from datetime import datetime

def log_event(
    message
):

    with open(
        "logs/events.txt",
        "a"
    ) as f:

        f.write(
            f"{datetime.now()} : {message}\n"
        )