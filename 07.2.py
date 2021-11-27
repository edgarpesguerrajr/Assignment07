def PasswordCheck(password):
	
	SpecialSymbol =['!', '”', '#', '$', '%', '&', '’', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '|', ']', '^', '_', '`', '}', '{', '~']
	val = True 
	
	if len(password) < 16:
		val = False
		
	if not any(char.isdigit() for char in password):
		val = False
		
	if not any(char.isupper() for char in password):
		val = False

	if not any(char in SpecialSymbol for char in password):
		val = False
	if val:
		return val

def Main():
	password = input('Enter your password :')

	if (PasswordCheck(password)):
		print("Password is valid")
	else:
		print("Invalid Password")
				
if __name__ == '__main__':
	Main()