num_p = int(input("Number of purchases: "))
sales_t = float(input("Sales tax: "))
customer_list = []
cost_list = []

for i in range(num_p):
    customer = input("Customer: ")
    customer_list.append(customer)
    cost = int(input("Cost: "))
    cost_list.append(cost)
    
def add_tax(listx, tax):
    new_list = []
    for num in listx:
        new_list.append(num + num*tax)
    return new_list

new_list = add_tax(cost_list, sales_t)

final_dict = {}

for i in range(num_p):
    if customer_list[i] in final_dict:
        final_dict[customer_list[i]] += new_list[i]
    else:
        final_dict[customer_list[i]] = new_list[i]


print(final_dict)
