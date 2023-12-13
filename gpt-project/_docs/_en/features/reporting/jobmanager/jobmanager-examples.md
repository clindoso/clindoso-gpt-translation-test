---
title: JobManager examples
product_label:
  - enterprise
description: Learn about important job types in injixo and what they are used for.
---

## Examples

Below are a few examples of different Job Types. The most important (and most frequently used) is the automatic creation and sending of Reports as described in the first example.

### Sending reports by email

{{ 1 | image: 'Sending Job Manager Report via Email', '50%' }}

| Parameter           | Meaning                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **cmd**             | Internal name of the Report, **Mandatory Field**, see {% link_new Report names and parameters | features/reporting/jobmanager/jobmanager-reportnames.md %} |
| **p**               | ID of the Planning Unit                                                                       |
| **e**               | Employees, all together or IDs with delimiters (-)                                            |
| **c**               | Contracts, all together or IDs with delimiters (-)                                            |
| **se**              | Selections, all together or IDs with delimiters (-)                                           |
| **level**           | ID of the Level                                                                               |
| **lid**             | [Language-ID](/jobmanager#parameter), e.g. 1031 for German                                    |
| **targethtml**      | Output Format, 0 for PDF, 1 for HTML                                                          |
| **targetanonymous** | Standard (0) or Anonymous (1) reports                                                         |
| jobnameid           | ID of the report _(optional)_                                                                 |

#### EMail parameters

All email parameters are optional. If these parameters are not specified, the report will only be available in the JobProcessor.

| Parameter      | Meaning                                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **em**         | Selected recipients, employee IDs with separators (-), -1 for all                                                                                                                                                     |
| **sendtoall**  | Send one email to all selected employees                                                                                                                                                                              |
| **sendperemp** | Send an email to each employee individually (1 or 0). Not available for all reports                                                                                                                                   |
| **email**      | Individual recipient email address. For multiple email recipients, use an email distribution list that forwards internally to multiple recipients. If IDs are specified in **em**, the parameter _email_ is not used. |
| **emailtype**  |  Selection of employee email address (first - 1, second - 3, both - 2)                                                                                                                                                |
| **comments**   | Optional text for email message                                                                                                                                                                                       |

### Insert shift sequences

{{ 2 | image: 'Insert Shift Sequences', '50%' }}

| Parameter        | Meaning                                                                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **delete1**      | 1 to delete all-day activities. Otherwise 0.                                                                                                        |
| **delete2**      | 1 to delete availability frame. Otherwise 0.                                                                                                        |
| **delete3**      | 1 to delete all activities and shifts. Otherwise 0.                                                                                                 |
| **level_id**     | ID of level                                                                                                                                         |
| **lid**          | [Language ID](/jobmanager#parameter), e.g. 1031 for German                                                                                          |
| **nr_of_seq**    | Number of employees with shift sequences (mandatory parameter), value: all                                                                          |
| **option**       | Must be set to 2                                                                                                                                    |
| **planunit_id**  | ID of the planning unit                                                                                                                             |
| **selection_id** | ID of the selection, 0 for all, multiple entries possible                                                                                           |
| **shiftseq_id**  | Internal ID of the assignment of the shift sequence to the employee, separator (-), mandatory unless type is set                                    |
| **type**         | Selection of all shift sequences of the employees listed, only 'all' possible. Optional parameter. If set, no IDs need to be listed in shiftseq_id. |

### Lottery and assignment

{{ 3 | image: 'Lottery or Assignment', '50%' }}

| Parameter       | Meaning                                                                                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **doreporting** | 1 to create a log file, 0 otherwise.                                                                                                                                                                                      |
| **e**           | Employees, all together or by ID with delimiters (-)                                                                                                                                                                      |
| **lid**         | [Sprach-ID](/jobmanager#parameter) Language ID, e.g. 1031 for German                                                                                                                                                      |
| **modelcase**   | Internal ID of the transaction. 10 for assignment, 11 for lottery                                                                                                                                                         |
| **observecorr** |  Set to 1 to take into account the tolerance value for the start time. Otherwise 0                                                                                                                                        |
| **periodid**    | ID of the planning period. Multiple selections are possible with a delimiter (,). If the planning period is relative, only the relevant planning period is taken into account <!-- won't work with scheduling periods --> |
| **puid**        | ID of the Planning Unit                                                                                                                                                                                                   |
| **staffcount**  | Number of employees to be processed. This value is ignored but must be set.                                                                                                                                               |
| **tolerance**   | 00:00 - Value for the deviation from the average start time. Mandatory if observecorr = 0                                                                                                                                 |

### Copying levels

{{ 4 | image: 'Level Copy', '50%' }}

| Parameter         | Meaning                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **copystartdate** | Start date for inserting the data from the source level. Mandatory value, must be specified in [Julian date format](https://www.onlineconversion.com/julian_date.htm). Must match the start date and the planning period. |
| **deletesource**  | 0 if the source level should not be deleted, 1 if it should be deleted                                                                                                                                                    |
| **lid**           | [Language ID](/jobmanager#parameter) for error messages, e.g. 1031 for German                                                                                                                                             |
| **e**             | Employees, all together or by ID with delimiters (-)                                                                                                                                                                      |
| **modelcase**     | Internal ID of the operation type. 15 to copy the level, 16 to delete it.                                                                                                                                                 |
| **periodid**      | ID of the planning period (mandatory value). Multiple entries are allowed when separated by a delimiter (,) <!-- won't work with scheduling periods -->                                                                   |
| **puid**          | ID of the planning unit. Can be restricted by ID when separated by a delimiter (-)                                                                                                                                        |
| **sourcelevel**   | ID of the source level                                                                                                                                                                                                    |
| **targetlevel**   | ID of the target level                                                                                                                                                                                                    |
| **staffcount**    | Number of employees to be processed. This value is ignored but must be set.                                                                                                                                               |
| **selectionid**   | -1 for all selections, restriction via ID possible if separated by delimiter (-)                                                                                                                                          |
| **staffids**      | -1 for all employees, restriction via ID possible if separated by delimiter (-)                                                                                                                                           |
