blacklist = ["spam1@xyz.com", "fraud2@abc.com", "junk3@mail.com"]

def check_spam(email):
    for item in blacklist:
        if item == email:
            return True
    return False

email = "fraud2@abc.com"
if check_spam(email):
    print(email, "is SPAM")
else:
    print(email, "is safe")
