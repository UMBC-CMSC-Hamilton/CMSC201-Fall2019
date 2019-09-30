print(17/5)
x = 5
x **= 30
print(x)

x = 5
x += 1
x = x + 1
print(x)

y = 15
y = y * 3
y *= 3

z = 1; w = 4
print(z / w)

print(15 / 3)  # 5.0, note that this is floating point
print(type(15/3))

print(18 // 3)  # integer division yields an integer
# But what about 19 // 3?
print(19//3)  # This is also 6, because we drop remainders in integer division
print(-5 // 3)  # what should happen here? This yields -2.
print(5 // -3)

print(17 % 5, 3 % 1, 15 % 5, 343 % 15)  # 2 0 0 13
print(2 % 5, -2 % 5)  # 2 3

print(3 * 19 % 7 * 2)

# comparison operators
print('Comparisons')
print(3 < 5)
print(5 < 3.9)
# string tests
print("hello" < "variable")
print("A" > "B")
print("Z" < "a")
#
print('testing equality')
print(3 == 3.0)
print("hello" == 'hello')
print("asdf" != 'hello')

#logical operators
a = True ; b = False ; c = True
print(a and (b or c))
print(not a or not b)
print(not (a or b) and not(a or c))
print(not b and c)

# demorgan's laws
print(not (a or b) == (not a and not b))
print(not (a and b) == (not a or not b))

conditional_statement = True
code_block = 1
code_after = 1

if conditional_statement:
    code_block

code_after

true_or_false_condition = True or False
if true_or_false_condition:
    print('the condition is true')
print('this will print regardless')

if x % 2 == 0:
    print('x is an even number')

entered_string = 'hello there'
if entered_string != 'quit':
    x += 1
    print('hello')

execute_code = True

if __name__ == '__main__':
    execute_code

if conditional_statement:
    execute_code
if not conditional_statement:
    execute_code

if x % 2 == 0:
    print('the number is even')
else:
    print('the number is odd')

s = 'hello there'
s = input('Enter a non-empty string! ')
if s:
    print('you\'ve entered a non-empty string')
else:
    print('You had one job...')

temperature = 50
if temperature < 32:
    print('we are freezing here')
elif temperature < 212:
    print('it is some temperature')
else:
    print('it\'s boiling in here, literally')

n = 15
if n == 1:
    print('the number is one')
elif n == 2:
    print('the number is two')
elif n == 3:
    print('the number is three')
elif n == 4:
    print('the number is four')
else:
    print('who knows what the number is, we certainly don\'t')

s = 's'

s.isupper()
