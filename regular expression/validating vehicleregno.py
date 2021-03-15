

from re import*
rule="KL[0-9]{2}[A-Z]{2}[0-9]{1,4}"#[K][L]\d{2}[A-Z]{2}\d{1,4}
vehicle_reg_no=input("enter vehicle register no:")
matcher=fullmatch(rule,vehicle_reg_no)
if matcher!=None:
    print("valid")
else:
    print("invalid")