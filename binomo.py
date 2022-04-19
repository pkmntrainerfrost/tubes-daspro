# Tugas Besar IF 1210 Dasar Pemrograman

# Kelompok 06 / Kelas 07
# NIM - Nama Anggota Kelompok:
# 16521213 - Salman Ma'arif Achsien

# Program BNMO
# 

# KAMUS

# NAMA MODUL / LIBRARY

import argparse
import datetime
import math
import os
import sys
import time

from lists import *
from parser import *

games = parse("game.csv")

print(strain(games,"GAME001",False,True,0))