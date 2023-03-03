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

    # Iterate over all wishlist choices, starting with first
    for choice in range (0, MAXCHOICES):
        # Allocate choices to students until the positions fill
        for key, value in students.items():
            if (value[ASSIGNED] == None and value[choice] != None):  # Not yet assigned and has a wishlist choice
                posID = positions[value[choice]][POSID]      
                if positions[posID][ALLOCCOUNT] < positions[posID][SLOTSAVAIL]:  # not overallocated
                    students[key][ASSIGNED] = posID     # assign choice
                    students[key][RANKRCVD] = choice     # what choice student received
                    positions[posID][ALLOCCOUNT] += 1   # increment allocation count for this position
                else:
                    #print("{0} not allocated choice #{1} because position {2} is full".format(
                    #    key, choice, posID))
                    pass

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
            for i in range (0,MAXCHOICES):      # loop through all 3 choices
                if value[i] != None:
                    posID = positions[value[i]][POSID]      # students 1st choice, assumes not None
                    if posID != None and posID ==job:
                        if positions[posID][ALLOCCOUNT] < desiredCount:  # not yet at desired count
                            students[key][ASSIGNED] = posID    # assign choice
                            students[key][RANKRCVD] = i        # what choice student got (0-2)
                            positions[posID][ALLOCCOUNT] += 1    # increment allocation count for this position