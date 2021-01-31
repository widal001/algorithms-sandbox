## Problem Statement

To optimize the scheduling of individual and group therapy sessions, given the following variables:
- Number of available rooms
- Number of session blocks per week
- Number of therapeutic staff
- Number of patients
- Number of groups and max size per group
- Mapping of topics to staff, patients, and groups based on interest or relevance

## Challenge 1: Double-sided Random Assignment

With the following variables fixed:
- Number of available rooms by session type
- Number of session blocks per week
- Number of staff per category

And the following constraints specified:
1. Staff members can lead a maximum of one session (group or individual) per session block
1. Rooms can hold a maximum of one session (individual or group) per session block
1. Group sessions must have a minimum of one staff member present
1. All individual sessions a patient has in a given category must be with the same staff member

Given the following inputs:
- Number of patients
- Number of groups sessions
- Number of times per week each group must meet
- Number of individual sessions per week each patient must have in each category

Produce a function that:
- **Decision:** Checks if its possible to schedule the preferred number of individual and group sessions without violating any of the constraints
- **Assignment:** Returns the following assignments without violating the constraints
  - Patients to staff
  - Patients and staff to groups
  - Individual and group sessions to rooms and session blocks

## Extending the problem

Additional fixed variables:
- Maximum occupancy per room

Additional constraints:
- Patients must be in exactly one session (individual or group) during a given session block
- No room can exceed its maximum occupancy
- Individuals and staff members can't be matched to a group unless they can attend all sessions for that group in a week

Additional inputs:
- Number of times per week each group must meet
- Mapping of topics to staff, patients, and groups based on interest or relevance
