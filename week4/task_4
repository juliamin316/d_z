import requests
from datetime import datetime, timedelta


def get_sites(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Ошибка, код ошибки: {response.status_code}')


def get_upcoming_contests(data):
    current_time = datetime.now()
    upcoming_contests = []

    for site in data:
        platform_name = site['key']
        URL = f'https://kontests.net/api/v1/{platform_name}'
        response = requests.get(URL)
        if response.status_code == 200:
            contests = response.json()
            for contest in contests:
                start_time = parse_start_time(contest['start_time'])
                if timedelta(days=15) >= start_time - current_time >= timedelta(days=0):
                    contest_name = contest['name']
                    contest_date = start_time.strftime("%d-%m-%Y")
                    upcoming_contests.append((contest_name, contest_date))
        else:
            raise Exception(f'Ошибка, код ошибки: {response.status_code}')

    return upcoming_contests


def parse_start_time(start_time):
    try:
        return datetime.fromisoformat(start_time[:-1])
    except ValueError:
        return datetime.strptime(start_time[2:10], "%y-%m-%d")


if __name__ == '__main__':
    URL = 'https://kontests.net/api/v1/sites'
    sites_data = get_sites(URL)
    upcoming_contests = get_upcoming_contests(sites_data)
    for contest in upcoming_contests:
        print(contest[0], "  DATE: ", contest[1])
