import torch.nn as nn

model = nn.Sequential(

    nn.Conv2d(3, 32, kernel_size=3),

    nn.ReLU(),

    nn.MaxPool2d(2),

    nn.Conv2d(32, 64, kernel_size=3),

    nn.ReLU(),

    nn.MaxPool2d(2),

    nn.Flatten(),

    nn.Linear(64 * 6 * 6, 128),

    nn.ReLU(),

    nn.Linear(128, 10)
)



model.eval()
