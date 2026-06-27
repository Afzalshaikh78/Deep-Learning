import torch.nn as nn

lstm = nn.LSTM(
  input_size=10,
  hidden_size=20,
  num_layesr = 1
)