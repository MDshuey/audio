mypath = 'D:/ROLAND/WAVE'
mydest = 'C:/Users/Mitch/OneDrive/crow/RC-202'
#-------------------------
# BOSS/Roland stores the recordings on the RC-202 as 8 memory slots, each with 8 banks.
# Each bank has 2 recording slots, for a total possible 128 recordings.
# On the machine, each recording has its own folder with a number 1-64 for each bank.
# This leads to a hard time finding and managing your recordings as you create them.
# This code copies the files directly and translates the file name to the memory-bank form.
# (We're kind of converting decimal #s to octal (base-8 + 1), which is neat.)
#--------------------------

import glob
import re
import math
import shutil

#create list of .wav files

wavlist = glob.glob(mydest + "/*/*.wav")

for filepath in wavlist:

  #extract the numbers from the filename
  loop = re.split('_', os.path.basename(filepath))
  num = int(loop[0])

  #Number conversion
  ## First digit: Divide by 8 and round up
  memory = str(math.ceil(num/8))

  ## Second Digit: Modulo (and account for 0)
  if num % 8 == 0:
    bank = '8'
  else: 
    bank = str(num % 8)
 
  #Finally, copying the file to destination path.
  destpath = mydest + '/' + memory + '-' + bank + '_' + loop[1]

  if os.path.exists(destpath):
      print(destpath + "Transfer failed: destination path exists. Review/rename existing recordings.")
  else:
    shutil.copy2(filepath, destpath)
