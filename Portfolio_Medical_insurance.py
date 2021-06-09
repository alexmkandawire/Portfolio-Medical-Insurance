import csv
insurance_list = []
f_smoker_cost = 0
f_nosmoker_cost = 0
m_parent_cost = 0
f_parent_cost = 0
f_smoker_count = 0
f_nosmoker_count = 0
def opencsvfile():
    with open("C:\Alex files\insurance.csv") as insurance_file:
        insurance_csv = csv.DictReader(insurance_file)
        for insurance_member in insurance_csv:
            insurance_list.append(insurance_member)
        return insurance_list

retrieved_insurance_list = opencsvfile()
    
def calculate_avg_insurance():
    male_count = 0
    male_cost = 0
    female_count = 0
    female_cost = 0
    male_avg= 0
    female_avg = 0
    for insurance_row in retrieved_insurance_list:
        if insurance_row["sex"] == "male":
            male_count += 1
            male_cost += float(insurance_row["charges"])
        else:
            female_count += 1
            female_cost += float(insurance_row["charges"])
    male_avg = male_cost / male_count
    female_avg = female_cost / female_count
    print(f"Average insurance for Females = {round(female_avg, 2)} Male = {round(male_avg, 2)}")

def smoker_avg_insurance():
    smoker_cost = 0
    smoker_count = 0
    nosmoker_cost = 0
    nosmoker_count = 0
    smoker_avg = 0
    non_smoker_avg = 0
    for insurance_row in retrieved_insurance_list:
        if insurance_row["smoker"] == "yes":
            smoker_cost += float(insurance_row["charges"])
            smoker_count += 1
        else:
            nosmoker_cost += float(insurance_row["charges"])
            nosmoker_count += 1
    smoker_avg = smoker_cost / smoker_count
    non_smoker_avg = nosmoker_cost / nosmoker_count
    print(f"Average insurance for smokers = {round(smoker_avg, 2)} Non-Smokers = {round(non_smoker_avg, 2)}")

def parent_avg_insurance():
    parent_cost = 0
    noparent_cost = 0
    parent_count = 0
    noparent_count = 0
    parent_avg = 0
    non_parent_avg = 0
    for insurance_row in retrieved_insurance_list:
       if int(insurance_row["children"]) > 0:
           parent_cost += float(insurance_row["charges"])
           parent_count += 1
       else:
           noparent_cost += float(insurance_row["charges"])
           noparent_count += 1
    parent_avg = parent_cost / parent_count
    non_parent_avg = noparent_cost / noparent_count
    print(f"Average insurance for Parent = {round(parent_avg, 2)} Non-Parent = {round(non_parent_avg, 2)}")
calculate_avg_insurance()
smoker_avg_insurance()
parent_avg_insurance()


