#python姿势学习

剔除一个字符串中的元音字母

~~~
Sample:
in		"Hello World"
out		"Hll wrld"
~~~

~~~python
我的姿势
def disemvowel(string):
	return filter(lambda ch:ch.lower() not in 'aeiou', string)

偷学来的
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
~~~

求各位数字的合

~~~
sample
in 		"19"
out		"10"
in		"-12"
out		"3"
~~~

~~~python
我的姿势
def sumDigits(number):
	return int(reduce(lambda x,y:str(int(x)+int(y)),str(number)))
	
偷学来的
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))
~~~


把数字的每位分割开来

~~~
sample
123 => [1,2,3]

1 => [1]

8675309 => [8,6,7,5,3,0,9]
~~~

~~~python
我的姿势
def digitize(n):
	L = []
	[L.append(int(i)) for i in str(n)]
	return L
	
偷学来的
def digitize(n):
    return [int(d) for d in str(n)]

def digitize(n):
  return map(int, str(n))
~~~

Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.

~~~python
我的姿势
def shorter_reverse_longer(a,b):
    shorter = a if len(a) < len(b) else b
    longer = a if len(a) >= len(b) else b
    return shorter + longer[::-1] + shorter
    
偷学来的
def shorter_reverse_longer(a,b):
  if len(a) < len(b): a, b = b, a
  return b+a[::-1]+b
 
def shorter_reverse_longer(a,b):
    return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a
~~~

Given two arrays of strings a1 and a2 return a sorted array in lexicographical order and without duplicates of the strings of a1 which are substrings of strings of a2.

Example: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Note: Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

~~~python
我的姿势
def in_array(array1, array2):
    L = []
    for t in array1:
        if any(map(lambda each:t in each,array2)):
            L.append(t) 
    return sorted(list(set(L)))

偷学来的
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
~~~