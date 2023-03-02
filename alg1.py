'''
 1st algorithm for lottery:
     Process 1st choices:
        if underallocated 1st choice -> assign
        if no 2nd chioce -> assign  (warn if this exceeds slots for that position)
        make 1 more pass, assign 1st choice for all unless position is full
    Repeat same process for 2nd and 3rd choices
'''
def compute1(positions, students):

    # Do the Flex hack (if Flex, PosID = 341 is any 3 choices, assign)
    for key, value in students.items():
       for i in range (0,3):
            if value[i] != None:
                posID = positions[value[i]][0]      # students 1st choice, assumes not None
                if posID == 341:
                    if positions[posID][4] < positions[posID][2]:  # not overallocated
                        students[key][3] = posID    # assign choice
                        students[key][4] = i        # what choice student got (0-2)
                        positions[posID][4] += 1    # increment allocation count for this position
                
    # Now continue with regularly scheduled program

    # 1st step in algorithm, allocate jobs to students whose 1st choice isn't overallocated
    for key, value in students.items():
        if value[3] == None:      # if not already assigned a job
            posID = positions[value[0]][0]      # students 1st choice, assumes not None
            if positions[posID][4] < positions[posID][2]:  # not overallocated
                students[key][3] = posID    # assign 1st choice
                students[key][4] = 0        # what choice student got (0-2)
                positions[posID][4] += 1    # increment allocation count for this position
 
    # 2nd step in algorithm, if student doesn't have 2nd choice, give them preference for 1st choice
    #for key, value in students.items():
    #    if value[1] == None and value[3] == None:  # no second choice and not yet assigned job
    #        posID = positions[value[0]][0]
    #        if (positions[posID][4] > positions[posID][2]):
    #            print("Overallocated position: {0} for student {1} when only choice, skipping".format(
    #               posID, key))
    #        else:
    #            students[key][3] = posID    # assign 1st choice
    #            students[key][4] = 0        # what choice student got (0-2)
    #            positions[posID][4] += 1    # increment allocation count for this position 

    # 3rd step in algorithm, assign remaining 1st choice spots until positions are full
    for key, value in students.items():
        if value[3] == None:      # if not already assigned a job
            posID = positions[value[0]][0]
            if (positions[posID][4] >= positions[posID][2]):
                #print("Overallocated position: {0} for student {1}, skipping".format(
                #posID, key))
                pass
            else:
                students[key][3] = posID    # assign 1st choice
                students[key][4] = 0        # what choice student got (0-2)
                positions[posID][4] += 1    # increment allocation count for this position

    # repeat same for 2nd choices for any student not yet allocated

    # 1st step in algorithm, allocate jobs to students whose 2nd choice isn't overallocated
    for key, value in students.items():
        if value[1] != None and value[3] == None:
            posID = positions[value[1]][0]      # students 2nd choice, assumes not None
            if positions[posID][4] < positions[posID][2]:  # not overallocated
                students[key][3] = posID    # assign 2nd choice
                students[key][4] = 1        # what choice student got (0-2)
                positions[posID][4] += 1    # increment allocation count for this position

    # 2nd step in algorithm, if student doesn't have 3nd choice, give them preference for 2nd choice
    #for key, value in students.items():
    #    if value[2] == None and value[3] == None:  # no second choice and not yet assigned job
    #        posID = positions[value[1]][0]
    #        if (positions[posID][4] > positions[posID][2]):
    #            print("Overallocated position: {0} for student {1} when only choice, skipping".format(
    #                posID, key))
    #        else:
    #            students[key][3] = posID    # assign 1st choice
    #            students[key][4] = 0        # what choice student got (0-2)
    #            positions[posID][4] += 1    # increment allocation count for this position 

    # 3rd step in algorithm, assign remaining 2nd choice spots until positions are full
    for key, value in students.items():
        if value[1] != None and value[3] == None:   # not yet assigned job
            posID = positions[value[1]][0]
            if (positions[posID][4] >= positions[posID][2]):
                #print("Overallocated position: {0} for student {1}, skipping".format(
                #posID, key))
                pass
            else:
                students[key][3] = posID    # assign 1st choice
                students[key][4] = 1        # what choice student got (0-2)
                positions[posID][4] += 1    # increment allocation count for this position

    # finally, allocate 3rd chioce to any remaining students, warn if they don't have a spot available
    for key, value in students.items():
        if value[2] != None and value[3] == None:   # not yet assigned job
            posID = positions[value[2]][0]
            if (positions[posID][4] >= positions[posID][2]):
                print("Overallocated position: {0} for student {1} and 3rd choice skipping".format(
                posID, key))
            else:
                students[key][3] = posID    # assign 1st choice
                students[key][4] = 2        # what choice student got (0-2)
                positions[posID][4] += 1    # increment allocation count for this position

