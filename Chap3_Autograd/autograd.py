import torch

# x = torch.randn(3, requires_grad=True)
x = torch.ones(3, requires_grad=True)
print("\nx :")
print(x)

y = x + 1

print("\ny :")
print(y)

z = y * y * 2
z = z.mean()  # Essential if we use 'backward' after

print("\nz :")
print(z)

z.backward()  # dz/dx
print("\nx.grad :")
print(x.grad)
print("\n\n")

# *******************************************
'''
x = torch.randn(3,requires_grad=True)
print(x)
'''

# Pour retirer le requires_grad (il ne sera plus visible lors du print de la matrice)

# x.requires_grad_(False)
# x.detach()
# with torch.no_grad():
#    y = x+2
#    print(y)

# *******************************************

weights = torch.ones(4, requires_grad=True)

for epoch in range(3):
    print("\n1:")
    model_output = (weights * weights * 2).sum()
    print((weights * 2))
    print("2:")

    model_output.backward()

    print(weights.grad)

if __name__ == '__main__':
    print("Hello World")