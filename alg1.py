'''
 1st algorithm for lottery:
     Very basic, assign 1st choices until positions fill, then move to 2nd choices and then 3rd
     There can/will be students who don't get a spot depending on slots available for their 
     job choices.
'''
import random
from constants import MAXCHOICES, POSID, SLOTSAVAIL, ALLOCCOUNT, GRADE, ASSIGNED, RANKRCVD


def compute1(positions, students, grades):
    ''' the most basic lottery algorithm '''

    if len(grades) == 0:
        return

    random.seed(4)    # seed random number generator for reproducible results
    for grade in grades:       # allocate in grade priority order
        # Iterate over all wishlist choices, starting with first
        for choice in range(0, MAXCHOICES):
            # Allocate choices to students until the positions fill
            items = list(students.items())
            random.shuffle(items)
            for key, value in items:
                if value[GRADE] == grade:     # only run for the current grade
                    # Not yet assigned and has a wishlist choice
                    if (value[ASSIGNED] is None and value[choice] is not None):
                        pos_id = positions[value[choice]][POSID]
                        # not overallocated
                        if positions[pos_id][ALLOCCOUNT] < positions[pos_id][SLOTSAVAIL]:
                            # assign choice
                            students[key][ASSIGNED] = pos_id
                            # what choice student received
                            students[key][RANKRCVD] = choice
                            # increment allocation count for this position
                            positions[pos_id][ALLOCCOUNT] += 1
                        else:
                            pass


def pre_fill(positions, students, preferred_jobs, grades):
    ''' Can be used as a first step before normal algorithm runs
       This routine will allocate upto percent full for each job in the preferredJobs list
       starting with 1st chioces and progressing to 2nd and 3rd choices until percetn full
       is reached or no more students have requrested

        positions:  The positions dictionary used throughout the program
        students:   The students dictionary used throughout the program
        preferredJobs:  A dictionary (key is position ID and value is desired percent full)
    '''
    if len(preferred_jobs) == 0:
        return

    for job, percent in preferred_jobs.items():
        desired_count = int(positions[job][2] * percent)
        print(
            f'Filling position {job} to {desired_count} out of {positions[job][2]} total seats')
        for key, value in students.items():
            if value[GRADE] in grades:
                for i in range(0, MAXCHOICES):      # loop through all 3 choices
                    if value[i] is not None:
                        # students 1st choice, assumes not None
                        pos_id = positions[value[i]][POSID]
                        if pos_id is not None and pos_id == job:
                            # not yet at desired count
                            if positions[pos_id][ALLOCCOUNT] < desired_count:
                                # assign choice
                                students[key][ASSIGNED] = pos_id
                                # what choice student got (0-2)
                                students[key][RANKRCVD] = i
                                # increment allocation count for this position
                                positions[pos_id][ALLOCCOUNT] += 1
