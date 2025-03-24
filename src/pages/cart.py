import streamlit as st

def show():
    st.header("Cart")
    
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    
    if len(st.session_state.cart) == 0:
        st.write("Your shopping cart is empty.")
    else:
        total = 0
        for item in st.session_state.cart:
            st.write(f"{item['name']} - {item['price']}")
            total += float(item['price'][1:])
        st.write(f"Total: ${total}")
        if st.button("Proceed to Checkout"):
            st.session_state.checkout_total = total
            st.session_state.page = "Checkout"
            st.session_state.rerun = True

    if 'rerun' in st.session_state and st.session_state.rerun:
        st.session_state.rerun = False
        st.rerun()