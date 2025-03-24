import streamlit as st

def show():
    st.title("Welcome to Our eCommerce Bookstore! 📚")
    
    st.header("📖 Featured Books")
    st.write("Check out our latest books below:")

    books = [
        {"name": "Rich Dad Poor Dad", "price": "$7.99", "image": "https://tse2.mm.bing.net/th?id=OIP.jOL5WCWxJlLsoNWaXsRBPQHaHa&w=200&h=200&c=7"},
        {"name": "The Psychology of Money", "price": "$11.49", "image": "https://tse2.mm.bing.net/th?id=OIP.uidb0PeUPjki837ccO-51QHaHa&w=200&h=200&c=7"},
        {"name": "Atomic Habits", "price": "$16.20", "image": "https://tse3.mm.bing.net/th?id=OIP.40YdU1lR2EQdFRfSxnTERQHaHa&w=200&h=200&c=7"},
    ]

    for book in books:
        st.image(book["image"], caption=f"{book['name']} - {book['price']}")
    
    st.header("🔥 Promotions & Discounts")
    st.write("Don't miss our special offers on bestselling books!")

    promotions = [
        {"image": "https://tse2.mm.bing.net/th?id=OIP.-FkAx5gsmOcOMEhkIHblMgHaLU&w=200&h=305&c=7", "caption": "Get 10% off on 'The 5 AM Club'!"},
        {"image": "https://tse2.mm.bing.net/th?id=OIP.PdPn5Xj4vahLtOFZPMIwbAHaJ5&w=200&h=267&c=7", "caption": "Limited-time deal on 'Who Will Cry When You Die?'"},
    ]

    for promo in promotions:
        st.image(promo["image"], caption=promo["caption"])
    
    st.header("📚 Bestsellers")
    st.write("Discover the books everyone is reading right now!")

    bestsellers = [
        {"name": "Sapiens: A Brief History of Humankind", "price": "$14.29", "image": "https://tse2.mm.bing.net/th?id=OIP.U7Cgx-f0lhA5IKBUL8viFgHaLX&w=200&h=200&c=7"},
        {"name": "The Alchemist", "price": "$8.99", "image": "https://tse1.mm.bing.net/th?id=OIP.CP_1Cu_o_riUJ-gnUWz6DwHaLX&w=200&h=200&c=7"},
    ]

    for book in bestsellers:
        st.image(book["image"], caption=f"{book['name']} - {book['price']}")

if __name__ == "__main__":
    show()
