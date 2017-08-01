import os



for x in ['1','2','3','4']:
   for y in ['10','20','30','40','49','50','51','60','70','80','90']:
       os.system('cp m'+x+'p'+y+'.dat ' + 'm'+x+'p'+y+'.csv')


