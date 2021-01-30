## Notation

With the following variables:

- S is total number of staff
- P is total number of patients
- R is total number of rooms
- C is max capacity per room
- B is number of session blocks per week
- G is number of group sessions per week
- N is number of individual sessions per patient per week

## Decision Problem Notes

Conditions that automatically make scheduling impossible:

- More total sessions `(G + (P * N))` than room block slots `(B * R)`
- More total sessions `(G + (P * N))` than staff block slots `(B * S)`
- More total sessions `(P + S) - ` than

(B * R) - (G + (P * N)) =
(20 + 8 * 4)  - 
