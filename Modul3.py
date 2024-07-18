#ćwiczenie 1
numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0
for i,n in enumerate(numbers):
    x = n//10
    y = 10 if n%10 >= 5 else 0
    numbers[i] = x*10 + y
print(numbers)
numbers.remove(min(numbers))
numbers.remove(max(numbers))
print(numbers)
mean_number = sum(numbers) / len(numbers)
print(mean_number)
#ćwiczenie 2
input(print("podaj"))
def build_bridge(chunk, goal):
  junction = chunk / 2
  x = (goal + (junction * 1))/(chunk + junction)
  return True if x.is_integer() else False