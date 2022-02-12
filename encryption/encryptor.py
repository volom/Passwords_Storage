#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:51:34 2021

@author: volom
"""

from cryptography.fernet import Fernet
import base64
import os

def encrypt_db(init_key):
    db_path = f"{os.getcwd()}//db_repo//password_db.db"

    key = bytes(str(init_key*31)[:31], 'utf8')
    key = base64.urlsafe_b64encode(key)
    key = bytes(init_key[0]+str(key)[2:-2], 'utf8')
    f = Fernet(key)

    # Encrypt
    with open(db_path, 'rb') as original_file:
        original = original_file.read()
        encrypted = f.encrypt(original)
    with open (db_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
