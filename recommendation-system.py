import streamlit as st
import pandas as pd

@st.cache
def load_data():
    return pd.read_csv('book_data.csv')


def main():
    st.title('Book Recommendation System')


    data = load_data()


    st.subheader('Scraped Book Data')
    st.write(data)


    st.subheader('Recommendations')
    selected_title = st.selectbox('Select a book:', data['Title'])
    st.write('You selected:', selected_title)
    recommended_books = data[data['Title'] != selected_title].sample(5)
    st.write('Recommended books:')
    st.write(recommended_books[['Title', 'Author', 'Rating']])


if __name__ == "__main__":
    main()
