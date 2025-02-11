import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZjYzYmQ1NDA1ZTdmYzE3MmMwNzAwODY2OWU0NTlmNCIsIm5iZiI6MTcxNzg1NTkxMy41NDEsInN1YiI6IjY2NjQ2NmE5OTI4ZDE5OGE1YzgyNWEzNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OnAtEfxpcfF-JJ4DHy_WFW_aWIAlIKs0VhYKhdWkZiI"
    }
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US', headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']

# Function to recommend movies
def recommend(selected_movie_name, num_recommendations):
    movie_index = movies[movies['Title'] == selected_movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:num_recommendations + 1]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].Title)
        movie_id = movies.iloc[i[0]].ID
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('model/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

def main():
    st.set_page_config(layout="wide", page_title="Movie Recommender System", page_icon="??")

    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF;
            color: #333333;
        }
        .stButton button {
            background-color: #2196F3;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #1976D2;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            text-align: center;
            color: #2196F3;
        }
        .stImage {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .stImage:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .stSidebar {
            background-color: #F5F5F5;
            padding: 20px;
        }
        .chatbot-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align: center; font-size: 36px; font-weight: bold; color: #2196F3;">
             Movie Recommender System
        </div>
        <div style="text-align: center; font-size: 18px; color: #666;">
            Discover your next favorite movie!
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    # Sidebar for chatbot and dark/light mode toggle
    # with st.sidebar:
    #     st.markdown("### ?? Chatbot")
    #     if st.button("Open Chatbot"):
    #         st.session_state.chat_open = True

    #     st.markdown("### ?? Dark/Light Mode")
    #     dark_mode = st.checkbox("Enable Dark Mode")

    # # Apply dark mode
    # if dark_mode:
    #     st.markdown(
    #         """
    #         <style>
    #         body {
    #             background-color: #0E1117;
    #             color: white;
    #         }
    #         </style>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # Main content
    col1, col2 = st.columns([1, 2])

    with col1:
        selected_movie_name = st.selectbox(
            'Select a Movie to Get Recommendations',
            movies['Title'].values,
            help="Choose a movie you like to get personalized recommendations."
        )
    with col2:
        num_recommendations = st.slider(
            'Number of Recommendations',
            min_value=5,
            max_value=20,
            value=5,
            help="Adjust the number of movie recommendations."
        )

    if st.button('Get Recommendations'):
            st.session_state.show_recommendations = True

    if st.session_state.get("show_recommendations", False):
        with st.spinner("Fetching recommendations..."):
            titles, posters = recommend(selected_movie_name, num_recommendations)
            st.success("Recommendations ready!")

        st.divider()
        st.markdown(
            f"""
            <div style="text-align: center; font-size: 24px; font-weight: bold; color: #2196F3;">
                Top Recommendations Based on "{selected_movie_name}"
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Display selected movie
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"<div style='text-align: center;'><h3>{titles[0]}</h3></div>", unsafe_allow_html=True)
            st.image(posters[0], width=300, use_container_width=True)

        # Display recommended movies in a grid
        with col2:
            st.markdown("<div style='text-align: center;'><h3>Recommended Movies for You</h3></div>", unsafe_allow_html=True)
            movies_per_row = 4  # Adjust based on your preference
            for i in range(1, len(titles), movies_per_row):
                cols = st.columns(movies_per_row)
                for j, col in enumerate(cols):
                    if i + j < len(titles):
                        with col:
                            st.image(posters[i + j], use_container_width=True)
                            st.markdown(
                                f"""
                                <div style="text-align: center; font-size: 16px; font-weight: bold; color: inherit;">
                                    {titles[i + j]}
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

        # Footer
        st.divider()
        st.markdown(
            """
            <div style="text-align: center; font-size: 18px; font-weight: bold;">
                Discover more movies by exploring our app!
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div style="text-align: center; font-size: 18px; color: #666;">
                Select a movie and press "Get Recommendations" to start.
            </div>
            """,
            unsafe_allow_html=True,
        )

# Run the app
if __name__ == "__main__":
    main()