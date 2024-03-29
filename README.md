# goit-algo-hw-05

## Порівняння алгоритмів пошуку підрядка

### Результати вимірювань

- **Knuth-Morris-Pratt (KMP):**
  - Стаття 1: існуючий підрядок - 0.0091, вигаданий підрядок - 0.0026
  - Стаття 2: існуючий підрядок - 0.0082, вигаданий підрядок - 0.0066
- **Rabin-Karp:**
  - Стаття 1: існуючий підрядок - 0.0135, вигаданий підрядок - 0.0105
  - Стаття 2: існуючий підрядок - 0.0018, вигаданий підрядок - 0.0158
- **Boyer-Moore:**
  - Стаття 1: існуючий підрядок - 0.0048, вигаданий підрядок - 0.0015
  - Стаття 2: існуючий підрядок - 0.0003, вигаданий підрядок - 0.0056

### Висновки

- **Стаття 1**: Алгоритм **Boyer-Moore** був найшвидшим для обох підрядків.
- **Стаття 2**: Для існуючого підрядка найшвидшим був алгоритм **Boyer-Moore**, а для вигаданого — **KMP** показав кращі результати, хоча для вигаданого підрядка результати більш змішані.
- Загально, **Boyer-Moore** зазвичай є найшвидшим алгоритмом, особливо для великих текстів або коли підрядок присутній у тексті.

Ці результати підтверджують, що алгоритм **Boyer-Moore** зазвичай ефективніший у порівнянні з **KMP** і **Rabin-Karp** для різних типів тексту та підрядків.
