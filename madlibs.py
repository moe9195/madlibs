def main():
	print("Mad libs where libs get mad.")
	time = input("Enter a number from 1 to 12: ")
	item = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	scream = input("Enter any sentence: ")
	action = input("Enter a verb: ")

	print("The story goes... \n\nIt was "+time+" o'clock when I heard a knock at the door.\nI opened the door and there was a box full of "+item+" with a note saying \"From Mr. "+name.title()+".\" \nJust as I closed the door I heard a scream \""+scream.upper()+"\".\nI froze in place and all I could do was "+action+".")




if __name__ == '__main__':
	main()
