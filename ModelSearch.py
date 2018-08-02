import numpy as np
import csv
import time
import gc


datafile = "/Users/nikitajerschow/Documents/Programming/Research-EinsteinCross/Fizz/PARTIAL.csv"

Groups = [];
GROUP_RADIUS = 0.05

Models = [];
OmittedModels=[];
MAX_SPREAD = 0.002

Interest = [];

def num_of_lines(fileName):
	with open(fileName) as f:
		for i, l in enumerate(f):
			pass
	return i+1

def openFile(fileName):
	try:
		f = open(fileName, "rb")
		return f
	except IOError:
		return -1;

num_lines = num_of_lines(datafile)

with open(datafile, "rb") as csvdata:
    
    rownumber=0
    nextidx=0
    datareader = csv.reader(csvdata)
    for row in datareader:
        #time.sleep(1)
        if (rownumber==0):
            print(row)
        elif (rownumber%65537==1):
            #for i in range(0,36):
            #    for j in range(0,36):
            #        print("DataSector "+ str(i)+"-"+str(j)+": "+str(len(data[i][j])))
            print("Parsing database file:%" +str(float(rownumber)/float(num_lines)*100.) +"\nNumber Of Groups:"+str(len(Groups)))
        elif (rownumber%1000000==1):
            print("cleaning...")
            gc.collect()
        else:
            ra = float(row[1])
            dec = float(row[2])
            z = float(row[3])
            
            if (len(Groups)==0):
            	Groups.append([])
            	Groups[nextidx].append({ "ra":ra, "dec":dec, "z":z})
            	nextidx+=1
            else:
            	added = 0
            	for group in Groups:
            		#print(group[0]["ra"],ra<group[0]["ra"]+GROUP_RADIUS, ra>group[0]["ra"]-GROUP_RADIUS , dec<group[0]["dec"]+GROUP_RADIUS , dec>group[0]["dec"]-GROUP_RADIUS)
            		#if (ra<group[0]["ra"]+GROUP_RADIUS and ra>group[0]["ra"]-GROUP_RADIUS and dec<group[0]["dec"]+GROUP_RADIUS and dec>group[0]["dec"]-GROUP_RADIUS):
            		if (ra<group[0]["ra"]+GROUP_RADIUS and ra>group[0]["ra"]-GROUP_RADIUS):
            			group.append({ "ra":ra, "dec":dec, "z":z})
            			added=1
            	if (added == 0):
            		Groups.append([])
            		Groups[nextidx].append({ "ra":ra, "dec":dec, "z":z})
            		nextidx+=1
        rownumber+=1
    print("done parsing")

for i in range(0,100):
	print("parsing model "+str(i)+"/100")
	Models.append({});
	f = openFile("Models/object_"+str(i)+"_nikitaj.csv")
	if (f==-1):
		for j in range(0,10):
			f = openFile("Models/object_"+str(i)+"_nikitaj_"+str(j)+".csv")
			if (f!=-1):
				break
	if (f==-1):
		OmittedModels.append(i);
		break
	
	rownumber = 0
	rowdata=[]
	for line in f:
		if (line==""):
			pass
		rowdata = row.split(",") #objid,ra,dec,z This is a mistake, I have not included the zErr into the models
		print(rowdata)
		try:
			ra = float(rowdata[1])
        	dec = float(rowdata[2])
        	z = float(rowdata[3])
        	if (rownumber!=0):
				Models.append([])
				Models[i].append({"ra":ra,"dec":dec,"z":z,})
		except IndexError:
			pass
	f.close()

for i in range(0,len(Models)):
	model = Models[i]

	ref=-1

	first=model[0]["z"]
	second=model[1]["z"]
	third=model[2]["z"]
	if (Math.abs(first-second)<MAX_SPREAD):
		ref=((first+second)/2)
	elif(Math.abs(second-third)<MAX_SPREAD):
		ref=(second+third)/2
	elif (Math.abs(first-third)<MAX_SPREAD):
		ref=(first+third)/2
	else:
		OmittedModels.append(i)
		break;

	for j in range(1,len(model)):

		objz = model[j]["z"]
		if (objz<(ref - MAX_SPREAD) or objz>(ref+MAX_SPREAD)):
			break;
		high = -1
		low = 10000

		if objz>high:
			high=obj["z"]
		if objz<low:
			low=obj["z"]
		
		model.insert(0,{"diff":(high-low)})

#need to compare elements in the group with models to add items to interest

for i in range(0,len(Groups)):
	Interest.append([])

for i in range(0,len(Groups)):
	group =Groups[i]
	print("starting search in group:"+i+"/"+str(len(Groups)))
	for model in Models:
		diff = model[0]['diff']
		for obj1 in group:
			for obj2 in group:
				ra1=obj1["ra"]
				ra2=obj2["ra"]
				dec1=obj1["dec"]
				dec2=obj2["dec"]
				z1=obj1["z"]
				z2=obj2["z"]
				if (Math.abs(ra1-ra2)<0.0041 and Math.abs(dec1-dec2)<0.005):
					for obj3 in group:
						ra3=obj3["ra"]
						dec3=obj3["dec"]
						z3=obj1["ra"]
						if (Math.abs(ra1-ra3)<0.0041 and Math.abs(dec1-dec3)<0.005 and Math.abs(ra3-ra2)<0.0041 and Math.abs(dec3-dec2)<0.005):
							if (Math.abs(z1-z3)>MAX_SPREAD and Math.abs(z2-z3)>MAX_SPREAD):
								Interest[i].append({"o1":obj1, "o2":obj2, "lens":obj3})

	print(Interest)

























