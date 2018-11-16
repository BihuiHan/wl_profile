import sys
import os


def main(ignored_parameter):
    # Pull Die Level Data in Server
    # os.system('prbext -bin=dR -trend=\'^COMP_UP_RES_PRE_PCT_GWL.*\' b27b -0.5 qbpp +csv > test.csv')
    with open('test.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
    # Transfer non-zero data to one(CNT)
    # Add Overall CNT by WL
    # Plot Profile by REG

    return



if __name__ == "__main__":
    main(*sys.argv)
    # IgnoredParameter,FileName

