import optparse
import os


parser = optparse.OptionParser()

parser.add_option('-d', dest = 'dim',
                      help = 'specify the dimension of the matrix')
parser.add_option('-f', dest = 'inputfile',
                      help = 'input cfg file')
parser.add_option('-c', dest = 'channel',
                      help = 'central channel')
(opt, args) = parser.parse_args()

phi_bcp= [
    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
    10, 9, 8, 7, 6, 1, 2, 3, 4, 5, 
    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
    6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 
    6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 
    6, 7, 8, 9, 10, 5, 4, 3, 2, 1, 
    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
    1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
    10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 
    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
    5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 
    5, 4, 3, 2, 1
]

eta_bcp = [     55, 55, 55, 55, 55, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53,
        52, 52, 52, 52, 52, 51, 51, 51, 51, 51, 56, 56, 56, 56, 56,
        57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59,
        60, 60, 60, 60, 60, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57,
        58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60,
        50, 50, 50, 50, 50, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48,
        47, 47, 47, 47, 47, 46, 46, 46, 46, 46, 50, 50, 50, 50, 50,
        49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 47, 47, 47, 47, 47,
        46, 46, 46, 46, 46, 55, 55, 55, 55, 55, 54, 54, 54, 54, 54,
        53, 53, 53, 53, 53, 52, 52, 52, 52, 52, 51, 51, 51, 51, 51,
        61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63,
        64, 64, 64, 64, 64, 65, 65 ,65, 65, 65, 61, 61, 61, 61, 61,
        62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64,
        65, 65, 65, 65, 65, 90, 90, 90, 90, 90, 89, 89, 89, 89, 89,
        88, 88, 88, 88, 88, 87, 87, 87, 87, 87, 86, 86, 86, 86, 86
]


central_channel = int(opt.channel)
matrix = (int(opt.dim)-1)/2
dimension = int(opt.dim)
input_file=opt.inputfile

out_file = "test.txt"
os.system("cp "+input_file+" "+out_file)
combined_phi_eta = zip(phi_bcp,eta_bcp)

phi_central,eta_central = combined_phi_eta[central_channel]
print(combined_phi_eta[int(opt.channel)], phi_central,eta_central)

first_eta = eta_central - matrix
first_phi = phi_central + matrix 

print(first_phi)
pair =(first_phi,first_eta)
first_index = combined_phi_eta.index(pair)
print(first_index)

letters = ['A', 'B', 'C', 'D', 'E']



for i in range(dimension*dimension):
	letter = letters[i // dimension]
	number = (i% dimension)+1				
	curr_eta = first_eta + i% dimension		
	print(curr_eta)
	curr_phi = first_phi - (i // dimension)
	curr_pair = (curr_phi,curr_eta)
	curr_index = combined_phi_eta.index(curr_pair) 
	command = "sed -i 's/##digiboard{0}{1}##/{2}/g; s/##digiChannel{0}{1}##/{3}/g' {4}".format(letter,number,1,curr_index,out_file)	
	os.system(command)


