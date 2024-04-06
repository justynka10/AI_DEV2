## Polecenie
Napisz parser nowego języka formatowania tekstu podanego przez użytkownika. Język ten składa się ze znaczników zapisywanych jako !slowo! i bazuje na dziwnych wyrażeniach jednego z afrykańskich plemion. Twój prompt powinien zamienić go na kod HTML (GPT-3.5-turbo)

## System [do uzupełnienia]
Zamień na kod HTML wiadomość użytkownika napisaną w dziwnym afrykańskim języku. Język ten składa się ze znaczników zapisywanych jako !slowo!. Zastąp te znaczniki afrykańskiego plemienia standardowymi znacznikami HTML. Nie pomijaj tekstu, jedynie afrykańskie znaczniki.\
Na przykład znacznik !kukak! to znacznik listy wypunktowanej.

Zwróć uwagę na treść, ponieważ sugeruje ona jakich znaczników powinieneś użyć, tzn. że jeśli jest mowa o paragrafie, to powinieneś użyć znacznika HTML dla paragrafu.

Zwróć tylko przepisany fragment kodu. ###

## Prompt [zdefiniowany]
!tumba!to jest !zabzila!pogrubiony napis!zabzila! w środku paragrafu!tumba!

!kukak! punkt pierwszy
!kukak! punkt drugi
!kukak! punkt trzeci

!uuuaaa!fotka_lwa.jpg!uuuaaa!

!matata!Nagłówek pierwszego stopnia!matata!
!tumba!To jest paragraf. Może być !zabzila!długi!zabzila!, może być krótki... ten język ogarnia wszystko!tumba!

## Output
```
<p>To jest <strong>pogrubiony napis</strong> w środku paragrafu</p>

<ul>
<li>punkt pierwszy</li>
<li>punkt drugi</li>
<li>punkt trzeci</li>
</ul>

<img src="fotka_lwa.jpg" />

<h1>Nagłówek pierwszego stopnia</h1>
<p>To jest paragraf. Może być <strong>długi</strong>, może być krótki... ten język ogarnia wszystko</p>
```
✅ Testy zaliczone