Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [1]
[1]
>>> [1,2,3]
[1, 2, 3]
>>> []
[]
>>> [True,True,True]
[True, True, True]
>>> ["Python", "Django"]
['Python', 'Django']
>>> ["Yoana ", "Georgieva ", "Radeva"]
['Yoana ', 'Georgieva ', 'Radeva']
>>> ["Ani", "Tedi", "Ivan", "Maria", "Alex"]
['Ani', 'Tedi', 'Ivan', 'Maria', 'Alex']
>>> ["Python", "C++"]
['Python', 'C++']
>>> languages = ["Python", "Ruby"]
>>> languages = languages + ["Ruby", "C++", "Java", "C#"]
>>> languages
['Python', 'Ruby', 'Ruby', 'C++', 'Java', 'C#']
>>> languages = languages = ["Python", "Ruby"]
>>> languages = languages +["C++", "Java", "C#"]
>>> languages
['Python', 'Ruby', 'C++', 'Java', 'C#']
>>> languages = ["Haskell"] + languages
>>> languages
['Haskell', 'Python', 'Ruby', 'C++', 'Java', 'C#']
>>> languages = languages + ["Go"]
>>> languages
['Haskell', 'Python', 'Ruby', 'C++', 'Java', 'C#', 'Go']
>>> languages[0]
'Haskell'
>>> languages[1]
'Python'
>>> languages[4]
'Java'
>>> languages[5] = "F#"
>>> languages
['Haskell', 'Python', 'Ruby', 'C++', 'Java', 'F#', 'Go']
>>> len(languages)
7
>>> languages[6]
'Go'
>>> "Haskell" in languages
True
>>> "Ruby" in languages
True
>>> "Go" in languages
True
>>> "Rust" in languages
False
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = [1]
>>> d = [8, 8, 10]
>>> a + b + c + d
[1, 2, 3, 4, 5, 6, 1, 8, 8, 10]
>>> a + b
[1, 2, 3, 4, 5, 6]
>>> c + d
[1, 8, 8, 10]
>>> a + a
[1, 2, 3, 1, 2, 3]
>>> 
