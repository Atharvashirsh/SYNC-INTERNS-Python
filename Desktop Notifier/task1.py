from plyer import notification


if __name__ == "__main__":
    print("Hello World")

    heading = "THIS IS NOTIFICATION TITLE"
    text = "This is a message"

    notification.notify(
        title=heading,
        message=text,
        app_icon=None,
        timeout=10,
        toast=False
    )
