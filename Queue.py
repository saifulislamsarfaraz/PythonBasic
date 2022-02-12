from  collections import deque

bank = deque(["anis", "korim", "rohim", "abul","balul"])
bank.popleft()
print(bank)