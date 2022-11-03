#n,m = 3,6
#group = ['A','A','A']
#userinput = ['cite 3 1','change 1','cite 1 2','change 1','change 2','cite 2 1']
n,m = input().split()
group = input().split()
userinput=[]
for i in range(int(m)):
    string = input()
    userinput.append(string)
x=0
y=0
for i in range(len(userinput)):
    newUs = userinput[i].split(' ')
    newUs[1]=int(newUs[1])-1
    if 'cite' in userinput[i]:
        newUs[2] = int(newUs[2])-1
        if group[newUs[1]] == group[newUs[2]]:
            if group[newUs[1]] == 'B':
                y += 1
            elif group[newUs[1]] == 'A':
                x += 1
        else:
            if group[int(newUs[2])] == 'B':
                y += 5
            elif group[int(newUs[2])] == 'A':
                x += 5
    elif 'change' in userinput[i] and group[newUs[1]] == 'A':
        #print('here',group[newUs[1]])
        group[newUs[1]] = 'B'
        #print('heredith',group[newUs[1]])

    elif 'change' in userinput[i] and group[newUs[1]] == 'B':
        group[newUs[1]] = 'A'

print(x,y)
#print(group)