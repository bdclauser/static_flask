#!/usr/bin/env python
"""Creat a new admin user able to view the /reports endpoint."""
from getpass import getpass
import sys

from flask import current_app
from bull import app, bcrypt
from bull.models import User, db