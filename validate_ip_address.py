def input_filename(filename):
    try:
        file = open(filename, 'r')
        data = list()
        for line in file:
            line = line.strip('\n')
            line_list = line.split(' ')
            start_ip = line_list[0].split('.')
            end_ip = line_list[1].split('.')
            test_ip = line_list[2].split('.')
            ip_data = list((start_ip,end_ip,test_ip))
            data.append(ip_data)
    except FileNotFoundError:
        print('** File not found**\n')
    return data
        

def truth_ip(data):
    data_truth=list()
    ip_set_truth=list()
    n=0
    for ip_set in data:
        for ip in ip_set:
            n+=1
            data_check=''
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
        if data_truth==[['t'],['t'],['t']]:
            data_truth='t'
        else:
            data_truth='f'
        ip_set_truth.append(data_truth)
        data_truth=list()
    return ip_set_truth

def identify_ip(data,truth):
    for x in range(0,len(data)):
        low_end=0
        high_end=0
        if truth[x]=='f':
            print('InValid')
            low_end=4
        else:
            for n in range(0,3):
                if data[x][0][n]>data[x][2][n] and low_end!=1:
                    low_end=2
                elif data[x][0][n]<data[x][2][n] and low_end!=2:
                    low_end=1
                if data[x][2][n]>data[x][1][n]and high_end!=1:
                    high_end=2
                elif data[x][2][n]<data[x][1][n] and high_end!=2:
                    high_end=1
        if low_end<2 and high_end<2:
            print('InRange')
        elif low_end!=4:
            print('OutRange')

file = input("What is the filename?")
data = input_filename(file)
truth = truth_ip(data)
identify_ip(data,truth)
