import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# List of your Excel files for each season
file_names = ["C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2016.xlsx", "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2017.xlsx", "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2018.xlsx", "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2019.xlsx", "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2020.xlsx", "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2021.xlsx", "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2022.xlsx"]

# Load and concatenate data from all sheets into one DataFrame
col_to_keep = ['ESPN Quarterback Rating', 'Net Total Yards','Sacks','3rd down %','Total Penalty Yards','Turnover Ratio','Total Sacks','Total Points','Stuffs','Defensive Touchdown','Passes Defended','Win Totals']
dfs = [pd.read_excel(file)[col_to_keep] for file in file_names]

#Columns not consistent in all spreadsheets
#.drop(columns=["Red Zone Touchdown Percentage","Red Zone Scoring Percentage","Red Zone Field Goal Percentage","Red Zone Efficiency Percentage","Two Point Pass Attempts","Two Point Pass","Two Point Pass Conversions", "Average Gain","Unnamed: 0"])for file in file_names]

df = pd.concat(dfs, ignore_index=True)
df = df.dropna(axis=0, how='all')

print(df)

#Data Preprocessing
features = df.drop('Win Totals', axis=1)
target = df['Win Totals']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Setting up Neural Network

class NFLPredictor(nn.Module):
    def __init__(self, input_dim):
        super(NFLPredictor, self).__init__()
        self.fc1 = nn.Linear(input_dim, 15)
        self.fc2 = nn.Linear(15, 1)
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        return self.fc2(x)

#Training the network

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

input_dim = X_train.shape[1]
model = NFLPredictor(input_dim).to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32).to(device)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).unsqueeze(1).to(device)

num_epochs = 7500
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
        


#Model Evaluation

model.eval()  # Set the model to evaluation mode

# Convert test data to tensor
X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(device)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).unsqueeze(1).to(device)

# Predict on test set
predictions = model(X_test_tensor)

# Calculate loss on test set
test_loss = criterion(predictions, y_test_tensor)
print(f"Test Loss: {test_loss.item():.4f}")


#New Pedictions
# Assuming you have loaded the model and the scaler from previous training

# Load the new data for prediction
file_new_season = "C:\\Users\\Sam\\Desktop\\NFL NN\\FullStats\\2015.xlsx"
col_to_keep_new = ['ESPN Quarterback Rating', 'Net Total Yards','Sacks','3rd down %','Total Penalty Yards','Turnover Ratio','Total Sacks','Total Points','Stuffs','Defensive Touchdown','Passes Defended']
df_new_season = pd.read_excel(file_new_season)[col_to_keep_new]

# Drop the target column if it's there, since you're predicting it
input_data_new = df_new_season.drop('Win Totals', axis=1, errors='ignore')  # errors='ignore' ensures it doesn't fail if column is not present

# Preprocess the new data
input_data_scaled_new = scaler.transform(input_data_new)

# Convert the data to a PyTorch tensor
input_tensor_new = torch.tensor(input_data_scaled_new, dtype=torch.float32).to(device)

# Predict with the model
model.eval()  # Set model to evaluation mode
predictions_new = model(input_tensor_new)

# Convert predictions to numpy array
predictions_np_new = predictions_new.cpu().detach().numpy()
print(predictions_np_new)

