"""
File Name: tester.py
Author: Elliot V Pourmand
Date: 03/05/2018
Description: Use pytest framework to test functionality of ticketviewer.py
"""
from ticketviewer import get_tickets, creds
from zenpy import Zenpy
from zenpy.lib.exception import APIException
import sys
from zenpy.lib.api_objects import Ticket


def test_get_tickets_return():
    """
    Test get_tickets() using pytest framework
    :return: void
    """
    try:
        zenpy_client = Zenpy(**creds)
        tickets = get_tickets(zenpy_client)
    except APIException:
        print("Error connecting to API")
        sys.exit(1)
    # Verify list was returned
    assert tickets is not None


def test_get_tickets_type():
    """
    Test get_tickets() using pytest framework
    :return: void
    """
    try:
        zenpy_client = Zenpy(**creds)
        tickets = get_tickets(zenpy_client)
    except APIException:
        print("Error connecting to API")
        sys.exit(1)
    # Verify type
    if len(tickets) > 0:
        assert isinstance(tickets[0], Ticket)

