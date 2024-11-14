from typing import Generator, Iterator, List


# This is a bad example
class Client:
    active: bool


def email(clients: Client) -> None:
    pass


def email_clients_bad(clients: List[Client]) -> None:
    for client in clients:
        if client.active:
            email(client)


# This is a good example


def get_active_clients(clients: List[Client]) -> List[Client]:
    return [client for client in clients if client.active]


def email_clients_good(clients: List[Client]) -> None:
    for client in get_active_clients(clients):
        email(client)


# This is better


def active_clients(clients: Iterator[Client]) -> Generator[Client, None, None]:
    return (client for client in clients if client.active)


def email_client(clients: Iterator[Client]) -> None:
    for client in active_clients(clients):
        email(client)
