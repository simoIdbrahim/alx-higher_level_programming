#!/usr/bin/python3
"""defines cls MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior."""
        return self.real == valu
