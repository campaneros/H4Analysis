import optparse
import os


parser = optparse.OptionParser()

parser.add_option('-d', dest = 'dim',
                      help = 'specify the dimension of the matrix')
parser.add_option('-f', dest = 'inputfile', default = "cfg/ECAL_H4_July2023/ECAL_H4_Phase2_5x5.cfg",
                      help = 'input cfg file')
parser.add_option('-c', dest = 'channel', default = 70,
                      help = 'central channel')
parser.add_option('--BCP', dest = 'BCP', default=1,
		  	help = 'BCP number')
parser.add_option('-o', dest = 'ouputfile', default = 'test.txt',
		      help = 'outputfile' )
(opt, args) = parser.parse_args()




phi_bcp = [ ########### BCP 0
		10,  9,  8,  7,  6,  6,  7,  8,  9, 10, 10,  9,  8,  7,  6,  6,  7,  8,  9, 10, 10,  9,  8,  7,  6, 
             15, 14, 13, 12, 11, 11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 
             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
              5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1, 
             10,  9,  8,  7,  6,  6,  7,  8,  9, 10, 10,  9,  8,  7,  6,  6,  7,  8,  9, 10, 10,  9,  8,  7,  6, 
              5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1,
	   ######### BCP 1
             15, 14, 13, 12, 11, 11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 
              1,  2,  3,  4,  5,  5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1,  1,  2,  3,  4,  5, 
              6,  7,  8,  9, 10, 10,  9,  8,  7,  6,  6,  7,  8,  9, 10, 10,  9,  8,  7,  6,  6,  7,  8,  9, 10, 
             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
             11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 11, 12, 13, 14, 15, 
              5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1,  1,  2,  3,  4,  5,  5,  4,  3,  2,  1
]


#phi_bcp= [
#    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
#    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
#    10, 9, 8, 7, 6, 1, 2, 3, 4, 5, 
#    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
#    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
#    6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 
#    6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 
#    6, 7, 8, 9, 10, 5, 4, 3, 2, 1, 
#    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
#    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
#    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
#    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
#    10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
#    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
#    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
#    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
#    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
#    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
#    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
#    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
#    5, 4, 3, 2, 1
#]

eta_bcp = [ ###### BCP 0
             55, 55, 55, 55, 55, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53, 52, 52, 52, 52, 52, 51, 51, 51, 51, 51, 
             50, 50, 50, 50, 50, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 47, 47, 47, 47, 47, 46, 46, 46, 46, 46, 
             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
             50, 50, 50, 50, 50, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 47, 47, 47, 47, 47, 46, 46, 46, 46, 46, 
             50, 50, 50, 50, 50, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 47, 47, 47, 47, 47, 46, 46, 46, 46, 46, 
             55, 55, 55, 55, 55, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53, 52, 52, 52, 52, 52, 51, 51, 51, 51, 51, 
	  ##### BCP 1
	     55, 55, 55, 55, 55, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53, 52, 52, 52, 52, 52, 51, 51, 51, 51, 51, 
             56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 
             56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 
             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
             56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 
             90, 90, 90, 90, 90, 89, 89, 89, 89, 89, 88, 88, 88, 88, 88, 87, 87, 87, 87, 87, 86, 86, 86, 86, 86, 
	] 



#eta_bcp = [     55, 55, 55, 55, 55, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53,
#        52, 52, 52, 52, 52, 51, 51, 51, 51, 51, 56, 56, 56, 56, 56,
#        57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59,
#        60, 60, 60, 60, 60, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57,
#        58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60,
#        50, 50, 50, 50, 50, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48,
#        47, 47, 47, 47, 47, 46, 46, 46, 46, 46, 50, 50, 50, 50, 50,
#        49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 47, 47, 47, 47, 47,
#        46, 46, 46, 46, 46, 55, 55, 55, 55, 55, 54, 54, 54, 54, 54,
#        53, 53, 53, 53, 53, 52, 52, 52, 52, 52, 51, 51, 51, 51, 51,
#        61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63,
#        64, 64, 64, 64, 64, 65, 65 ,65, 65, 65, 61, 61, 61, 61, 61,
#        62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64,
#        65, 65, 65, 65, 65, 90, 90, 90, 90, 90, 89, 89, 89, 89, 89,
#        88, 88, 88, 88, 88, 87, 87, 87, 87, 87, 86, 86, 86, 86, 86
#]

if int(opt.BCP) == 1:
	bcp_num = 0
elif int(opt.BCP) == 2:
	bcp_num = 1
else:
	print("bad bcp number inserted")
	exit(1)

central_channel = int(opt.channel)+bcp_num*150
matrix = (int(opt.dim)-1)/2
dimension = int(opt.dim)
input_file=opt.inputfile

out_file = "test.txt"
os.system("cp "+input_file+" "+out_file)
combined_phi_eta = zip(phi_bcp,eta_bcp)

phi_central,eta_central = combined_phi_eta[central_channel]
print(combined_phi_eta[int(opt.channel)], phi_central,eta_central)

if (eta_central<0) or (phi_central<0):
	print("ERROR CENTRAL CHANNEL NOT ACTIVE")
	exit(1)

first_eta = eta_central - matrix
first_phi = phi_central + matrix 

#print(first_phi)
#pair =(first_phi,first_eta)

if dimension == 5:
	letters = ['A', 'B', 'C', 'D', 'E']
	flag = [1,1,1,1,1]

elif dimension == 7:
	letters = ['A', 'B', 'C', 'D', 'E', 'F','G']
	flag =    [1, 1, 1, 1, 1, 1, 1]

elif dimension == 3:
	letters = ['A', 'B', 'C']
	flag = [1,1,1]



for i in range(dimension*dimension):
	letter = letters[i // dimension]
	number = (i% dimension)+1				
	curr_eta = first_eta + i% dimension		
	curr_phi = first_phi - (i // dimension)
	print(curr_eta,curr_phi)
	curr_pair = (curr_phi,curr_eta)
	try:
		curr_index = combined_phi_eta.index(curr_pair)
	except:
		print("REMOVE CHANNEL NOT EXISTING IN CFG FILE, THEY HAVE NEGATIVE NUMBERS")
		curr_index = -1	
	if curr_index == -1:
		bcp_number = -1
		flag[i% dimension]=0
	elif  curr_index<150:
		bcp_number = 0
	else:
		bcp_number = 1 
	command = "sed -i 's/##digiboard{0}{1}##/{2}/g; s/##digiChannel{0}{1}##/{3}/g' {4}".format(letter,number,bcp_number,curr_index,out_file)	
	os.system(command)
	if curr_index>=0:
		#print("EUREKA")
			#command = "sed -i 's/#Valid{0}{1}#//g; s/#matrix{0}{1}#/{0}{1}/g; s/\\\\/test/g' {2}".format(letter,number,out_file)
		command = "sed -i 's/#Valid{0}{1}#//g; s/#matrix{0}{1}#/{0}{1}/g' {2}".format(letter,number,out_file)
	else:
		command = "sed -i 's/#Valid{0}{1}#/###/g; s/#matrix{0}{1}#//g' {2}".format(letter,number,out_file)
	os.system(command)
	if (number == dimension):
		#print(flag, letter)
		if letter!='A':
			letter = letters[i // dimension-1]
			if 1 in flag:
				command = "sed -i 's/#end{0}#/\\\\/g' {1}".format(letter,out_file)
			else:
				command = "sed -i 's/#end{0}#/ /g' {1}".format(letter,out_file)
		os.system(command)
		for x in flag:
			x=1
