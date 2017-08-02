import os

for p in ['10','20','30','40', '49', '50', '51','60','70','80', '90']:
	pdfs = ''
    	for a in ['1', '2', '3', '4', '5']:
        	pdfs = pdfs +'./p'+p+'cut'+a+'.pdf '
        	os.system('pdfunite ' + pdfs + 'output/p'+p+'.pdf')

