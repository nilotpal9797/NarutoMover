import shutil,os
dir='/home/nilotpal/Downloads' #Put your path here
for i in os.listdir(dir):
	if "Naruto_ Shippuuden" in i and "[9anime.to]" in i: #Specify ondition
		shutil.move(i,'/home/nilotpal/Downloads/NARUTO_SHIPUDEN/') #1st arg->file #2nd arg->folder in which file will move to
