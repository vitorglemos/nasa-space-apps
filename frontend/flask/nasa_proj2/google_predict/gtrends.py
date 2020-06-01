import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from matplotlib.pyplot import figure


class AnalyticsData:
    def __init__(self):
        pass

    @staticmethod
    def show(df, title):
        figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
        words = ['Fever', 'Cough', 'Fatigue', 'Diarrhea', 'Headache']
        for word in words:
            plt.plot(df['Date'], df[word], marker="o", label=word)

        plt.xlabel('Data')
        plt.ylabel('Frequencia de Busca')
        plt.title(title)
        plt.legend()
        plt.grid()
        plt.xticks(rotation=90)
        plt.show()
        # plt.savefig(f'data/output_gtrends_f3.png')


if __name__ == "__main__":
    analytics = AnalyticsData()

    f1 = pd.read_csv("data/g1.csv")
    f2 = pd.read_csv("data/g2.csv")
    f3 = pd.read_csv("data/g3.csv")

    analytics.show(f1, 'GoogleTrends - filter 1 - Mundo (H1N1)')
    analytics.show(f2, 'GoogleTrends - filter 2 - Mundo (COVID)')
    analytics.show(f3, 'GoogleTrends - filter 3 - Italia (COVID)')

    st.title('Track Covid-19')
    st.markdown('## When everything may have started: Google')
    st.image('data/output_gtrends_f1.png')
    st.image('data/output_gtrends_f2.png')
    st.image('data/output_gtrends_f3.png')
