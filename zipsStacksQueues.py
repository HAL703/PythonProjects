list1 = [1,2,3]
list2 = [4,5,6]

#To COMBINE these lists

print(list(zip(list1, list2)))


#LAST IN FIRST OUT - STACKS

browsing_session = []
browsing_session.append[1]
browsing_session.append[2]
browsing_session.append[3]
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("Disable")
#Basically imagine the back buttons in a browser

#FIRST IN FIRST OUT

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("EMPTY")