import streamlit as st

# Class to generate multiple Streamlit pages using an object oriented approach
class Multipage:
    def __init__(self,app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()