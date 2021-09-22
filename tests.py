#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 9
day = 24

def test_code():
    assert main.product3Plus1(2,2,2) == 9, "product3Plus1(2, 2, 2) == 9 failed"
    assert main.product3Plus1(3,4,5) == 61, "product3Plus1(3, 4, 5) == 61 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
