import os

'''
Using a Tuple you can pull each item into a seperate variable.
Remember if you know the pattern you can name the variable as shown in the tuple.
In out case our tuple looks like this: ('veil 10', '.mp3')
'''

os.chdir('/Users/Jared/Desktop/rename_test')

#verifies I am in the right directory
#print(os.getcwd())


for f in os.listdir():
#	print(f) = returns all the files in the directory

#	print(os.path.splitext(f)) = returns tuples, split extension off
	file_name, file_ext = os.path.splitext(f)
#	print(file_name.split())

	file_title, file_number = file_name.split()


	file_number = file_number.zfill(2)
	#print('{} - {}{}'.format(file_number, file_title, file_ext))
	new_name ='{} - {}{}'.format(file_number, file_title, file_ext)

	os.rename(f,new_name)
'''
If your file has unwanted space you can use .strip to remove items:
file_title = file_title.strip()
file_number = file_number.strip()
'''