# HTML Article Formatter

## Opis aplikacji

**HTML Article Formatter** to prosta aplikacja Python, która pobiera treść artykułu z pliku tekstowego, a następnie formatuje go do postaci HTML. Proces generowania HTML korzysta z modelu GPT-4o-mini OpenAI, który automatycznie dodaje strukturalne tagi HTML, w tym miejsca na obrazy z opisami i podpisami.

### Funkcje aplikacji:
1. **Odczyt treści artykułu** z pliku tekstowego.
2. **Generowanie treści HTML** z użyciem modelu GPT.
3. **Zapisywanie wygenerowanego HTML** do pliku wyjściowego.


---

## Instrukcja uruchomienia


1. **Sklonuj repozytorium lub pobierz pliki projektu.**

2. **Zainstaluj wymagane biblioteki.**  
   Użyj `pip`, aby zainstalować bibliotekę `openai`:
   ```bash
   pip install openai
   ```

3. **Dodaj swój klucz API OpenAI.**  
W pliku kodu aplikacji zamień:
    ```bash
   api_key="put your openAI API key here"
   ```
    na swój klucz API

4. **Uruchom aplikację.**  
W terminalu uruchom plik aplikacji:
    ```bash
   python main.py
   ```