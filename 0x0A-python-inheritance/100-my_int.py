#!/usr/bin/python3
"""Inherits from int and modifies some methods"""


class MyInt(int):
    """Inherits from int and operators == and != are inverted"""
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        """Redefine '==' to mean '!=' """
        if self.a != other:
            return True
        else:
            return False

    def __ne__(self, other):
        """Redefine '!=' to mean '==' """
        if self.a == other:
            return True
        else:
            return False
