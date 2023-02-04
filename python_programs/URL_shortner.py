import pyshorteners

long_url = input("Enter your URL link : ")

short_string = pyshorteners.Shortener()

short_url =  short_string.tinyurl.short(long_url)

print(short_url)

