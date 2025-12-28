'''🔹 MIXED (LIST + SET + DICT) – REAL INTERVIEW LEVEL
Q1. Recommendation Engine

You are given:
user1 = {"python", "sql", "java"}
user2 = {"python", "django", "sql"}

Find:
Common skills
Skills unique to each user'''

user1 = {"python", "sql", "java"}
user2 = {"python", "django", "sql"}

common_skills = user1.intersection(user2)
print(common_skills)

uniques_skills = user1.difference(user2)
print("User1 unique skills: ",uniques_skills)

uniques_skills2 = user2.difference(user1)
print("User2 unique skills: ",uniques_skills2)

'''Q2. Word Frequency Analyzer
Given a paragraph, return top 2 most frequent words.'''

paragraph = 'a part of a piece of writing that consists of one or more sentences. A paragraph always starts on a new line.'
para = paragraph.split()
frequency={}

for n in para:
    if n in frequency:
        frequency[n] = frequency[n]+1
    else:
        frequency[n] = 1
print(frequency)

'''Q3. Remove Invalid Records
Given:
data = [{"name": "Alice", "age": 20},{"name": "Bob"},{"age": 25},{"name": "Charlie", "age": 22}]
Remove invalid records (missing name or age).'''

data = [{"name": "Alice", "age": 20},{"name": "Bob"},{"age": 25},{"name": "Charlie", "age": 22}]
valid_record = []

for record in data:
    if "name" in record and "age" in record:
        valid_record.append(record)

print(valid_record)

'''Q4. Group Data
Group students by grade using a dictionary of lists.'''

students = {"Karthik":90,"Allen":80,"David":60,"Bob":64}
grouped_data={"A":[],"B":[],"C":[]}

for name,marks in students.items():
    if marks >= 90:
        grouped_data["A"].append(name)
    elif marks >=75:
        grouped_data["B"].append(name)
    else:
        grouped_data["C"].append(name)

print(grouped_data)

'''Q5. First Non-Repeating Character
Given a string, find the first non-repeating character.
s = "programming"'''

s = "programming"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch]==1:
        print("First Non-Repeating Character:", ch)
        break

'''Q6. Real-Time Log Analyzer

Given:
logs = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR"]
Create a dictionary showing count of each log type.'''

logs = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR"]
count = {}

for i in logs:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)








