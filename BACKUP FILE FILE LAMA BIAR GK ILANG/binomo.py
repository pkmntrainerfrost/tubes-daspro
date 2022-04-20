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

from F11 import *
from F15 import *
from F16 import *

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder",type=str)
args = parser.parse_args()

nama_folder = args.nama_folder

(data_user,data_game,data_riwaya,data_kepemilikan) = load(nama_folder)