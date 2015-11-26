palin = 0
nonlych = 0
lych = 0
num_list=[]

print("I will tell you how many Lychrel candidates are in a specific range.")
low_bound = (int(input("What is the lower bound? ")))
up_bound = (int(input("What is the upper bound? ")))

# creates a list from the lower bound until the upper bound
for i in range (low_bound,up_bound+1):
    num_list.append(i)

for i in num_list:
    value_i = str(i)
    rev_value_i = value_i[::-1]
    if  value_i == rev_value_i:
        palin = palin+1
    else:
        count = 0
        while(value_i != rev_value_i)and(count != 30):
            value_i = int(value_i)
            rev_value_i = int(rev_value_i)
            value_i = value_i + rev_value_i
            value_i = str(value_i)
            rev_value_i = value_i[::-1]

            if value_i == rev_value_i:
                nonlych += 1
            count = count+1

        if(value_i != rev_value_i)and(count == 30):
            print (i ,"is a Lychrel candidate.")
            lych = lych+1

print ("Natural palindromes: ", palin)
print ("Non lychrels (become palindromes): ", nonlych)
print ("Lychrel candidates: ", lych)
