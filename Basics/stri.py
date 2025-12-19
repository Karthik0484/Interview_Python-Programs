'''1️⃣ Email Generator & Validator (VERY COMMON)

Scenario:
You are building a company onboarding system.

Task:
Take a full name as input (can contain extra spaces, mixed case).
Generate a corporate email in the format:
firstname.lastname@company.com

Conditions:
Remove extra spaces
Convert to lowercase
Validate that the name contains only alphabets and spaces

📌 Used in HR systems, onboarding tools '''

name = input("Enter your name: ").strip()

# Clean spaces in the name
clean_name = name.replace(" ","")

#validate and generate the email
if clean_name.isalpha():
    email = clean_name.lower()+"@company.com"
    print(email)

else:
     print("Enter valid name")

''' 2️⃣ Password Strength Checker
Scenario:
Used in login/signup pages.

Task:
Check if a password is valid based on rules:
Minimum length: 8

Must contain:
at least one digit
at least one uppercase letter
at least one lowercase letter
Must NOT contain spaces

📌 Asked in almost every product-based company'''

password = input("Enter your password: ")

has_digit = False
has_upper = False
has_lower = False
has_space = False

if len(password) < 8 :
    print("Length of password must be atleast 8.")

else:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch.islower():
            has_lower = True
        elif ch == " ":
            has_space = True

    if has_upper and has_lower and has_digit and not has_space:
            print("Password is Strong.")

    else:
        print("Password is not strong.")

''' 3️⃣ URL Validator

Scenario:
Backend validation before saving URLs to database.

Task:
Write a program that checks whether a given URL:

Starts with http:// or https://
Ends with .com or .in
Has no spaces
📌 Real backend interview question '''

url= input("Enter your url: ")

if (url.startswith("http://") or url.startswith("https://")) and \
    (url.endswith(".com") or url.endswith(".in")) and \
    (" " not in url):
    print("valid url.")

else:
    print("Invalid url.")

''' 4️⃣ User Input Cleanup System

Scenario:
User enters messy data into a form.

Input Example:
"   Python,  Java ,C++,  JavaScript   "

Task:

Remove extra spaces
Convert all values to lowercase
Convert the string into a clean list:
['python', 'java', 'c++', 'javascript']

📌 Used in filters, search engines '''

skills = input("Enter your skills: ")

clean_skills = skills.lower().strip().split(",")

final_skills = []
for skill in clean_skills:
    final_skills.append(skill.strip())

print(final_skills)


