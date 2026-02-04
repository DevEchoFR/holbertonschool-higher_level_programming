#!/usr/bin/env python3
"""Defines mixins and a Dragon class."""


class SwimMixin:
    """Mixin that adds swimming behavior."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon that can swim and fly."""
    def roar(self):
        print("The dragon roars!")
