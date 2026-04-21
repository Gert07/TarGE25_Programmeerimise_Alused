"""Client"""
import csv
from typing import Optional
from Clients import *


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            clients += [Client(row[0], row[1], int(row[2]), int(row[3]), int(row[4]))]
    return clients


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    clients = read_from_file_into_list(filename)
    return [c for c in clients if c.bank == bank]


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    clients = read_from_file_into_list(filename)
    max_earnings_per_day = max(c.earnings_per_day() for c in clients)
    max_client = []
    if max_earnings_per_day <= 0:
        return None
    for c in clients:
        if c.earnings_per_day() == max_earnings_per_day and max_earnings_per_day > 0:
            max_client.append(c)
    return sorted(max_client, key=lambda c: c.account_age)[0]


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    client_list = read_from_file_into_list(filename)
    max_losses_per_day = min(c.earnings_per_day() for c in client_list)
    min_client = []
    if max_losses_per_day >= 0:
        return None
    for c in client_list:
        if c.earnings_per_day() == max_losses_per_day and max_losses_per_day < 0:
            min_client.append(c)
    return sorted(min_client, key=lambda c: c.account_age)[0]