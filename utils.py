''' Utility functions for the Job Share Lottery '''
import csv
from constants import COMPANY, SLOTSAVAIL, ALLOCCOUNT, RANKRCVD, WISHLIST0, WISHLIST1, WISHLIST2, EMAIL, GRADE


def print_summary_stats(positions, students):
    '''
      Positions:  Unique position count, total available slots
      Students: Student total
    '''
    total_jobs = 0
    for key, value in positions.items():
        total_jobs += value[SLOTSAVAIL]

    print(
        f'Unique positions offered: {len(positions)}\nTotal available slots: {totalJobs}')
    print(f'Total students: {len(students)}')


def print_allocation_stats(positions, students, grades):
    '''
        Students: how many got 1st, 2nd and 3rd choices, how many Not allocated
        Positions:  Company Name, seat count and allocated count
    '''
    first_choice = 0
    second_choice = 0
    third_choice = 0
    no_choice = 0
    student_grade = {"Freshman": 0, "Sophmore": 0, "Junior": 0, "Senior": 0}
    for key, value in students.items():
        if (value[GRADE] in grades):
            student_grade[value[GRADE]] += 1
            if value[RANKRCVD] is None:
                no_choice += 1
            elif value[RANKRCVD] == 0:
                first_choice += 1
            elif value[RANKRCVD] == 1:
                second_choice += 1
            else:
                third_choice += 1
        else:
            print(f'Grade {value[GRADE]} not in grades list: {grades}')

    print("Student Choice Summary:")

    print("\nGrades Considered in Lottery:")
    print(student_grade)
    [print(i) for i in grades]
    print(
        f'First Choice: {first_choice}\nSecond Choice: {second_choice}\nThird Choice: {third_choice}\nNot allocated: {no_choice}')

    return

    # print("Students with no choice allocated:")
    # for key, value in students.items():
    #    if value[RANKRCVD] is None:
    #        print("{0}, {1} ,{2}, {3}".format(
    #            key,
    #            positions[value[WISHLIST0]][COMPANY] if (
    #                value[WISHLIST0] != None) else "",
    #            positions[value[WISHLIST1]][COMPANY] if (
    #                value[WISHLIST1] != None) else "",
    #            positions[value[WISHLIST2]][COMPANY] if (value[WISHLIST2] != None) else ""))

    # print("\nCompany Stats:")
    # print("Company\tseats\tallocated")
    # for key, value in positions.items():
    #    print("{0}\t{1}\t{2}".format(
    #        value[COMPANY], value[SLOTSAVAIL], value[ALLOCCOUNT]))


def write_student_results(positions, students, grades):
    ''' Output Student name, position allocated and what choice they got '''

    row_list = []
    for key, value in students.items():
        if (value[GRADE] in grades):
            # Build candidates company choices and print only if they didn't get a company assigned
            companyChoices = positions[value[WISHLIST0]][COMPANY] if (
                value[WISHLIST0] != None) else ""
            companyChoices += "," + \
                str(positions[value[WISHLIST1]][COMPANY]) if (
                    value[WISHLIST1] != None) else ""
            companyChoices += "," + \
                str(positions[value[WISHLIST2]][COMPANY])if (
                    value[WISHLIST2] != None) else ""
            row_list.append([key,
                             value[EMAIL],
                             value[GRADE],
                             positions[value[ASSIGNED]][COMPANY] if (
                                 value[ASSIGNED] != None) else companyChoices,
                             value[ASSIGNED],
                             value[RANKRCVD]])

    header_row = ["Student Name", "Student Email", "Student Grade",
                  "Company Name", "Position ID", "Wishlist Order"]
    with open('JobShare.csv', 'w', newline='') as csvfile:
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
        0: [0, 1000, 0, 0],
        1: [0, 1000, 0, 0],
        2: [0, 1000, 0, 0],
        3: [0, 1000, 0, 0]
    }
    firstChoice = 0
    secondChoice = 0
    thirdChoice = 0
    noChoice = 0
    for key, value in students.items():
        slots = positions[value[WISHLIST0]][SLOTSAVAIL] if (
            value[WISHLIST0] != None) else 0
        slots += positions[value[WISHLIST1]
                           ][SLOTSAVAIL] if (value[WISHLIST1] != None) else 0
        slots += positions[value[WISHLIST2]
                           ][SLOTSAVAIL] if (value[WISHLIST2] != None) else 0
        if value[RANKRCVD] == None:
            noChoice += 1
            results[3][0] += 1
            results[3][2] += slots
            if results[3][1] > slots:
                results[3][1] = slots
            if results[3][3] < slots:
                results[3][3] = slots
        elif value[RANKRCVD] == 0:
            firstChoice += 1
            results[0][0] += 1
            results[0][2] += slots
            if results[0][1] > slots:
                results[0][1] = slots
            if results[0][3] < slots:
                results[0][3] = slots
        elif value[RANKRCVD] == 1:
            secondChoice += 1
            results[1][0] += 1
            results[1][2] += slots
            if results[1][1] > slots:
                results[1][1] = slots
            if results[1][3] < slots:
                results[1][3] = slots
        else:
            thirdChoice += 1
            results[2][0] += 1
            results[2][2] += slots
            if results[2][1] > slots:
                results[2][1] = slots
            if results[2][3] < slots:
                results[2][3] = slots

    for i in range(0, 4):
        results[i][2] = results[i][2]/results[i][0]
    print(results)
