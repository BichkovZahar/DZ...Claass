class Bank:
    def __init__(self , customer , bince):
        self.customer = customer
        self.bince = bince
class BankAccount:
    def __init__(self , customers , balance):
        self.customers = customers
        self.balance = balance
    def get_total_balance(self , bince , balance):
        suma = bince + balance
        return suma
finish = Bank("Захар" , 700)
finish1  = Bank("Женя" , 800)
finish2 = Bank("Даша" , 300)
print(f"Клиент: {finish.customer} . Баланс: {finish.bince} грн")
print(f"Клиент: {finish1.customer} . Баланс: {finish1.bince} грн")
print(f"Клиент: {finish2.customer} . Баланс: {finish2.bince} грн")
print()
rezult = BankAccount("Маша" , 100)
print(f"Клиент: {rezult.customers} . Баланс: {rezult.balance} грн")
print()
print(f"Загальний баланс усіх становить: {rezult.get_total_balance(bince=1800 , balance=100)} грн")