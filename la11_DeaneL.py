
'''CSCI 161L

LA11

Lucy Deane'''
def main():

    while True:
        flag = 0
        print('1: Search an employee using SSN number')
        print('2: Display the employee details based on sorted Employee IDs')
        print('3: Exit')
        userInput = int(input('Enter an option: '))
        if userInput == 1:
            userSSN = str(input('Enter your 9 digit SSN: '))
            f = open('Employee_SSN.txt', 'r')
            for line in f:
                ssn = line[6:17]
                iD = line[0:4]
                if ssn == userSSN:
                    flag = flag + 1
                    user_ID = iD
            if flag == 0:
                print('SSN not found in file')
            else:
                x = open('Employee_Details.txt', 'r')
                for line in x:
                    num = line[0:4]
                    if num == user_ID:
                        print('SSN match found')
                        print('The employee details are: ')
                        print(line)
        if userInput == 3:
            conf = int(input('Are you sure you would like to exit the program? 1 for yes, 0 for no. '))
            if conf == 1:
                quit()
            else:
                True
        if userInput == 2:
            f = open('Employee_Details.txt', 'r')
            iD_list = []
            det_list = []
            for line in f:
                iD = line[0:4]
                iD_list.append(iD)
                det_list.append(line)
            
            new_list = []
            while iD_list:
                minimum = iD_list[0]  
                for x in iD_list: 
                    if x < minimum:
                        minimum = x
                new_list.append(minimum)
                iD_list.remove(minimum)                  
            for i in new_list:
                for x in det_list:
                    if i == x[0:4]:
                        print(x)
                        print()
                    
            
main()



