from IC_Car import Address
a = Address('2500', 'University Drive', 'Some City', 'Some State', '12345')
b = Address('12-1200', 'College Blvd', 'Other City', 'Other State', '99102')

print("Address a is:")
a.run()
print("\nAddress b is:\n")
b.run()

if a.before(b):
    print("a comes before b is",a.before(b))
else:
    print("b comes before a is",b.before(a))