##
# Algorithms
#
#	1. What is a url ? A series of character following 'https://' needs to parse the url
#	2. Generating random hash from series of characters and store their relationship with dictionary
#	3. How many strings do we foresee? 36^6
#	4. Handling invalid url by checking if the string is considered a url.
#
##
import random, hashlib
class url_shortener:
	hex_value = "0123456789abcdef"
	list = {}
	urls = []

	def detect_url(self, string):
		if ("https://" in string) or ("http://" in string):
			print("Found string")
		else:
			print("String not found")

	def hash_value(self, url):
		hashvalue = ""
		hash_object = hashlib.sha256(url)
		hex_dig = hash_object.hexdigest()
		print(hex_dig)
		return hashvalue


	def get_from_file(self):
		with open("./url_file.txt") as file:
			for line in file:
				hashvalue = self.hash_value(line.strip())
				self.list[] = f"https://short.ly/{hashvalue}"

def main():
	test = url_shortener()
	test.get_from_file()
	#print(test.list)
	print(test.list["https://example.com/some/long/path"])

main()
