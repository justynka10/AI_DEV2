## Polecenie
Przygotuj tablicę JSON (a nie serię pojedynczych JSON-ów) zawierającą elementy składające się z par tytułów (title) i autorów (author) do każdej z książek. Wykorzystaj One-shot prompting (GPT-3.5-turbo).

## Notka
<b>One-shot / Few-shot Prompting</b> polega na podawaniu przykładów prezentujących oczekiwane zachowanie modelu.

## System [do uzupełnienia]
Przygotuj tablicę JSON zawierającą elementy składające się z par tytułów i autorów do każdej z książek

Przykład:
[{"title": "Krzyżacy", "author": "Henryk Sienkiewicz"}, ...] ###

## Prompt [zdefiniowany]
Romeo i Julia\
Cień wiatru\
Rok 1984

## Output
```
[
    {"title": "Romeo i Julia", "author": "William
Shakespeare"},
    {"title": "Cień wiatru", "author": "Carlos
Ruiz Zafón"},
    {"title": "Rok 1984", "author": "George
Orwell"}
]
```