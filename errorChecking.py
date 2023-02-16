from datetime import datetime, date
# from ".US_modules/DateBeforeCurrent" import dateBeforeCurrentDate
# from US_modules import *

from US_modules.DateBeforeCurrent import dateBeforeCurrentDate
from US_modules.Parents_not_too_old import parents_not_too_old
from US_modules.individual_is_too_young_to_be_married import individual_is_too_young_to_be_married
from US_modules.ageIsLessThan150 import ageIsLessThan150
from US_modules.divorceBeforeDeath import divorceBeforeDeath

# Initial error checking of incorrect lines
def initial_error_checking(gedcom_lines):
    for index, line in enumerate(gedcom_lines):
        # if the line is a level 0 tag
        if line[0] == "0":
            pass

        # if the line is a level 1 tag
        elif line[0] == "1":
            # Asserting that 1 DATE is not present
            assert(line.split()[-1] != "DATE")

        # if the line is a level 2 tag
        elif line[0] == "2":
            # Asserting that 2 NAME is not present
            assert(line.split()[1] != "NAME")

# List of individual functions
individual_functions = [
    dateBeforeCurrentDate,
    parents_not_too_old,
    individual_is_too_young_to_be_married,
    ageIsLessThan150
]

# Error checking the individuals
def individuals_error_checking(individual_list):
    print('-'*50, 'Starting Individual Error Checking', '-'*50)
    counter = 0
    for function in individual_functions:
        try: 
            function(individual_list)
            print(f"Success {function.__name__} ✅")
        except AssertionError: 
            print(f"Error: {AssertionError} on function {function.__name__} ❌")
            counter += 1
    if counter == 0: print("All individual tests passed ✅")
    else: print(f"{counter} tests failed ❌")

# List of family functions
family_functions = [
    divorceBeforeDeath
]

def families_error_checking(individual_list, family_list):
    print('-'*50, 'Starting Family Error Checking', '-'*50)
    counter = 0
    for function in family_functions:
        try:
            function(individual_list, family_list)
            print(f"Success {function.__name__} ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")
            counter += 1
    if counter == 0: print("All family tests passed ✅")
    else: print(f"{counter} tests failed ❌")

    # birth_before_death(individual_list)
    # for individual in individual_list:
    #     # [US07] - TaeSeo
    #     if individual['Age'] != 'N/A':
    #         assert(int(individual['Age']) < 150), "Individual is too old"

    #     # [US01] - Justus
    #     if individual['Birthday'] != 'N/A':
    #         date = individual['Birthday'].split()
    #         day, month, year = int(date[0]), int(
    #             datetime.strptime(date[1], "%b").month), int(date[2])
    #         curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
    #         assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay)), "Birth date is after today's date"

    #     # [US01] - Justus
    #     if individual['Death'] != 'N/A':
    #         date = individual['Death'].split()
    #         day, month, year = int(date[0]), int(
    #             datetime.strptime(date[1], "%b").month), int(date[2])
    #         curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
    #         assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay)), "Death date is after today's date"


# # Error checking the families
# def families_error_checking(family_list, individual_list):
    
#     for family in family_list:
#         # [US03] - Mateusz
#         if family['Marriage Date'] != 'N/A':
#             for individual in individual_list:
#                 if individual['ID'] == family['Husband ID']:
#                     if individual['Birthday'] != 'N/A':
#                         MarriageDate = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
#                         husbandBirthDate = datetime.strptime(individual['Birthday'], '%d %b %Y').date()
#                         assert(husbandBirthDate < MarriageDate), "Husband birth date is after husband's Marriage date"
                

#                 if individual['ID'] == family['Wife ID']:
#                     if individual['Birthday'] != 'N/A':
#                         MarriageDate = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
#                         wifeBirthDate = datetime.strptime(individual['Birthday'], '%d %b %Y').date()
#                         assert(wifeBirthDate < MarriageDate), "Wife birth date is after husband's Marriage date"
                        
#         # [US06] - TaeSeo Um
#         if family['Divorce Date'] != 'N/A':
#             for individual in individual_list:
#                 if individual['ID'] == family['Husband ID']:
#                     if individual['Death'] != 'N/A':
#                         divorceDate = datetime.strptime(family['Divorce Date'], '%d %b %Y').date()
#                         husbandDeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
#                         assert(divorceDate < husbandDeathDate), "Divorce date is after husband's death date"
                

#                 if individual['ID'] == family['Wife ID']:
#                     if individual['Death'] != 'N/A':
#                         divorceDate = datetime.strptime(family['Divorce Date'], '%d %b %Y').date()
#                         wifeDeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
#                         assert(divorceDate < wifeDeathDate), "Divorce date is after wife's death date"

#         # [US01] - Justus
#         if family['Marriage Date'] != 'N/A':
#             date = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
#             curDate = datetime.now().date()
#             assert(date < curDate), "Marriage date is after today's date"
#         if family['Divorce Date'] != 'N/A':
#             date = datetime.strptime(family['Divorce Date'], '%d %b %Y').date()
#             curDate = datetime.now().date()
#             assert(date < curDate), "Divorce date is after today's date"

# #Mateusz USER STORY 02
# #If there are individuals in the list for whom birth and death dates are not both available, or all individuals were born after they died, the function will return False.
# def birth_before_death(individuals):
#     for individual in individuals:
#         individual_values = {
#             'ID': 'N/A',
#             'Name': 'N/A',
#             'Gender': 'N/A',
#             'Birthday': 'N/A',
#             'Age': 'N/A',
#             'Alive': 'N/A',
#             'Death': 'N/A',
#             'Child': 'N/A',
#             'Spouse': 'N/A'
#         }

#         for attributes in individual:
#             individual_values[attributes[0]] = attributes[1]

#         #if(individual_values['Death'] == 'N/A' and individual_values['Alive'] == 'True'):
#         #    return True
        
#         if(individual_values['Death'] == 'N/A' or individual_values['Birthday'] == 'N/A'):
#             continue

#         birthdate = individual_values['Birthday'].split()
#         Birthday, Birthmon, Birthyear = birthdate[0], birthdate[1], birthdate[2]

#         deathdate = individual_values['Death'].split()
#         Deathday, Deathmon, Deathyear = deathdate[0], deathdate[1], deathdate[2]

#         if(Deathyear > Birthyear):
#             return True
#         elif(Birthyear == Deathyear):
#             if(datetime.strptime(Deathmon, '%b').month > datetime.strptime(Birthmon, '%b').month):
#                 return True
#             if(datetime.strptime(Deathmon, '%b').month == datetime.strptime(Birthmon, '%b').month):
#                 if(Deathday >= Birthday):
#                     return True
#         else:
#             print('ERR0R: Death was before birth')
#             return False
        
#     return False

    
# #Mateusz USER STORY 03
# #doesnt check if birthday is missing, maybe new user story?
# def birth_before_marriage(individuals, families):
    
#     for family in families:
#         family_values = {
#             'Family ID': 'N/A',
#             'Marriage Date': 'N/A',
#             'Divorce Date': 'N/A',
#             'Husband ID': 'N/A',
#             'Wife ID': 'N/A',
#             'Children ID(s)': ['N/A']
#         }

#         for attributes in family:
#             if attributes[0] == 'Children ID(s)':
#                 family_values['Children ID(s)'].append(attributes[1])
#             else:
#                 family_values[attributes[0]] = attributes[1]

#         if len(family_values['Children ID(s)']) > 1:
#             family_values['Children ID(s)'] = family_values['Children ID(s)'][1:]

#         husband_birth = None
#         wife_birth = None
#         marriage_date = None

#         for individual in individuals:
#             if individual[0][1] == family_values['Husband ID']:
#                 for attr in individual:
#                     if attr[0] == 'Birthday':
#                         husband_birth = datetime.strptime(attr[1], '%d %b %Y').date()
#                         break

#             elif individual[0][1] == family_values['Wife ID']:
#                 for attr in individual:
#                     if attr[0] == 'Birthday':
#                         wife_birth = datetime.strptime(attr[1], '%d %b %Y').date()
#                         break

#         if family_values['Marriage Date'] != 'N/A' and husband_birth and wife_birth:
#             marriage_date = datetime.strptime(family_values['Marriage Date'], '%d %b %Y').date()
#             if husband_birth > marriage_date or wife_birth > marriage_date:
#                 print(f"ERROR: STORY ID US03: {family_values['Family ID']}: Birth date is before Marraige Date of either husband or wife")
#                 return False

#     return True
