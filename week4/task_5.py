import requests

def calculate_working_hours(months):
    working_hours = 0
    for month in months:
        url = f"https://example.com/api/working_hours/{month}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Non-200 response code")
        data = response.json()
        working_hours += sum(data.values())
    return working_hours

def calculate_worker_earnings(workers, hourly_rate, hours):
    earnings = {}
    for worker in workers:
        name = worker['name']
        currency = worker['currency']
        rate = worker['rate']
        hourly_pay = task_2(currency, rate, "RUB")
        total_earnings = hourly_pay * hours
        earnings[name] = {'currency': 'RUB', 'total_earnings': total_earnings}
    return earnings

def task_5(workers_data):
    months = [3, 4, 5]
    working_hours = calculate_working_hours(months)
    earnings = calculate_worker_earnings(workers_data, hourly_rate, working_hours)
    
    for worker, data in earnings.items():
        name = worker
        total_earnings = data['total_earnings']
        currency = data['currency']
        print(f"{name} earned {total_earnings} {currency}")

# Пример использования
workers_data = [{'name': "Ivan Ivanov", "currency": "RUB", "rate": 100}]
task_5(workers_data)
