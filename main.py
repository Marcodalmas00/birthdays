#! /usr/bin/env python3
from bdpackage.bdmodule import return_birthday
import sys

print(sys.argv[1]+" "+sys.argv[2])
return_birthday(sys.argv[1]+" "+sys.argv[2])
