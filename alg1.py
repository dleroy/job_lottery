'''
 1st algorithm for lottery:
     Process 1st choices:
        if underallocated 1st choice -> assign
        if no 2nd chioce -> assign  (warn if this exceeds slots for that position)
        make 1 more pass, assign 1st choice for all unless position is full
    Repeat same process for 2nd and 3rd choices
'''
from constants import *

def compute1(positions, students):

    # 1st step in algorithm, allocate jobs to students whose 1st choice isn't overallocated
    for key, value in students.items():
        if value[ASSIGNED] == None:      # if not already assigned a job
            posID = positions[value[WISHLIST0]][POSID]      # students 1st choice, assumes not None
            if positions[posID][ALLOCCOUNT] < positions[posID][SLOTSAVAIL]:  # not overallocated
                students[key][ASSIGNED] = posID    # assign 1st choice
                students[key][RANKRCVD] = 0        # what choice student got (0-2)
                positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position

    # 3rd step in algorithm, assign remaining 1st choice spots until positions are full
    for key, value in students.items():
        if value[ASSIGNED] == None:      # if not already assigned a job
            posID = positions[value[WISHLIST0]][POSID]
            if (positions[posID][ASSIGNED] >= positions[posID][SLOTSAVAIL]):
                #print("Overallocated position: {0} for student {1}, skipping".format(
                #posID, key))
                pass
            else:
                students[key][ASSIGNED] = posID    # assign 1st choice
                students[key][RANKRCVD] = 0        # what choice student got (0-2)
                positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position

    # repeat same for 2nd choices for any student not yet allocated

    # 1st step in algorithm, allocate jobs to students whose 2nd choice isn't overallocated
    for key, value in students.items():
        if value[WISHLIST1] != None and value[ASSIGNED] == None:
            posID = positions[value[WISHLIST1]][POSID]      # students 2nd choice, assumes not None
            if positions[posID][ASSIGNED] < positions[posID][SLOTSAVAIL]:  # not overallocated
                students[key][ASSIGNED] = posID    # assign 2nd choice
                students[key][RANKRCVD] = 1        # what choice student got (0-2)
                positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position

    # 3rd step in algorithm, assign remaining 2nd choice spots until positions are full
    for key, value in students.items():
        if value[WISHLIST1] != None and value[ASSIGNED] == None:   # not yet assigned job
            posID = positions[value[WISHLIST1]][POSID]
            if (positions[posID][ASSIGNED] >= positions[posID][SLOTSAVAIL]):
                pass
            else:
                students[key][ASSIGNED] = posID    # assign 1st choice
                students[key][RANKRCVD] = 1        # what choice student got (0-2)
                positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position

    # finally, allocate 3rd chioce to any remaining students, warn if they don't have a spot available
    for key, value in students.items():
        if value[WISHLIST2] != None and value[ASSIGNED] == None:   # not yet assigned job
            posID = positions[value[WISHLIST2]][POSID]
            if (positions[posID][ASSIGNED] >= positions[posID][SLOTSAVAIL]):
                print("Overallocated position: {0} for student {1} and 3rd choice skipping".format(
                posID, key))
            else:
                students[key][ASSIGNED] = posID    # assign 1st choice
                students[key][RANKRCVD] = 2        # what choice student got (0-2)
                positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position



def preFill(positions, students, preferredJobs):
    ''' Can be used as a first step before normal algorithm runs
       This routine will allocate upto percent full for each job in the preferredJobs list
       starting with 1st chioces and progressing to 2nd and 3rd choices until percetn full
       is reached or no more students have requrested
       
        positions:  The positions dictionary used throughout the program
        students:   The students dictionary used throughout the program
        preferredJobs:  A dictionary (key is position ID and value is desired percent full)
    '''
    for job, percent in preferredJobs.items():
        desiredCount = int(positions[job][2] * percent)
        print("Filling position {0} to  {1} out of {2} total seats".format(
            job, desiredCount, positions[job][2]))
        for key, value in students.items():
            for i in range (0,3):      # loop through all 3 choices
                if value[i] != None:
                    posID = positions[value[i]][POSID]      # students 1st choice, assumes not None
                    if posID != None and posID ==job:
                        if positions[posID][ALLOCCOUNT] < desiredCount:  # not yet at desired count
                            students[key][ASSIGNED] = posID    # assign choice
                            students[key][RANKRCVD] = i        # what choice student got (0-2)
                            positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position