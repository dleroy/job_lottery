# JobShadow Lottery Selection
This is a standalone python program that takes an exported report from the 2022 Job Shadow Program website and assigns job choices to students.

Configurable parameters:
  1) Grades: You can define the grades considered in the lottery. These are in a priority order and 1st in the list will get allocations first.
  2) Companies: You can define a set of companies and how full you'd like their allocations. This will be done as a preprocessing step before the 
     general lottery algorithm runs.
     
 Both of these are currently defined in lottery.py and not exposed as externally configurable parameters

 Note: 2023 lottery program is in jobcamp_lottery repo
 
