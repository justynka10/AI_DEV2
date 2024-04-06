## Polecenie
Spraw, aby ChatGPT poprawił poniższy kod tak, aby poprawnie zwracał zadaną liczbę ciągu Fibonnacciego. Kod jest napisany w PHP 8.1. Limit czasu wykonania funkcji to 2 sekundy. W przypadku jakichkolwiek błędów, zwracaną wartością z funkcji powinno być zero. Weź pod uwagę, że wyliczanie elementów ciągu Fibbonaciego jest BARDZO zasobożerne pod względem pamięci. Może warto pomyśleć o jakimś usprawnieniu? (GPT-4)

## System [zdefiniowany]
Masz dany poniższy kod. Wszystkie moje polecenia dotyczą właśnie jego. W odpowiedziach zwracaj tylko gotowy kod bez żadnych wyjaśnień i komentarzy.

###
```
function fib($n) {
    if ($n > 2) return $n
    return fib($n-1) + fib($n-2)
}
```

## Prompt [do uzupełnienia]
Popraw ten kod, a następnie zastanów się w jaki sposób można go zoptymalizować. Zależy mi na szybkim wykonywaniu funkcji - maksymalnie do 2 sekund. Zadbaj o obsługę błędów - w przypadku pojawienia się błędu, funkcja powinna zwrócić 0. Nie rzucaj wyjątkami. Weź pod uwagę odpowiednie zarządzanie pamięcią.

## Output
```
function fib($n) {
    if (!is_numeric($n) || $n < 0) return 0;
    if ($n <= 1) return $n;
    $a = 0;
    $b = 1;
    for ($i = 2; $i <= $n; $i++) {
        $c = $a + $b;
        $a = $b;
        $b = $c;
    }
    return $b;
}
```

Test01 (małe liczby) = OK\
Test02 (liczby ujemne) = OK\
Test03 (tekst jako input) = OK\
Test04 (duża liczba) = OK