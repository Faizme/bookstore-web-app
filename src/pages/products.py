import streamlit as st

def show():
    st.header("Products")
    st.write("Here are our products.")
    
    # Product listings
    products = [
        {"name": "Rich Dad Poor Dad", "price": "$7.99", "image": "https://tse2.mm.bing.net/th?id=OIP.jOL5WCWxJlLsoNWaXsRBPQHaHa&w=200&h=200&c=7"},
        {"name": "The Psychology of Money", "price": "$11.49", "image": "https://tse2.mm.bing.net/th?id=OIP.uidb0PeUPjki837ccO-51QHaHa&w=200&h=200&c=7"},
        {"name": "Atomic Habits", "price": "$16.20", "image": "https://tse3.mm.bing.net/th?id=OIP.40YdU1lR2EQdFRfSxnTERQHaHa&w=200&h=200&c=7"},
        {"name": "The 5 AM Club", "price": "$14.99", "image": "https://tse1.mm.bing.net/th?id=OIP.-FkAx5gsmOcOMEhkIHblMgHaLU&w=200&h=305&c=7"},
        {"name": "Who Will Cry When You Die?", "price": "$6.99", "image": "https://tse2.mm.bing.net/th?id=OIP.PdPn5Xj4vahLtOFZPMIwbAHaJ5&w=200&h=267&c=7"},
        {"name": "Where the Crawdads Sing", "price": "$9.98", "image": "https://tse1.mm.bing.net/th?id=OIP.h1ZkrWQ1gu-ZDl-4T1ymBQHaLp&w=200&h=200&c=7"},
        {"name": "The Silent Patient", "price": "$12.99", "image": "https://tse1.mm.bing.net/th?id=OIP.f4Teqq6WhuhunD_juQ3GCwHaL2&w=200&h=200&c=7"},
        {"name": "Educated", "price": "$13.99", "image": "https://tse3.mm.bing.net/th?id=OIP.Kn8v8LjGkvpgg8BanIjFnAHaLQ&w=200&h=200&c=7"},
        {"name": "Becoming", "price": "$11.89", "image": "https://tse3.mm.bing.net/th?id=OIP.e__NEYvJpiqMPy4lAR_zHgHaLQ&w=200&h=200&c=7"},
        {"name": "The Nightingale", "price": "$10.29", "image": "https://tse1.mm.bing.net/th?id=OIP.X6eefV_yCkswDyKZu50U_AHaLH&w=200&h=200&c=7"},
        {"name": "The Alchemist", "price": "$8.99", "image": "https://tse1.mm.bing.net/th?id=OIP.CP_1Cu_o_riUJ-gnUWz6DwHaLX&w=200&h=200&c=7"},
        {"name": "Sapiens: A Brief History of Humankind", "price": "$14.29", "image": "https://tse2.mm.bing.net/th?id=OIP.U7Cgx-f0lhA5IKBUL8viFgHaLX&w=200&h=200&c=7"},
        {"name": "The Subtle Art of Not Giving a F*ck", "price": "$12.99", "image": "https://tse4.mm.bing.net/th?id=OIP.2oSAsLprWg9L17YnE2uIgQHaHa&w=200&h=200&c=7"},
        {"name": "The Tattooist of Auschwitz", "price": "$9.99", "image": "https://tse3.mm.bing.net/th?id=OIP.Pg9WMZ2ysiauH-eO8syshQHaLO&w=200&h=200&c=7"},
        {"name": "Little Fires Everywhere", "price": "$11.59", "image": "https://tse4.mm.bing.net/th?id=OIP.MnttOv1RbtokPddJVX5jfwHaLo&w=200&h=200&c=7"},
    ]

    
    for product in products:
        st.image(product["image"], caption=product["name"])
        st.write(f"Price: {product['price']}")
        if st.button("Add to Cart", key=product["name"]):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")