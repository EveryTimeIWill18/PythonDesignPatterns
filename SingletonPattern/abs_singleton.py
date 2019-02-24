"""
Abstract Singleton
------------------
Abstract singleton design pattern.
"""
import abc

class AbsSingleton(metaclass=abc.ABCMeta):
    """Abstract Base Class"""

    @abc.abstractmethod
    def __new__(cls, **kwargs):
        """required"""
        pass
