customers_list = list(map(int, input().split(', ')))
taxi_list = list(map(int, input().split(', ')))
total_time = 0

while taxi_list:

    if customers_list:

        current_customer = customers_list[0]
        if current_customer <= taxi_list[-1]:
            total_time += current_customer
            customers_list.pop(0)
            taxi_list.pop()

        else:
            taxi_list.pop()
            continue

    else:
        print('All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')

else:

    if customers_list:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join(list(map(str, customers_list)))}')

    else:
        print('All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')

