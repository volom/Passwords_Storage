#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:22:12 2021

@author: volodymyr
"""

from cryptography.fernet import Fernet
import base64
import os

def decrypt_db(init_key):
    db_path = f"{os.getcwd()}//db_repo//password_db.db"
    key = bytes(str(init_key*31)[:31], 'utf8')
    key = base64.urlsafe_b64encode(key)
    key = bytes(init_key[0]+str(key)[2:-2], 'utf8')

    # Decrypt
    f = Fernet(key)

    with open(db_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(db_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted) 
