
n,m=2,6
#userinput=['1 alex','1 Alex','2 sam','1 alix','1 Alix','2 caM']
userinput = ['3 jun','3 Jin','1 Li','2 Kitty','2 Josh','3 Bob','1 Dave','2 Jose','1 David','3 Rob','3 Anne','3 Ann','3 Kevin','2 Lara','1 ALI','3 Xin']
#for i in userinput1:
    #print(i)
'''
for i in range(int(m)):
    string = input()
    userinput.append(string)
'''

# INPUT
# alex Alex alix Alix
# sam caM

# INPUT
# li dave david ali
# kitty josh jose kevin lara
# jun jin bob rob anne ann xin

# RIGHT ANSWER
# li dave david ali
# kitty josh kevin lara
# jun bob anne ann xin

# algo: sort by each class
# so class 1 2 3
# then compare name in each class

# how to compare each class
# loop through the list of names
# compare

def classSeparation(nameList):
    for i in range(len(userinput)):
        newus = userinput[i].split(' ')
        newus[1] = newus[1].lower()
        #print(newus[1])
        nameList.append(newus[1])
    print(nameList)
def compare(name1,name2):
    # if 2 strings have the same length, compare them
    if len(name1) == len(name2):
        # loop through each character in the string
        counter = 0
        for i in range(len(name1)):
            # if they have the same character, add 1 to counter
            if name1[i] != name2[i]:
                counter +=1
        # if they're too similar, difference <=1
        if counter >= 1:
            return name1
    else:
        return ''
    #return counter

#print(compare('jooon','xin'))
def d2(classMember):
    for i in range(len(classMember)):
        for j in range(len(classMember)):
            print(classMember[i],classMember[j])
def d1(classMember):
    newList = []
    for i in range(len(classMember)):
        classMember[i] =classMember[i].upper()
        for j in range(i + 1, len(classMember)):
            print(classMember[i],classMember[j])
            temp = compare(classMember[i],classMember[j])
            #newList.append(compare(classMember[i],classMember[j]))
            if temp not in newList and temp != '':
                newList.append(temp)
    nl2 = []
    for i in range(len(newList)):
        for j in range(i + 1, len(newList)):
            temp1= compare(newList[i],newList[j])
            if temp1 not in nl2 and temp1 !='':
                nl2.append(temp1)

    print(nl2)


def find_similarity(s1,s2):
    counter=0
    for l in range(len(s1)):
        if s1[l] != s2[l]:
            counter += 1
    if counter < 2:
        return s1

#print(find_similarity('aeee','alen'))
def main():
    nameList =[]
    for i in range(len(userinput)):
        newus = userinput[i].split(' ')
        newus[1] = newus[1].lower()
        #print(newus[1])
        nameList.append(newus[1])
    print(nameList)
    nl=[]
    didntmakeit = []
    # range a - z
    # 25
    print(d1(nameList))
    for i in range(1,len(nameList)):
        if len(nameList[i]) != len(nameList[i-1]):
            nl.append(nameList[i-1])
        else:
            '''
            word1 = nameList[i]
            word2 = nameList[i-1]
            temp0=0
            temp1=0
            word1 = list(word1)
            word2 = list(word2)
            #word2.sort()
            #word1.sort()
            counter=0
            print(nameList[i])
            print(nameList[i-1])
            for l in range(len(word1)):
                if word1[l] != word2[l]:
                    counter+=1
            print('here', word1)
            print('here', word2)
            for j in nameList[i]:
                temp0+=ord(j)
            for x in nameList[i-1]:
                temp1+=ord(x)
            print('counter',counter)
            '''
            if find_similarity(nameList[i],nameList[i-1]) != 'None':
                didntmakeit.append(nameList[i])
            #print('ascii',nameList[i],temp0)
            #print('ascii2', nameList[i-1], temp1)

            #print(nameList[i-1],nameList[i])
            #print(nameList[i])

    #print(didntmakeit)
    #print(nl)
    thirdlist=[]
    for i in range(len(nameList)):
        for j in range(len(nameList)):
            if nameList[i] == nameList[j]:
                nameList[i]=''
                continue
    #print(nameList)
main()