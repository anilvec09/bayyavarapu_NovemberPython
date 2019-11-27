import re
import os
import sys
import os
"""
This module takes an input directory as input and read through all files and perform a regex pattern serahc and tranform data accordingly
and replaces contents in the files with new modified data.
"""
filedir=input("Provide desire folder which has a lost files example C:\\Users\\sravn\\Documents\\RAND\\MPP :")

filelist=os.listdir(filedir)
for file in  filelist:

    filename=filedir+"\\"+file
    newfilename=filename+"_new.txt"

    f=open(filename,"r")
    nf=open(newfilename,"a")
    nf.write("      PID        ID       DAD       MOM       SEX    LOC_01    LOC_02    ENV_01      PHEN       AFF     z_AFF IsProband\n")

    for line in f.readlines():
        if line[6:9] != "PID":
            DAD=line[27:29]
            MOM=line[37:39]
            LOC_01=line[54:59]
            LOC_02=line[64:69]
            IsProband=line[118:119]
            if (re.search(".1/.2",LOC_01) and  re.search(".1/.2",LOC_02) or re.search(".2/.1",LOC_01) and  re.search(".2/.1",LOC_02)) and  not (re.search("-1",DAD) and re.search("-1",MOM) ):
                newline=line[:118]+"#\n"
                nf.write(newline)
            else: nf.write(line)

    nf.close()
    f.close()
    nfr=open(newfilename,"r")
    fw=open(filename,"w")

    for line in nfr.readlines():
        fw.write(line)

#clean up
    fw.close()
    nfr.close()
    os.remove(newfilename)