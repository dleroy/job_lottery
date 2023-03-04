import csv
from constants import *

def printSummaryStats(positions, students):
    '''
      Positions:  Unique position count, total available slots
      Students: Student total
    '''
    totalJobs = 0
    for key, value in positions.items():
        totalJobs += value[SLOTSAVAIL]

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
        if value[RANKRCVD] == None:
            noChoice += 1
        elif value[RANKRCVD] == 0:
            firstChoice += 1
        elif value[RANKRCVD] == 1:
            secondChoice += 1
        else:
            thirdChoice += 1

    print("Student Choice Summary:")
    print("First Choice: {0}\nSecond Choice: {1}\nThird Choice: {2}\nNot allocated: {3}".format(
        firstChoice, secondChoice, thirdChoice, noChoice))
    
    print("Students with no choice allocated:")
    for key, value in students.items():
        if value[RANKRCVD] == None:
            print("{0}, {1} ,{2}, {3}".format(
                key, 
                positions[value[WISHLIST0]][COMPANY] if (value[WISHLIST0] != None) else "",
                positions[value[WISHLIST1]][COMPANY] if (value[WISHLIST1] != None) else "",
                positions[value[WISHLIST2]][COMPANY] if (value[WISHLIST2] != None) else ""))
                      
    print("\nCompany Stats:")
    print("Company\tseats\tallocated")
    for key, value in positions.items():
        print("{0}\t{1}\t{2}".format(
            value[COMPANY], value[SLOTSAVAIL], value[ALLOCCOUNT]))
        
def printStudentResults(positions, students):
    ''' Output Student name, position allocated and what choice they got '''
   
    row_list = []
    for key, value in students.items():
        if value[ASSIGNED] != None:
        # XXX Add not assigned as well?
            row_list.append([key, value[EMAIL], positions[value[ASSIGNED]][COMPANY], value[ASSIGNED], value[RANKRCVD]])
    
    header_row = ["Student Name", "Student Email", "Company Name", "Position ID", "Wishlist Order"]
    with open('JobShare.csv', 'w', newline = '') as csvfile:
        my_writer = csv.writer(csvfile)
        my_writer.writerow(header_row)
        my_writer.writerows(row_list)
        

def printAllocationStats2(positions, students):
    ''' Look at correlation between number of slots available in choices made vs. what spot they received
        Output:
            1st choice:  num, min, mean, max slots available
            2nd choice: ...
            3rd choice: ...
            not allocated: ...
    '''
    results = {
        0: [0,1000,0,0],
        1: [0,1000,0,0],
        2: [0,1000,0,0],
        3: [0,1000,0,0]
    }
    firstChoice = 0
    secondChoice = 0
    thirdChoice = 0
    noChoice = 0
    for key, value in students.items():
        slots =  positions[value[WISHLIST0]][SLOTSAVAIL] if (value[WISHLIST0] != None) else 0
        slots += positions[value[WISHLIST1]][SLOTSAVAIL] if (value[WISHLIST1] != None) else 0
        slots += positions[value[WISHLIST2]][SLOTSAVAIL] if (value[WISHLIST2] != None) else 0
        if value[RANKRCVD] == None:
            noChoice += 1
            results[3][0] += 1
            results[3][2] += slots;
            if results[3][1] > slots:
                results[3][1] = slots;
            if results[3][3] < slots:
                results[3][3] = slots;
        elif value[RANKRCVD] == 0:
            firstChoice += 1
            results[0][0] += 1
            results[0][2] += slots;
            if results[0][1] > slots:
                results[0][1] = slots;
            if results[0][3] < slots:
                results[0][3] = slots;
        elif value[RANKRCVD] == 1:
            secondChoice += 1
            results[1][0] += 1
            results[1][2] += slots;
            if results[1][1] > slots:
                results[1][1] = slots;
            if results[1][3] < slots:
                results[1][3] = slots;
        else:
            thirdChoice += 1
            results[2][0] += 1
            results[2][2] += slots;
            if results[2][1] > slots:
                results[2][1] = slots;
            if results[2][3] < slots:
                results[2][3] = slots;

    for i in range(0, 4):
        results[i][2] = results[i][2]/results[i][0]
    print(results);

# one time code to read in a final assignments csv and insert the correct email addresses next to student names
# Now that happens automatically in the lottery output.
# XXX Can delete when sure not needed again
#assignments= pd.read_csv("./final-assignments.csv")
#assignments = assignments.reset_index()  # make sure indexes pair with number of rows

#row_list = []
#for index, row in assignments.iterrows():
#    row_list.append([row["Name"],
#                     StudentDict[row["Name"]][5],
#                     row["Company Name"],
#                     row["Position ID"],
#                     row["Wishlist Order"]])
    
#    header_row = ["Name", "Email Address" "Company Name", "Position ID", "Wishlist Order"]
#    with open('final.csv', 'w', newline = '') as csvfile:
#        my_writer = csv.writer(csvfile)
#        my_writer.writerow(header_row)
#        my_writer.writerows(row_list)       