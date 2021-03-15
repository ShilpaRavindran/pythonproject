#customised exception generates by using raise

no=int(input("enter no:"))
try:
    if no<0:
        raise Exception("invalid")#constructor calling
except Exception as e:
    print(e.args)

# digitalocean-hwtoinstll mysql
# sudo apt update
# pwd
# sudo apt installl mysql-server
