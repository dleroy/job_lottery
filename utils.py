import csv

def printSummaryStats(positions, students):
    '''
      Positions:  Unique position count, total available slots
      Students: Student total
    '''
    totalJobs = 0
    for key, value in positions.items():
        totalJobs += value[2]

    print("Unique positions offered: {0}\nTotal available slots: {1}".format(
        len(positions), totalJobs))
    print("Total Students: {0}\n".format(
          len(students)))
    
def printAllocationStats(positions, students):
    '''
        Students: how many got 1st, 2nd and 3rd choices, how many Not allocated
        Positions:  Company Name, seat count and allocated count
    '''
    firstChoice = 0
    secondChoice = 0
    thirdChoice = 0
    noChoice = 0
    for key, value in students.items():
        if value[4] == None:
            noChoice += 1
        elif value[4] == 0:
            firstChoice += 1
        elif value[4] == 1:
            secondChoice += 1
        else:
            thirdChoice += 1

    print("Student Choice Summary:")
    print("First Choice: {0}\nSecond Choice: {1}\nThrid Choice: {2}\nNot allocated: {3}".format(
        firstChoice, secondChoice, thirdChoice, noChoice))
    
    print("Students with no choice allocated:")
    for key, value in students.items():
        if value[4] == None:
            print("{0}, {1} ,{2}, {3}".format(
                key, 
                positions[value[0]][1] if (value[0] != None) else "",
                positions[value[1]][1] if (value[1] != None) else "",
                positions[value[2]][1] if (value[2] != None) else ""))
                      
    print("\nCompany Stats:")
    print("Company\tseats\tallocated")
    for key, value in positions.items():
        print("{0}\t{1}\t{2}".format(
            value[1], value[2], value[6]))
        
def printStudentResults(positions, students):
    ''' Output Student name, position allocated and what choice they got '''
   
    row_list = []
    for key, value in students.items():
        if value[3] != None:
            #print("{0}\t{1}\t{2}".format(key, value[3], value[4]))
            row_list.append([key, positions[value[3]][1], value[3], value[4]])
    
    header_row = ["Student Name", "Company Name", "Position ID", "Wishlist Order"]
    with open('JobShare.csv', 'w', newline = '') as csvfile:
        my_writer = csv.writer(csvfile)
        my_writer.writerow(header_row)
        my_writer.writerows(row_list)
        

        