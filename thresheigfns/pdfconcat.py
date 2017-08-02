import os


for m in ['1','2','3','4','5']:
    for p in ['10','20','30','40', '49', '50', '51','60','70','80', '90']:
    	for a in ['2', '3', '4', '5']:
        	pdfs = ''
        	index = 1
        	while os.path.isfile('./'+m+'/'+p+'/'+a+'/'+str(index)+'.pdf'):
            		pdfs = pdfs + './'+m+'/'+p+'/'+a+'/'+str(index)+'.pdf ' 
            		index = index + 1
        		os.system('pdfunite ' + pdfs + 'output/m'+m+'p'+p+'cut'+a+'.pdf')

