# Co to AI_DEVS2?
<b>AI_Devs</b> to 5-tygodniowy kurs łączenia narzędzi Generative AI (w szczególności modeli OpenAI) z logiką aplikacji oraz narzędziami do automatyzacji.

W ramach kursu, każdego dnia pojawiają się zadania praktyczne do wykonania. Ich rozwiązania (oraz inne przykłady kodu pojawiające się w kursie) zamieszczam w niniejszym repozytorium.

# Co zawiera to repozytorium?
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji">Przykłady z lekcji</a> - w oryginale przykłady prezentowane w kursie napisane są w języku TypeScript. Jako, że na codzień posługuję się głównie Pythonem, to staram się przełożyć prezentowane kody, właśnie na tę technologię;
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Zadania%20z%20API">Zadania z API</a> - to moja implementacja rozwiązań zadań praktycznych (takiej pracy domowej z poszczególnych lekcji) wykonywanych przy wykorzystaniu API, głównie OpenAI; biblioteką używaną w większości zadań jest <a href="https://python.langchain.com/docs/get_started/introduction">LangChain</a>;
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Zadania%20z%20Playground">Zadania z Playground</a> - to spis rozwiązań drugiego typu zadań praktycznych pojawiających się w kursie. Symulują one korzystanie z OpenAI Playground. Jedno z pól "system" lub "user" jest zdefiniowane, a zagadką jest uzupełnienie tego drugiego, tak aby uzyskać output pożądany w zadaniu.

## Przykłady z lekcji
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/01_langchain_init_(C01L04).ipynb">01_langchain_init</a> - schemat połączenia z modelem i wysłanie prostego zapytania;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/02_langchain_format_(C01L04).ipynb">02_langchain_format</a> - użycie formatek do definiowania promptów dostępnych w LangChain;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/03_langchain_stream_(C01L04).ipynb">03_langchain_stream</a> - strumieniowanie w LangChain;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/04_tiktoken_(C01L04).ipynb">04_tiktoken</a> - kontrola zużycia tokenów dla różnych modeli;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/05_conversation_(C01L04).ipynb">05_conversation</a> - konwersacja z użyciem LangChain, wprowadzenie "pływającego okna" - `ConversationBufferWindowMemory`;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/06_external_(C01L05).ipynb">06_external</a> - podejście PAL (Program-Aided Language Models), czyli generowanie kodu w odpowiedzi, który następnie można wykonać i uzyskać poprawny rezultat;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/07_output_(C01L05).ipynb">07_output</a> - Guardrails, czyli zastosowanaie dodatkowego prompta w celu ochrony przed ujawnieniem instrukcji systemowej;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/08_cot_(C01L05).ipynb">08_cot</a> - zastosowanie Chain of Thought (CoT), czyli prowadzenie modelu przez ciąg myślowy;
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji/09_context_(C02L02)">09_context</a> - dostarczanie zewnętrznego, dynamicznego kontekstu;
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji/10_switching_(C02L02)">10_switching</a> - wybór źródła wiedzy dopasowanego do pytania;
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji/11_docs_(C02L02)">11_docs</a> - podział plików na fragmenty tematyczne i tworzenie na tej podstawie dokumentów (ang. chunk);
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji/12_web_(C02L02)">12_web</a> - tworzenie dokumentu na podstawie żródła o nietypowej strukturze - zescrapowanej strony internetowych;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/13_functions_(C02L05).ipynb">13_functions</a> - wprowadzenie Function Calling;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/14_agent_(C02L05).ipynb">14_agent</a> - automatyczny wybór funkcji, koncepcja Agentów i Single Entry Point (jeden punkt wejścia);
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji/17_tree_(C03L01)">17_tree</a> - zastosowanie Tree of Thoughts, czyli wygenerowanie możliwych scenariuszy, pogłębienie ich, wybranie najbardziej prawdopodobnych i udzielenie odpowiedzi;
- <a href="https://github.com/justynka10/AI_DEV2/tree/main/Przyk%C5%82ady%20z%20lekcji/18_knowledge_(C03L01)">18_knowledge</a> - podstawowe wyszukiwanie słów kluczowych w dokumencie, aby dopasować odpowiedź do kontekstu;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/20_catch_(C03L02).ipynb">20_catch</a> - obsługa błędów mocniejszym promptem albo modelem;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/21_similarity_(C03L03)">21_similarity</a> - wyszukiwanie (tzw. Similarity Search) z pomocą baz wektorowych i tworzenie dynamicznego kontekstu na tej podstawie;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/22_simple_(C03L03).ipynb">22_simple</a> - Similarity Search w pracy z małą bazą wiedzy;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/23_fragmented_(C03L03).ipynb">23_fragmented</a> - problem fragmentacji dokumentów, która może prowadzić do pominięcia istotnych informacji w dynamicznym kontekście;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/24_files_(C03L03)">24_files</a> - praca z różnymi formatami plików - budowanie zestawu danych na podstawie informacji bezpośrednio ze strony internetowej;
- <a href="https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/25_correct_(C03L04)">25_correct</a> - korekta dłuższego tekstu podzielonego na fragmenty;
- [27_qdrant](https://github.com/justynka10/AI_DEV2/blob/main/Przyk%C5%82ady%20z%20lekcji/27_qdrant_(C03L04)) - wyszukiwanie w lokalnej bazie wektorowej Qdrant;