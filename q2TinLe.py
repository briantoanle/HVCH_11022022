courses = 3
entries = 6
ui1 = ['1 alex','1 Alex','2 sam','1 alix','1 Alix','2 caM']

ui2 = ['3 jun','3 Jin','1 Li','2 Kitty','2 Josh','3 Bob','1 Dave','2 Jose','1 David','3 Rob','3 Anne','3 Ann','2 Kevin','2 Lara','1 ALI','3 Xin']
#courses = 3
#entries = 16
#stuEntries = ['3 jun','3 Jin',]
# same string
# string with 1 character difference

def main():
  co = []
  for i in range(courses):
    co.append([])

  course_1=[]
  course_2=[]
  course_3=[]

  for i in ui2:
    if "1" in i:
      co[0].append(i.split())
    elif "2" in i:
      co[1].append(i.split())
    else:
      co[2].append(i.split())

  #print(co[0])

  listreturn = []
  # for loop to go through array of all classes
  for i in range(1,2):
    # in each class


    for j in range(len(co[i])):
      list1 = co[i][j]
      print(list1)
      findNew(list1)
      """
        temp1 = co[i][j][1]
        temp2 = co[i][j-1][1]
        s1 = find_similarity(temp1, temp2)
        if s1 != 'None':
          listreturn.append(s1)
      """
      '''
        if len(temp1)==len(temp2):
          s1 = find_similarity(temp1,temp2)
          if s1 != 'None':
            listreturn.append(s1)
        else:
          listreturn.append(temp1)
      '''
        #print(temp2)
  #print(listreturn)

def compareString(s1,s2):
  if s1.lower() == s2.lower():
    return True
  else:
    return False
def findNew(mylist):
  for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
      print(mylist[i],mylist[j])
      # if compare return true, it means strings are the same
      #if compareString(mylist[i], mylist[j]):

def find_similarity(s1, s2):
  if len(s1)==len(s2):
    print(s1,s2)
    counter = 0
    for l in range(len(s1)):
      if s1[l] != s2[l]:
        counter += 1
    if counter < 2:
      print(counter)
      return s2
  else:
    print('Appending',s1)
    return s1
# separate user input into classes
# go through names in each class
#

main()