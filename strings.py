# Q.1 A user is registering on your website and accidentally types their email with extra spaces at the beginning and end: email = "   alex@gmail.com   ". Write a piece of code to clean this input and extract only the valid email ID.
# email = "   alex@gmail.com   "
# print(email.strip())

# Q.2 You are building a secure web crawler. Given a URL string url = "https://xyz.com", write a line of code to verify if the website protocol starts with "https".
# url = "https://xyz.com"
# print(url.startswith("https"))

# Q.3 A Python script needs to clean up server log files. Given the line log_entry = "[ERROR]===System Crash===", write a line of code to strip away only the trailing = characters from the right side.
# log_entry = "[ERROR]===System Crash==="
# print(log_entry.rstrip("="))

# Q.4 A user uploads a file named document = "final_report.pdf". Write a piece of code to check if this file ends with the appropriate ".pdf" extension.
# document = "final_report.pdf"
# print(document.endswith(".pdf"))

# Q.5 You are building a search bar for an e-commerce store. A user searches for "IPHONE", but the database inventory holds the item as "iphone". Write code to convert the user's search string so it matches the database perfectly, regardless of case.
# 

# Q.6 You are designing a text terminal for a checkout counter. The price of an item is price = "450". Write code to right-justify this price inside a 10-character wide block so it aligns perfectly with other receipts.

#  Q.7 A user submits a chat message containing a banned word: msg = "This software has a nasty bug". Write code to automatically replace the word "bug" with the word "feature".
# msg = "This software has a nasty bug"
# print(msg.replace("bug","feature !"))

# Q.8 An API returns a web domain formatted as domain = "www.google.com". Write a single line of code using a strip method to remove the "www." prefix from the left side.
# domain = "www.google.com"
# print(domain.lstrip("www."))

# Q.9 An e-commerce website needs to generate clean URL paths. Given a product title title = "blue running shoes", write code to replace all spaces with dashes (-) to make it look like "blue-running-shoes".
# title = "blue running shoes"
# print(title.replace(" ","-"))

# Q.10 A script reads a secure authentication key from a text file, but it includes an accidental newline character at the end: key = "KEY123XYZ\n". Write a line of code to safely clean this string so only "KEY123XYZ" remains.
key = "KEY123XYZ\n"
print(key.rstrip())