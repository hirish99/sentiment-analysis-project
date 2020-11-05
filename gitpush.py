import os
import sys

os.system("git add *")
os.system("git status")
os.system('git commit -m'+str(sys.argv[1]))
os.system("git push")
