## Notation

With the following variables:

- _B_ is number of session blocks per week
- _S<sub>i</sub>_ is total number of staff per category _i_
- _P_ is total number of patients
- _R<sub>j</sub>_ is total number of rooms available for session type _j_
- _G<sub>i</sub>_ is number of group sessions per week for category _i_
- _N<sub>i</sub>_ is number of individual sessions per week for category _i_

## Decision Problem Notes

Necessary conditions to make scheduling possible

- Total available room blocks must be greater than or equal to the total required sessions _(B * R) >= (G + (P * N))_
- Available room blocks per session type must be greater than or equal to number of required sessions of that type _(B * R<sub>j</sub>) >= (G + (P * N))_
- Total available staff blocks must be greater than or equal to total required sessions _(B * S >= (G + (P * N))_
- Staff blocks per category must be greater than or equal to required sessions per category _(B * S<sub>i</sub>) >= (G<sub>i</sub> + (P<sub>i</sub> * N<))_
