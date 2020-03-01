from smtplib import SMTPException

import pytest
import allure

from gmail import GMail
from gmail.message import Message

# def test_messages_dispatch(credentials):
#     login, password, sender, recepient, subject = credentials.split()
#     client = Gmail()
#     print(login, password)
#     with allure.step("signing in"):
#         client.login(login, password)
#     with allure.step("sending message"):
#         response = client.send(sender, recepient, subject, plain="msg.txt")
#     assert response == 2
#     print(response)
#     with allure.step("logging out"):
#         client.logout()

class TestInputException: pass


def test_message_dispatch(username, password, to, body, subject):
    # username regex

    with allure.step("Check password"):
        if password is None:
            raise TestInputException("Password required")
        # regex
    
    with allure.step("Check body"):
        if body is None:
            raise TestInputException("Message text required")
    
    gmail = GMail(username=username, password=password)
    to = to.split(",")
    with allure.step("Check target mailbox"):
        # regex mailbox
        pass
    msg = Message(subject=subject,
                  to=",".join(to),
                  text=body)
    try:
        with allure.step("Sending message"):
            gmail.send(msg)
    except SMTPException:
        raise AssertionError
    with allure.step("Close connection with gmail"):
        gmail.close()
