'''
2 groups
student can be only assigned 1 at a time
measure success by citation score, starts at 0

'''

# if x and y same group, their group score + 1
# if x and y different group, y's group score + 5

# 1 cite 3 y=5
# 1 cite 2 x=1
# change 1 B A B B B B
# 2 cite 1 y=10
# 4 cite 2 x=6
def main():
    #n,m = input("students ").split()
    #group = input('group ').split()
    n,m = 6,5
    group = ['A','A','B','B','B','B']
    #group=['A','A','A']
    #userinput=[]
    userinput = ['cite 1 3','cite 1 2','change 1','cite 2 1','cite 4 2','change 1']
    #userinput = ['cite 3 1','change 1','cite 1 2','change 1','change 2','cite 2 1']
    '''
    for i in range(m):
        string = input()
        userinput.append(string)
    
    '''
    #print(group)
    #print(userinput)
    x=0
    y=0
    for i in range(len(userinput)):
        newUs = userinput[i].split(' ')
        print('newus',newUs)
        newUs[1] = int(newUs[1])-1
        print(i,'i counter')
        if 'cite' in userinput[i]:
            newUs[2] = int(newUs[2]) - 1
            if group[int(newUs[1])] == group[int(newUs[2])]:
                #print(newUs)
                print(group[int(newUs[1])],group[int(newUs[2])])
                if group[int(newUs[1])] == 'B':
                    x+=1
                elif group[int(newUs[1])] == 'A':
                    y+=1
            else:
                if group[int(newUs[2])] == 'B':
                    y+=5
                elif group[int(newUs[2])] == 'A':
                    x+=5
        elif 'change' in userinput[i] and group[i] == 'A':
            #print('change')
            #print(group)
            #print('group ',i)
            #print('location of i', i)
            group[int(newUs[1])-1] = 'B'

            #print(group)
        elif 'change' in userinput[i] and group[i-1] == 'B':
            #print('change')
            #print(group)
            #print('group ',i)
            #print('location of i',i)
            group[int(newUs[1])-1] = 'A'

            #print( group)
    print("score x: ",x,'score y: ',y)
main()