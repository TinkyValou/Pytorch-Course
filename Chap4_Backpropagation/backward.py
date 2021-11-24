import torch

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0,requires_grad=True)

#forward pass and compute the loss
y_hat = x*w
s = y_hat - y
loss = s**2

print(loss)

#backward pass

loss.backward()
print(w.grad)