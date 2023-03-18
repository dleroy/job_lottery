'''
Columns of interest in followmedata.csv export data:

 "Position ID":          unique ID associated with a Job Share position at a company
 "Total Seat Count":     # of seats available for a specific "Position ID"
 "Remainin Seat Count":  # of seats remaining (assumes a previous lottery already run)
 "Wishlist Order":       how student ranked this company,  0 = highest, 2 = lowest
 "Company Name":         for mapping "Position ID" to a company
 "Student Name":         for mapping wishlist positions to a student
 "Student Email":        to map to corresponding student name in the output
 "Student Grade":        if you want to run lottery on a subset of grades
'''
import pandas as pd
from utils import printSummaryStats, printAllocationStats, writeStudentResults
from alg1 import compute1, pre_fill
from constants import WISHLIST0, WISHLIST1, WISHLIST2, EMAIL, GRADE, FSTCHOICE, SNDCHOICE, THRDCHOICE

# Read job share data into Pandas dataframe
followme = pd.read_csv("./followmedata.csv")
followme = followme.reset_index()  # make sure indexes pair with number of rows

# iterate over exported data, building data structures for managing lottery algorithm
PositionDict = {}
StudentDict = {}

# Initialize data structures for tracking job allocations
for index, row in followme.iterrows():

    # initialize position table  (Key is Position ID)
    PositionDict[row["Position ID"]] = [row["Position ID"],
                                        row["Company Name"],
                                        row["Total Seat Count"],
                                        row["Remaining Seat Count"],
                                        0,   # number seats allocated
                                        0,   # desired 2nd choice count
                                        0,   # desired 3rd choice count
                                        0]   # desired 1st choice count

    # initialize student table (Key is Student Name)
    StudentDict[row["Student Name"]] = [
        None, None, None, None, None, None, None]

# 2nd pass for StudentDict to populate wishlist choices
for index, row in followme.iterrows():
    if row["Wishlist Order"] == 0:
        StudentDict[row["Student Name"]][WISHLIST0] = row["Position ID"]
    if row["Wishlist Order"] == 1:
        StudentDict[row["Student Name"]][WISHLIST1] = row["Position ID"]
    if row["Wishlist Order"] == 2:
        StudentDict[row["Student Name"]][WISHLIST2] = row["Position ID"]
    StudentDict[row["Student Name"]][EMAIL] = row["Student Email"]
    StudentDict[row["Student Name"]][GRADE] = row["Student Grade"]

# Now calculate desired wishlist 0 position counts and update the Position dict
# XXX Note that this is currently for all exported data and not grade specific
for index, row in followme.iterrows():
    if row["Wishlist Order"] == 0:
        PositionDict[row["Position ID"]][FSTCHOICE] += 1
    elif row["Wishlist Order"] == 1:
        PositionDict[row["Position ID"]][SNDCHOICE] += 1
    elif row["Wishlist Order"] == 2:
        PositionDict[row["Position ID"]][THRDCHOICE] += 1

# Define grades you want to consider in lottery. Order matters. 1st element will get allocations 1st
# grades = ["Freshman", "Sophomore", "Junior", "Senior"]
grades = ["Senior", "Junior", "Sophmore", "Freshman"]

# If you want to pre-fill specific Job IDs, put the list here (posID: %tofill 0.0-1.0 )
# preferredJobs = { 341: 1.0,     # Flex
#                  332: 1.0,     # Lockheed
#                  331: 1.0,     # Intuitive Surgical
#                  }
preferredJobs = {}

# Preprocessing step to "pre-fill" speicific roles first
pre_fill(PositionDict, StudentDict, preferredJobs, grades)

# Compute and output results of algorithm 1 selection
compute1(PositionDict, StudentDict, grades)

# Print Student results to a CSV file JobShare.csv
writeStudentResults(PositionDict, StudentDict, grades)

# Print stats about positions and students to cross check with followmejobshadow.com site
printSummaryStats(PositionDict, StudentDict)

# print 1st, 2nd, 3rd choide stats
printAllocationStats(PositionDict, StudentDict, grades)
