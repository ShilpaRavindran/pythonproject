def print_employee(**kwargs):
    employees = {
        1000: {"eid": 1000, "ename": "ram", "desig": "developer", "salary": 30000},
        1001: {"eid": 1001, "ename": "raj", "desig": "qa", "salary": 28000},
        1002: {"eid": 1002, "ename": "roja", "desig": "ba", "salary": 25000}
    }
    id=kwargs["eid"]
    if id in employees:

        print(employees[id]["ename"])
        if "proprty" in kwargs:
            prop=kwargs["property"]
            print(employees[id][prop])
    else:
        print("invalid")
print_employee(eid=1000,property="desig")
print_employee(eid=1002,property="salary")