import streamlit as st
import pickle
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import pickle
import pandas

user_sim_df = pickle.load(open('recommend_new_nation.pkl','rb'))
final_ratings=pickle.load(open('data_new_file.pkl','rb'))
st.title('Book recommendation app')

#userid= st.selectbox(label="User-ID",options=final_ratings["User-ID"].unique())
userid = st.sidebar.number_input("Enter User id")


try:
#if(userid in final_ratings['User-ID']):
    tem=list(user_sim_df.sort_values([userid],ascending=False).head(5).index)
    print(tem)
    book_list=[]
    url_list=[]
    for i in tem:
        book_list=book_list+list(final_ratings[final_ratings["User-ID"]==i]['Book-Title'][1:3])
        url_list=url_list+list(final_ratings[final_ratings["User-ID"]==i]['Image-URL-M'][1:3])
        #print(book_list)
    read_books=list(final_ratings[final_ratings['User-ID']==userid]['Book-Title'][1:8])
    read_urls=list(final_ratings[final_ratings['User-ID']==userid]['Image-URL-M'][1:8])
    for i in read_books:
        if i in book_list:
            book_list.remove(i)
    for i in read_urls:
        if i in url_list:
            url_list.remove(i)
    st.subheader("Books already read by the user")
    for i in enumerate(read_books):
        st.write(i[1])
        st.image(read_urls[i[0]])


    st.subheader("Recommended books")
    for i in enumerate(book_list):
        st.write(i[1])
        st.image(url_list[i[0]])
except:
#else:
    #st.write("Enter valid user id")
    dataset = pickle.load(open('popular_dataset.pkl', 'rb'))
    popular_books = pickle.load(open('Popularity_based.pkl', 'rb'))

     #Keeping only one entry of each book
    popular_books = popular_books.sort_values('Score', ascending=False).drop_duplicates('Book-Title').sort_index()
    #cm = sns.light_palette('yellow', as_cmap=True)
    #Sorting books based on score calculated above
    popular_books = popular_books.sort_values('Score', ascending=False)

    # Printing the top 20 books
    a=popular_books[['Book-Title', 'Total_No_Of_Users_Rated', 'Avg_Rating', 'Score']].reset_index(drop=True).head()
    st.subheader("Recommendations")
    for i in enumerate(a['Book-Title']):
        st.write(i[1])
        st.image(dataset[dataset['Book-Title']==i[1]]['Image-URL-M'].iloc[0])
    


