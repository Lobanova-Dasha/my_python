#exceptions.py

try:
    f = open('text_file.txt')
    print(f.read())
    f.close() 
    f2 = open('currupt_file.txt') 
    if f2.name == 'currupt_file.txt':
     	raise Exception
except FileNotFoundError as e:
	#print('Sorry, this file does not exist.')
	print(e)
except Exception as e:
    #print('Sorry, something went wrong.')
    print('Error was raised!')
else:
    # print(f.read())
    # f.close() 
    print(f2.read())
    f2.close() 
finally:
	print('Executing Finally...')
