file = open("..\Input.txt","r")
tot = 0

number_name = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def findDig(l):
    for i in range(len(number_name)):
        l = l.replace(number_name[i], number_name[i] + str(i) + number_name[i],1)
        last_ocur = l.rfind(number_name[i])
        if last_ocur != -1:
            l = l[:last_ocur] + number_name[i] + str(i) + number_name[i] + l[last_ocur + len(number_name[i]) :]

#56324
    for x in l:
        if x.isdigit():
            break
    for y in reversed(l):
        if y.isdigit():
            break

    return x,y




for line in file:
    a, b = findDig(line)
    print(a,b)
    sum = str(a) + str(b)

    tot += int(sum)
print(tot)

