import logging as log
import hashlib
import getpass
import datetime
import os

log.basicConfig(format='%(levelname)s: %(message)s', level=log.INFO)

# Configure application log level
if 'LOG_LEVEL' in os.environ and os.environ['LOG_LEVEL'] == 'INFO':
    log_level = log.INFO
elif 'LOG_LEVEL' in os.environ and os.environ['LOG_LEVEL'] == 'DEBUG':
    log_level = log.DEBUG
elif 'LOG_LEVEL' in os.environ:
    log.error('Value for environment variable "LOG_LEVEL" must be either "INFO" or "DEBUG"')
    exit(1)
else:
    log_level = log.INFO

log.getLogger().setLevel(log_level)

quickhash = {
	#save location and salt generation
	path = "../hashbank/hashbank.txt"
	salt = input("Press enter to generate salt, or input a salt value: ")
	if salt == "": 
		salt = os.urandom(16)
		binary_representation = ' '.join(format(byte, '08b') for byte in salt)
		print(f'Salt in binary format: {binary_representation}')
	print(f' salt in python byte is: {salt}')
	log.debug(f'Salt is currently: {salt} BUT SOMETHING IS WRONG')

	# ------ set password, either hardcoded 
	passw = "Tuff3-Uff3" 

	# ------ or by input
	# passw = getpass.getpass(prompt='Password to hash: ', stream=None)
	# COMBINE W ------ easy random password gen  
	# passw = getpass.getpass(prompt='Password to hash: ', stream=None)
	# if passw == "": 
	#	passw = os.urandom(16)

	hashVers = input("You want sha256(default), sha384, or sha512?: ") 
	if hashVers not in ["sha256", "sha384", "sha512"]:
	    hashVers = "sha256"
	print(f'type of hash: {hashVers}')
	hashed_password = hashlib.pbkdf2_hmac(hashVers, passw.encode("utf-8"), salt, 100000).hex()
	print(f' hash is : {hashed_password}')
	print(f' salt is: {salt}')


	qSaveQ = input("Do you want to save that to the hashbank? \ny/N ")
	if qSaveQ == "n":
		print("Ok cool, remember to copy paste that")

	if qSaveQ == "y":
		print("ait then, we're saving it in the format: this_time - hash, salt, byte version of salt)")
		f = open("../hashbank/hashbank.txt", "a")
		f.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {hashed_password}, {salt} \n')

		f.close()

}
# END QUICKHASH