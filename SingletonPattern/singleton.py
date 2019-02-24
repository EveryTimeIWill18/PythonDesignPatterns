"""
Singleton
---------
"""
from abs_singleton import AbsSingleton

class Singleton(AbsSingleton):
    """Singleton Design Pattern"""
    _instance = None

    def __new__(cls, **kwargs):
        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls)
            for k in list(kwargs.keys()):
                Singleton._instance.kwargs.get(k)
        return Singleton._instance
