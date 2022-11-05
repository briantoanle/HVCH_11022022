
n,m=2,6
userinput=['1 alex','1 Alex','2 sam','1 alix','1 Alix','2 caM']
#userinput = ['3 jun','3 Jin','1 Li','2 Kitty','2 Josh','3 Bob','1 Dave','2 Jose','1 David','3 Rob','3 Anne','3 Ann','3 Kevin','2 Lara','1 ALI','3 Xin']
#for i in userinput1:
    #print(i)
'''
for i in range(int(m)):
    string = input()
    userinput.append(string)
'''

# INPUT
# li dave david ali
# kitty josh jose kevin lara
# jun jin bob rob anne ann xin

# RIGHT ANSWER
# li dave david ali
# kitty josh kevin lara
# jun bob anne ann xin
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
    print(nl)
    thirdlist=[]
    for i in range(len(nameList)):
        for j in range(len(nameList)):
            if nameList[i] == nameList[j]:
                nameList[i]=''
                continue
    #print(nameList)
main()