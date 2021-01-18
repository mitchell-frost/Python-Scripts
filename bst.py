from BST import *
from student import *

gTotalAges = 0
def AddAges(s):
	global gTotalAges
	gTotalAges += int(s.GetAge())
  
def main():
global gTotalAges
studentList = UUC()

########## Inserting ##########
fin = open("InsertNamesTiny.txt","r")
for line in fin:
words = line.split()
s = Student(words[0], words[1], words[2], words[3], words[4])
ok = studentList.Insert(s)
if not ok:
print("Error inserting", words[1])
fin.close()
print("Students inserted:", studentList.Size())

########## Traversing ##########
studentList.Traverse(AddAges)
ave = gTotalAges / studentList.Size()
print("The average age is",ave)

########## Deleting ##########
  

########## Retrieving ##########
fin = open("RetrieveNamesTiny.txt","r")
totalAge = 0
count = 0
for line in fin:
ssn = line.strip()
s1 = Student("", "", ssn, "", "")
s2 = studentList.Retrieve(s1)
if s2 is None:
print("Error retrieving student with ssn of", ssn)
else:
totalAge += int(s2.GetAge())
count += 1
print("Average age of retrieved student is", totalAge / count)
main()
class Student:
def __init__(self, l, f, s, e, a):
self.mLast = l
self.mFirst = f
self.mSSN = s
self.mEmail = e
self.mAge = a

def GetAge(self):
return self.mAge

def __eq__(self, rhs):
return self.mSSN==rhs.mSSN

def __ne__(self, rhs):
return self.mSSN!=rhs.mSSN

def __lt__(self, rhs):
return self.mSSN   
def __le__(self, rhs):
return self.mSSN<=rhs.mSSN
  
def __gt__(self, rhs):
return self.mSSN>rhs.mSSN
  
def __ge__(self, rhs):
return self.mSSN>=rhs.mSSN

bst

class Node:
def __init__(self, item):
self.mItem = item
self.mL = None
self.mR = None

class UUC:
def __init__(self):
self.mRoot = None

def Insert(self, item): # returns False if item is a duplicate
if self.Exists(item):
return False
n = Node(item)
self.mRoot = self.InsertR(n, self.mRoot)
return True

def InsertR(self, n, current):
if current is None:
current = n
elif n.mItem < current.mItem:
current.mL = self.InsertR(n, current.mL)
else:
current.mR = self.InsertR(n, current.mR)
return current
  
def Exists(self, item): # returns True if found, False otherwise
return self.ExsistsR(item, self.mRoot)
  
def ExistsR(self, item, current):
if current is None:
return False
elif item==current.mItem:
return True
elif item < current.mItem:
return self.ExistsR(item, current.mL)
else:
return self.ExsistsR(item, current.mR)

def Delete(self, item): # return True on success, False otherwise
if not self.Exists(item):
return False
self.mRoot = self.DeleteR(item, self.mRoot)
return True

def DeleteR(self, item, current):
if item < current.mItem:
current.mL = self.DeleteR(item, current.mL)
elif item > current.mItem:
current.mR = self.DeleteR(item, current.mR)
else:
if current.mR is None and current.mL is None:
current = None
elif current.mR is not None and current.mL is None:
current = current.mR
elif current.mL is not None and current.mR is None:
current = current.mL
else:
successor = current.mR
while successor.mL is not None:
successor = successor.mL
current.mItem = successor.mItem
current.mR = self.DeleteR(successor.mItem, current.mR)
return current

def Retrieve(self, item):
return RetrieveR(self, self.mRoot, item)

def RetrieveR(self, current, item):
if current is None:
return current
else:
if item == current.mItem:
return current
elif item < current.mItem:
return self.RetrieveR(self, current.mL, item)
#otherwise retrieve it from right subtree
else:
return self.RetrieveR(self, current.mR, item)

def Size(self):
return self.SizeR(self.mRoot)
  
def SizeR(self, current):
if current is None:
return 0
return 1 + self.SizeR(current.mL) + self.SizeR(current.mR)
  

def Traverse(self, callback):
self.TraverseR(callback, self.mRoot)

def TraverseR(self, callback, current):
if current:
callback(current.mItem)
self.TraverseR(callback, current.mL)
self.TraverseR(callback, current.mR)