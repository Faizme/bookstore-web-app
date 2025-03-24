class Chatbot:
    def __init__(self):
        self.commands = {
            # General Greetings & Small Talk
            "hello": "Hi there! How can I assist you today?",
            "hi": "Hello! How can I help?",
            "how are you": "I'm just a bot, but I'm here to assist you!",
            "thank you": "You're welcome! Let me know if you need anything else.",
            "bye": "Goodbye! Have a great day!",
            
            # E-Commerce & Checkout Related
            "checkout": "To complete your purchase, go to your cart and click 'Proceed to Checkout'.",
            "bill": "After purchasing, you can download your bill from the checkout page.",
            "refund": "Refunds are processed within 5-7 business days after approval.",
            "exchange": "Exchanges are available within 30 days of purchase.",
            "payment options": "We accept credit cards, debit cards, UPI, and PayPal.",
            "shipping info": "We offer free shipping on orders over $50. Standard delivery takes 3-5 days.",
            "return policy": "You can return products within 30 days if they are unused and in original packaging.",
            "discounts": "Check our website for the latest discounts and offers!",
            
            # Fun & Miscellaneous
            "tell me a joke": "Why did the computer break up with the printer? Because it felt like it was getting too much paper work!",
            "fun fact": "Did you know? The first item ever sold on eBay was a broken laser pointer!",
            "motivate me": "Believe in yourself! Every expert was once a beginner. Keep going!",
            "what's your name": "I'm your shopping assistant chatbot!",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        return self.commands.get(user_input, "I'm sorry, I didn't understand that. Can you please rephrase?")