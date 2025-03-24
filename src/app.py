import streamlit as st
from chatbot import Chatbot

if 'cart' not in st.session_state:
    st.session_state.cart = []

if 'checkout_total' not in st.session_state:
    st.session_state.checkout_total = 0

if 'page' not in st.session_state:
    st.session_state.page = "Home"

def main():
    st.title("E-Commerce Web Application")
    st.sidebar.title("Navigation")
    
    pages = {
        "Home": "home",
        "Products": "products",
        "Cart": "cart",
        "Checkout": "checkout"
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(st.session_state.page))
    st.session_state.page = selection
    
    if selection == "Home":
        import pages.home as home
        home.show()
    elif selection == "Products":
        import pages.products as products
        products.show()
    elif selection == "Cart":
        import pages.cart as cart
        cart.show()
    elif selection == "Checkout":
        import pages.checkout as checkout
        checkout.show()
    
    st.sidebar.title("Chatbot")
    chatbot = Chatbot()
    user_input = st.sidebar.text_input("Ask me anything about our store:")
    
    if user_input:
        response = chatbot.get_response(user_input)
        st.sidebar.text_area("Chatbot Response", value=response, height=200)

if __name__ == "__main__":
    main()