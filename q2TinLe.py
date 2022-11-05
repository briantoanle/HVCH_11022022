courses = 3
entries = 6
ui1 = ['1 alex','1 Alex','2 sam','1 alix','1 Alix','2 caM']

ui2 = ['3 jun','3 Jin','1 Li','2 Kitty','2 Josh','3 Bob','1 Dave','2 Jose','1 David','3 Rob','3 Anne','3 Ann','2 Kevin','2 Lara','1 ALI','3 Xin']
#courses = 3
#entries = 16
#stuEntries = ['3 jun','3 Jin',]
# same string
# string with 1 character difference
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
for i in range(len(co)):
    print(co)