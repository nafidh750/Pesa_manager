import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Function to generate business performance charts
def generate_performance_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['profit_loss'], marker='o', linestyle='-', color='gold', label='Profit/Loss')
    plt.xlabel('Date')
    plt.ylabel('Profit/Loss')
    plt.title('Business Performance Over Time')
    plt.legend()

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64
    graph = base64.b64encode(image_png).decode('utf-8')
    return graph
