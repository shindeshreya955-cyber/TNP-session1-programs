# Function Overloading Example in Python
class PaymentMethod:
    def payment_netbanking(self, bank_name, amount):
        print("Payment through Net Banking")
        print("Bank Name :", bank_name)
        print("Amount :", amount)
        
    def payment_creditcard(self, card_number, amount):
        print("Payment through Credit Card")
        print("Card Number :", card_number)
        print("Amount :", amount)

    def payment_upi(self, upi_id, pin, amount):
        print("Payment through UPI")
        print("UPI ID :", upi_id)
        print("Amount :", amount)

obj = PaymentMethod()
obj.payment_netbanking("SBI", 5000.0)
print()
obj.payment_creditcard(1234567890123456, 2500.0)
print()
obj.payment_upi("shreya@upi", 1234, 1500.0)
