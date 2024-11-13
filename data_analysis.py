import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def monthly_spending(self):
        # Extrair informações de gastos mensais e plotar um gráfico de barras
        self.data['Purchase Month'] = pd.to_datetime(self.data['Purchase Dates'].str[0]).dt.to_period('M')
        monthly_spending = self.data.groupby('Purchase Month')['Annual Income'].sum()
        fig, ax = plt.subplots()
        monthly_spending.plot(kind='bar', ax=ax)
        ax.set_title('Total Spending per Month')
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Spending')
        return fig

    def demographic_analysis(self):
        # Análise de gastos por faixa etária e sexo
        self.data['Age Group'] = pd.cut(self.data['Age'], bins=[0, 20, 30, 40, 50, 60, 100], labels=['0-20', '21-30', '31-40', '41-50', '51-60', '60+'])
        fig, ax = plt.subplots()
        sns.countplot(data=self.data, x='Age Group', hue='Gender', ax=ax)
        ax.set_title('Demographics by Age Group and Gender')
        ax.set_xlabel('Age Group')
        ax.set_ylabel('Number of Customers')
        return fig

    def ticket_average(self):
        # Ticket médio por compra
        fig, ax = plt.subplots()
        self.data['Ticket Average'] = self.data['Annual Income'] / self.data['Purchase Dates'].apply(len)
        sns.histplot(self.data['Ticket Average'], kde=True, ax=ax)
        ax.set_title('Ticket Average Distribution')
        ax.set_xlabel('Average Ticket Value')
        return fig