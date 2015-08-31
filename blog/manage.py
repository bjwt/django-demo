#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    for arg in sys.argv:
        print arg
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
