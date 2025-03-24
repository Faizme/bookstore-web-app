from fpdf import FPDF
import streamlit as st

def generate_pdf_bill(cart, total_amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Your Bill", ln=True, align="C")
    pdf.ln(10)
    
    pdf.cell(100, 10, txt="Product", border=1)
    pdf.cell(50, 10, txt="Price", border=1, ln=True)
    
    for item in cart:
        pdf.cell(100, 10, txt=item['name'], border=1)
        pdf.cell(50, 10, txt=item['price'], border=1, ln=True)
    
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total: ${total_amount}", ln=True, align="C")
    pdf.cell(200, 10, txt="Thank you for your purchase!", ln=True, align="C")
    
    return pdf.output(dest="S").encode("latin1")

def show():
    st.header("Checkout")
    
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    if 'checkout_total' not in st.session_state:
        st.session_state.checkout_total = 0
    
    if not st.session_state.cart or st.session_state.checkout_total == 0:
        st.write("Your cart is empty. Please add items to your cart before proceeding to checkout.")
        return
    
    st.write("Items in your order:")
    for item in st.session_state.cart:
        st.write(f"{item['name']} - {item['price']}")
    
    st.write(f"Total amount to be paid: ${st.session_state.checkout_total}")
    
    if st.button("Confirm Purchase"):
        st.success("Thank you for your purchase!")
        
        # Generate PDF bill with itemized list
        pdf_bill = generate_pdf_bill(st.session_state.cart, st.session_state.checkout_total)
        
        # Provide a download button for the PDF bill
        st.download_button(
            label="Download Bill as PDF",
            data=pdf_bill,
            file_name="bill.pdf",
            mime="application/pdf"
        )
        
        # Clear the cart and reset the checkout total
        st.session_state.cart = []
        st.session_state.checkout_total = 0
        
        # Redirect to home after download
        st.session_state.page = "Home"