# Overview

Algorithm to optimize the scheduling of vaccination

## Inputs

### Vaccine Production Facility

The following attributes define each facility:

- Number of cases of vaccines produced each month
- Number of vaccines doses per case
- Number of hours in which all vaccines must be administered once a case is opened
- Maximum number of vaccine deliveries per month
- Maximum number of cases that can be shipped per delivery

### Vaccination Facility

The following attributes define each facility:

- Maximum number of cases the facility can store
- Number of workers supporting supporting registration
- Number of workers administering vaccines
- Number of hours of operation per day
- Number of minutes required to register a patient
- Number of minutes required to vaccinate a patient
- Number of minutes required to monitor a patient for symptoms

### Population Variables

- Population distribution
- Maximum number of miles

## Outputs

- Maximize:
  - Number of patients vaccinated
- Minimize:
  - Number of vaccines wasted
  - Number of workers per category
  - Average wait time for patients
- Optimize:
  - Number of vaccine shipments per month
  - Number of vaccine cases per shipment
  - Number and placement of vaccination facilities
