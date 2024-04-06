## Polecenie
Piszesz klasyfikator problemów użytkownika w dziale pomocy technicznej. Zwróć JSON z kategorią problemu (dostępne kategorie to: pralka/telewizor/zmywarka), nazwę producenta oraz akcję której wymaga klient (zwrot/naprawa). Oczekiwana struktura odpowiedzi zależy od modelu.
Dla GPT-3.5-turbo:
`{"kategoria":"pralka","producent":"Whirpool","akcja":"zwrot"}`.\
Dla GPT-4:
`{"kategoria":"pralka","producent":"Whirpool","akcja":"zwrot","data":"20240406"}`\
UWAGA: Twój prompt wykonuje się jednocześnie na GPT-3.5-turbo i GPT-4!

## System [do uzupełnienia]
Wsparcie techniczne z tej strony. Klasyfikuję problemy zgłaszane przez użytkowników do jednej z kategorii: "pralka, telewizor, zmywarka". Następnie określam akcję, której żąda klient: "zwrot, naprawa".
Odpowiadam w formacie JSON, na przykład:
`{"kategoria":"pralka","producent":"Whirpool","akcja":"zwrot"}`.

Dzisiaj jest 30 marca 2024 roku. Jeśli jestem modelem GPT-4, to dodatkowo zapisuję tę datę w formacie "20240330":
`{"kategoria":"pralka","producent":"Whirpool","akcja":"zwrot","data":"20240406"}`

## Prompt [zdefiniowany]
Dzień dobry zespole wsparcia technicznego!

Kolejny raz zepsuł mi się odbiornik telewizyjny. Tak, to ten sam stary Samsung który ostatnio naprawialiście. Próbowałem włączyć i wyłaczyć go i to nawet trzy razy, ale nadal nie działa. Co robić? jak żyć?! Naprawicie to?

## Output
GPT-3.5-turbo
```
{"kategoria":"telewizor",
"producent":"Samsung",
"akcja":"naprawa"}
```
GPT-4
```
{"kategoria":"telewizor",
"producent":"Samsung",
"akcja":"naprawa",
"data":"20240330"}
```

## Notka
Teoretycznie to nie powinno działać, bo model nie wie, czym jest. Mogło tutaj zadziałać to, że druga instrukcja była nieco bardziej złożona i zrozumiał ją jedynie model GPT-4.