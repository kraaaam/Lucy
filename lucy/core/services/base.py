import abc


class BaseChannel(abc.ABC):
    @abc.abstractmethod
    def send_message(self, message: str):
        raise NotImplementedError
