########################################################################################################################
##  VALIDATE IP ADDRESSES       by: Cameron Gibson
##
## Originally used with a test file with a specific format:
##      -each line of the file contains three ip addresses (###.###.###.###)
##      -each ip address was separated from the next by a space
##      -the first ip address was the start_ip, the second was the end_ip, and the third was the test_ip
##
## This program tests if the ip addresses are valid ip addresses and then test if the test_ip is in range of the
## start_ip and end_ip.
##
########################################################################################################################


#this FUNCTION takes in an input fileaname and tries to open the file
#once the file is opened, it takes the contents of the file and reates a list of the ip addresses (in groups of three)
#if the file cannot be opened then tell the user
#RETURNS: the list of ip addresses
def input_filename(filename):
    
    try:
        file = open(filename, 'r')
        data = list()
        
        #splits the contents and organizes it into lists (grouped by 3)
        for line in file:
            line = line.strip('\n')
            line_list = line.split(' ')
            #file must have "start_ip end_ip test_ip" on each line
            start_ip = line_list[0].split('.')
            end_ip = line_list[1].split('.')
            test_ip = line_list[2].split('.')
            ip_data = list((start_ip,end_ip,test_ip))
            data.append(ip_data)
            
    #handle the exception if the file cannot be opened
    except FileNotFoundError:
        print('** File not found**\n')
        
    return data

########################################################################################################################    
    
#this FUNCTION tests if each ip address is valid in the list, which has been created from the input file
#RETURNS: a list of truth values (t or f) for each set of three ip addresses
def truth_ip(data):
    #initializing
    data_truth=list()
    ip_set_truth=list()
    n=0
    
    #for each list of three ip addresses in the data list
    for ip_set in data:
        #for each ip address in the list of three
        for ip in ip_set:
            n+=1
            data_check=''
            #for each number in the ip address
            for num in ip:
                try:
                    if 0>int(num)>255:
                        data_check+='f'
                    else:
                        data_check+='t' 
                except ValueError:
                    data_check+='f'
            if data_check=='tttt':
                data_check=list('t')
            else:
                data_check=list('f')
            
            data_truth.append(data_check)
            
        #if every ip in the set of three is valid, then the set is a valid set
        #records the truth values in the data_truth list
        if data_truth==[['t'],['t'],['t']]:
            data_truth='t'
        else:
            data_truth='f'
    
        ip_set_truth.append(data_truth)
        data_truth=list()
        
    return ip_set_truth

########################################################################################################################

#this FUNCTION takes in the list of ip addresses and the list of truth values for each set of three ip addresses
def identify_ip(data,truth):
    
    #for every set of three ip addresses
    for x in range(0,len(data)):
        #initialize to 0
        low_end=0
        high_end=0
        
        #check if the list of three ip addresses contains all valid ip addresses
        if truth[x]=='f':
            print('InValid')
            low_end=4
        else:
            #for each number in the ip address, check if the test_ip is in range of the start_ip and end_ip
            #(between the first two ip addresses)
            for n in range(0,3):
                if data[x][0][n]>data[x][2][n] and low_end!=1:
                    low_end=2
                elif data[x][0][n]<data[x][2][n] and low_end!=2:
                    low_end=1
                if data[x][2][n]>data[x][1][n]and high_end!=1:
                    high_end=2
                elif data[x][2][n]<data[x][1][n] and high_end!=2:
                    high_end=1
                    
        #PRINTS the result (either InRange or OutRange) 
        if low_end<2 and high_end<2:
            print('InRange')
        elif low_end!=4:
            print('OutRange')

#######################################################################################################################  
   
#MAIN part of the file: asks the user for a filename, calls the functions in order to print out the result for
#each of the sets of ip addresses in the file
file = input("What is the filename?")
data = input_filename(file)
truth = truth_ip(data)
identify_ip(data,truth)
