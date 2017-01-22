"""Utilites for opening editors"""
import subprocess

class SublimeEditor:
    two_column_command = 'set_layout {"cols": [0, 0.5, 1], "rows": [0, 1], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]}'

    @classmethod
    def _call(cls, *args):
        subprocess.call(['subl'] + list(args))

    @classmethod
    def simple_open(cls, *paths):
        cls._call('-n', *paths)

    @classmethod
    def compare(cls, path1, path2):
        cls._call('-n', '--command', cls.two_column_command, path1, path2)

class IdeaEditor:
    @classmethod
    def _call(cls, *args):
        subprocess.call(['idea'] + list(args))

    @classmethod
    def simple_open(cls, *paths):
        for path in paths:
            cls._call('--temp-project', path)

    @classmethod
    def compare(cls, path1, path2):
        cls._call('diff', path1, path2)

DefaultEditor = SublimeEditor