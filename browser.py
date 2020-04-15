import os

nytimes = '''
This New Liquid Is Magnetic, and Mesmerizing
 
Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)
 
 
Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
 
Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.
 
'''
bloomberg = '''
The Space Race: From Apollo 11 to Elon Musk
 
It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)
 
 
Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
 
Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

def menu():
	user_url = input()
	history_list.append(user_url)
	if user_url == 'back':
		del history_list[-2:]
		user_url = history_list[-1]

	if "dir" in user_url:
		create_dir(user_url)
	elif "." in user_url and user_url in text_list:
		pages_list.append(page_url(user_url))
		writer(user_url)
		print(text_list[user_url])
	elif user_url == "exit":
		exit(0)
	elif user_url in pages_list:
		open_page(user_url)
	else:
		print("error")

	return menu()



def create_dir(user_url):
    try:
        os.mkdir(user_url)
        # print("Directory " , user_url,  " Created ")
        global dir_name
        dir_name = user_url
    except FileExistsError:
        print("error")
        return menu()


def writer(user_url):
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)
		with open(f'{dir_name}/{page_url(user_url)}.txt', 'w') as f:
			f.write(text_list[user_url])
	else:
		with open(f'{dir_name}/{page_url(user_url)}.txt', 'w') as f:
			f.write(text_list[user_url])

def page_url(user_url):
    # Return name url
    return user_url.rsplit(".").pop(0)


def open_page(user_url):
	try:
	    with open(f'{dir_name}/{user_url}.txt') as f:
	        for line in f:
	        	print(line.strip())
	except FileNotFoundError:
		print('error')

history_list = []
pages_list = []
dir_name = "tb_tabs"
text_list = {'nytimes.com': nytimes, 'bloomberg.com': bloomberg}
menu()
