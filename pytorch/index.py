# import torch

# x = torch.tensor(2.0, requires_grad=True)

# y = x ** 2

# y.backward()


# print(x.grad)


# import torch
# import torch.nn as nn

# class SimpleNN(nn.Module):
#   def __init__(self):
#     super().__init__()

#     self.fc1 = nn.Linear(2,4)
#     self.fc2 = nn.Linear(4,1)
  
#   def forware(self,x):
#     x = torch.relu(self.fc1(x))
#     x = self.fc2(x)
#     return x



# model = SimpleNN()
# print(model)


import torch
import torch.nn as nn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load data
iris = load_iris()
X = torch.tensor(iris.data, dtype=torch.float32)
y = torch.tensor(iris.target, dtype=torch.long)

# 2. Split + normalize
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = torch.tensor(scaler.fit_transform(X_train), dtype=torch.float32)
X_test  = torch.tensor(scaler.transform(X_test),      dtype=torch.float32)

# 3. Define model
class IrisNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 16),   # 4 features → 16 hidden neurons
            nn.ReLU(),
            nn.Linear(16, 3)    # 16 → 3 classes
        )

    def forward(self, x):
        return self.net(x)

model = IrisNet()

# 4. Loss + optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 5. Training loop
for epoch in range(200):
    model.train()
    optimizer.zero_grad()       # clear old gradients
    output = model(X_train)     # forward pass
    loss = criterion(output, y_train)  # compute loss
    loss.backward()             # backprop → compute gradients
    optimizer.step()            # update weights

    if (epoch + 1) % 20 == 0:
        model.eval()
        with torch.no_grad():
            preds = model(X_test).argmax(dim=1)
            acc = (preds == y_test).float().mean()
        print(f"Epoch {epoch+1}: loss={loss.item():.4f}, acc={acc.item()*100:.1f}%")

print("Done!")