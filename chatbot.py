# Smart AI Customer Support Chatbot

print("===================================")
print("   Welcome to Smart AI Chatbot")
print("===================================")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    # Greeting
    if "hello" in user or "hi" in user:
        print("Bot: Hello! Welcome to our service.")

    # Order
    elif "order" in user:
        order_id = input("Bot: Enter your Order ID: ")
        print("Bot: Your order", order_id, "is being processed.")

    # Refund
    elif "refund" in user:
        print("Bot: Refund will be credited within 5-7 working days.")

    # Cancel
    elif "cancel" in user:
        print("Bot: Your order cancellation request is accepted.")

    # Payment
    elif "payment" in user:
        print("Bot: We support UPI, Debit Card and Credit Card.")

    # Delivery
    elif "delivery" in user:
        print("Bot: Delivery usually takes 3-5 days.")

    # Contact
    elif "contact" in user:
        print("Bot: Contact us at support@gmail.com")

    # Help
    elif "help" in user:
        print("Bot: Available services:")
        print("1. Order Tracking")
        print("2. Refund Status")
        print("3. Cancellation")
        print("4. Payment Information")
        print("5. Delivery Details")

    # Exit
    elif user == "bye":
        print("Bot: Thank you for using our chatbot!")
        break

    # Default
    else:
        print("Bot: Sorry! I didn't understand.")
