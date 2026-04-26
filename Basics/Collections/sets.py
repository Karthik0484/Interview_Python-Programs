'''🔹 SET – Interview Questions
Q8. Remove Duplicate Emails
You receive email IDs from two sources:
emails_day1 = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
emails_day2 = ["b@gmail.com", "d@gmail.com"]

Find:
All unique emails
Emails received on both days'''
emails_day1 = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
emails_day2 = ["b@gmail.com", "d@gmail.com"]

set1 = set(emails_day1)
set2 = set(emails_day2)

unique_emails = set1 | set2
common_emails = set1 & set2

print("All unique emails: ",unique_emails)
print("Email received on both days: ",common_emails)

'''Q9. Find Missing Numbers
Given:
expected = {1,2,3,4,5,6}
received = {1,2,4,6}

Find missing numbers.'''
expected = {1,2,3,4,5,6}
received = {1,2,4,6}
print(expected - received)

'''Q10. Unique Words Counter
Given a sentence, print number of unique words.
 '''
sentence = "python is easy and python is powerful"
words = sentence.split()
unique = set(words)
print(len(unique))
print(unique)


