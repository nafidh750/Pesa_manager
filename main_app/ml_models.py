import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Define the model using PyTorch
class BusinessPerformanceModel(nn.Module):
    def __init__(self, input_size):
        super(BusinessPerformanceModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Function to create and train the model using PyTorch
def create_business_performance_model(data):
    # Preparing the dataset
    X = data[['capital', 'daily_sales']].values  # Features: capital, daily sales
    y = data['profit_loss'].values  # Target: profit/loss

    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Convert data to PyTorch tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

    # Defining the model
    input_size = X_train_tensor.shape[1]
    model = BusinessPerformanceModel(input_size)

    # Define loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training the model
    epochs = 50
    batch_size = 10
    for epoch in range(epochs):
        model.train()
        permutation = torch.randperm(X_train_tensor.size()[0])

        for i in range(0, X_train_tensor.size()[0], batch_size):
            indices = permutation[i:i+batch_size]
            batch_X, batch_y = X_train_tensor[indices], y_train_tensor[indices]

            optimizer.zero_grad()  # Clear gradients
            outputs = model(batch_X)  # Forward pass
            loss = criterion(outputs, batch_y)  # Calculate loss
            loss.backward()  # Backpropagation
            optimizer.step()  # Update weights

        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

    # Evaluating the model on the test set
    model.eval()
    with torch.no_grad():
        test_predictions = model(X_test_tensor)
        test_loss = criterion(test_predictions, y_test_tensor)
        print(f"Test Loss: {test_loss.item()}")

    return model, scaler

# Function to use the model for predictions
def predict_performance(model, scaler, capital, daily_sales):
    input_data = np.array([[capital, daily_sales]])
    input_data = scaler.transform(input_data)  # Scale the input data
    input_tensor = torch.tensor(input_data, dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        prediction = model(input_tensor)
    return prediction.item()
