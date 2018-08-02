#Research - Einstein Cross
import numpy as np
import csv
import time
import gc

REDSHIFT_PERCENTAGE = 50


def storedata(filename, criterion):
    print('getstuff')
    with open("/Users/nikitajerschow/Documents/Programming/Research-EinsteinCross/Fizz/ENTIRE_nikitaj.fits", "rb") as csvdata:
        
        rownumber=0
        datareader = csv.reader(csvdata)
        for row in datareader:
            #print(row)
            #time.sleep(1)
            if (rownumber==0):
                print(row)
            elif (rownumber%655370==1):
                #for i in range(0,36):
                #    for j in range(0,36):
                #        print("DataSector "+ str(i)+"-"+str(j)+": "+str(len(data[i][j])))
                print("Percent Done:" +str(float(rownumber)/float(num_lines)*100.))
            elif (rownumber%576421==1):
                print("cleaning...")
                gc.collect()
            else:
                ra = float(row[1])
                dec = float(row[2])
                z = float(row[3])
                zErr = float(row[4])
                if (ra>339.7 and ra <340.3):
                    if (dec>3.0 and dec<3.6):
                    	print("ObjID:" +str(row[0])+"\t RA:"+ str(ra)+ "\t Dec:"+str(dec)+"\t z:"+str(z)+"\t zErr:"+str(zErr))
                        Interest.append(row)
                added=0
                
                ira = int(ra)
                idec = int(dec)
                
                #data[ira/10][idec/10].append(row)
                added=1
                if(added==0):
                    print("row not added to any sector:"+str(rownumber)+" ObjID:"+row[0]+" RA:"+row[1]+" DEC:"+row[2])
            rownumber+=1
        print("done")
        # for i in range(0,36):
        #     for j in range(0,36):
        #         if(len(data[i][j])!=0):
        #             print("DataSector "+ str(i)+"-"+str(j)+": "+str(len(data[i][j])))
                      
        
            
            
        return
    #    datareader = csv.reader(csvfile)
    #    count = 0
    #    print('datareader: ' + datareader)
    #    for row in datareader:
    #        print('row: '+ row)
    #        if row[3] in ("column header", criterion):
    #            yield row
    #            count += 1
    #        elif count < 2:
    #            continue
    #        else:
    #            return
                
print("hello")
storedata("ec.csv", 'dec')
print('done')
time.sleep(3)
print("values of interest ...:")
time.sleep(3)
for i in range(0,len(Interest)): #340.126250101, 3.35861111111
	print("\tObjID:"+str(Interest[i][0])+"\tra:"+str(Interest[i][1])+"\tdec:"+str(Interest[i][2])+"\tz:"+str(Interest[i][3])+"zErr:"+str(Interest[i][4]))




