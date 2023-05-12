import matplotlib.pyplot as plt

x_values = []
y_values = []

n = int(input('Please insert num '))
for x in range(n):
    num1 = int(input('Please insert time '))
    x_values.append(num1)
    num2 = int(input('Please insert frequency' )) 
    y_values.append(num2)
    
plt.plot(x_values, y_values)

plt.xlabel('ms')
plt.ylabel('Hz')
plt.title('frequency value')

plt.show()
