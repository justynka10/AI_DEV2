import requests

def get_authentication_token(apikey, task_name):

    data = {"apikey": apikey}
    url = f"https://tasks.aidevs.pl/token/{task_name}"

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Sprawdzenie, czy odpowiedź jest sukcesem (status kod 2xx)
        token = response.json().get("token")
        return token
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    

def get_task(token):

    try:
        url = f"https://tasks.aidevs.pl/task/{token}"
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy odpowiedź jest sukcesem (status kod 2xx)
        return response.json()  # Zwraca odpowiedź w formie słownika JSON
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
import requests

def send_answer(token, answer):
    
    try:
        data = {"answer": answer}
        url = f"https://tasks.aidevs.pl/answer/{token}"

        response = requests.post(url, json=data)
        response.raise_for_status()  # Sprawdzenie, czy odpowiedź jest sukcesem (status kod 2xx)
        return response.json()  # Zwrócenie odpowiedzi w formie słownika JSON
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
