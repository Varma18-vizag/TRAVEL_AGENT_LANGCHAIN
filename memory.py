def get_chat_history(messages):

    history = ""

    for msg in messages:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    return history