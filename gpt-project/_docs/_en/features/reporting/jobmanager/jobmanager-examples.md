---
title: JobManager examples
product_label:
  - enterprise
description: Learn about important job types in injixo and what they are used for.
---

Examples of different job types that you can configure in _WFM > Administration > System > JobManager_{:.breadcrumbs}. Add the following parameters and values in the dialog window in the **Job Processing Parameters** section after clicking the {% icon item-add %}.


<style>
table {
  width: 100%;
}

table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

## Email reports

<!-- {{ 1 | image: 'Sending Job Manager Report via Email', '50%' }} -->

| Parameter       | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| cmd             | Internal report name                                                 |
| p               | Planning unit ID                                                     |
| e               | Employees<br>Values: all, individual IDs delimited by hyphen (-)     |
| c               | Contracts<br>Values: all, individual IDs delimited by hyphen (-)     |
| se              | Selections<br>Values: all, individual IDs delimited by hyphen (-)    |
| level           | [Level ID](#level-id)                                                |
| lid             | [Language ID](#language-id)                                          |
| targethtml      | Output Format<br>Values: 0 (PDF), 1 (HTML)                           |
| targetanonymous | Standard or Anonymous reports<br>Values: 0 (standard), 1 (anonymous) |
| jobnameid       | (Optional) Internal report ID that can be blank.                     |

## Insert shift sequences

<!-- {{ 2 | image: 'Insert Shift Sequences', '50%' }} -->

| Parameter    | Description                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| delete1      | Delete full-day activities<br>Values: 1 (yes), 0 (no)                                                                             |
| delete2      | Delete availability periods<br>Values: 1 (yes), 0 (no)                                                                            |
| delete3      | Delete all activities and shifts<br>Values: 1 (yes), 0 (no)                                                                       |
| level_id     | [Level ID](#level-id)                                                                                                             |
| lid          | [Language ID](#language-id)                                                                                                       |
| nr_of_seq    | Number of employees with shift sequences<br>Value: all                                                                            |
| option       | Internal ID<br>Value: 2                                                                                                           |
| planunit_id  | Planning unit ID                                                                                                                  |
| selection_id | Selections<br>Values: -1 (all selections), specific IDs delimited by hyphen (-)                                                   |
| shiftseq_id  | IDs of shift sequences assigned to the selected employees delimited by hyphen (-). Required unless type is set.                   |
| type         | (Optional) Selects all shift sequences for the selected employees. If used, the shiftseq_id parameter can be blank.<br>Value: all |

### Lottery and assignment

<!-- {{ 3 | image: 'Lottery or Assignment', '50%' }} -->

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doreporting | Log file<br>Values: 1 (yes), 0 (no)                                                                                                                                                                                                                                                                                                                                                                                                          |
| e           | Employees<br>Values: all, individual IDs delimited by hyphen (-)                                                                                                                                                                                                                                                                                                                                                                             |
| lid         | [Language ID](#language-id)                                                                                                                                                                                                                                                                                                                                                                                                                  |
| modelcase   | Internal ID<br>Values: 10 (shift assignment), 11 (shift lottery)                                                                                                                                                                                                                                                                                                                                                                             |
| observecorr | Take the tolerance value for the start time into account<br>Values: 0 (no), 1 (yes)                                                                                                                                                                                                                                                                                                                                                          |
| periodid    | Planning period ID or multiple IDs delimited by comma. The correct planning period ID can be found in the source code of the page via dev tools (first part of the value in the data-flip-id element) or by using the [API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). If the time period for job processing is set to relative, only the relevant planning period is taken into account. |
| puid        | Planning unit ID                                                                                                                                                                                                                                                                                                                                                                                                                             |
| staffcount  | Required but not used. Enter value 0                                                                                                                                                                                                                                                                                                         |
| tolerance   | Maximum deviation from the average start time<br>Value: Time using format HH:MM), 00:00 (if the observecorr parameter is 0)                                                                                                                                                                                                                                                                                                                  |

### Copy level

The **Copy level content** functionality can be found under _Plan > Configuration > Scheduling actions_{:.breadcrumbs}.

| Parameter     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| copystartdate | Start date for inserting the data in [Julian date format](https://www.onlineconversion.com/julian_date.htm). Data is shifted if the data is not the start date of the planning period. |
| deletesource  | Delete the source level.<br>Values: 0 (Keep source level), 1 (delete source level)                                                                                                                                                                                                                                                                                                                                                           |
| lid           | [Language ID](#language-id) for error messages                                                                                                                                                                                                                                                                                                                                                                                               |
| e             | Employees<br>Values: all, individual IDs delimited by hyphen (-)                                                                                                                                                                                                                                                                                                                                                                             |
| modelcase     | Internal ID.<br>Values: 15 (copy level), 16 (delete level)                                                                                                                                                                                                                                                                                                                                                                                 |
| periodid      | Planning period ID or multiple IDs delimited by comma. The correct planning period ID can be found in the source code of the page via dev tools (first part of the value in the data-flip-id element) or by using the [API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). If the time period for job processing is set to relative, only the relevant planning period is taken into account. |
| puid          | ID of the planning unit. Can be restricted by ID when separated by a delimiter (-)                                                                                                                                                                                                                                                                                                                                                           |
| sourcelevel   | [Level ID](#level-id) (Source)                                                                                                                                                                                                                                                                                                                                                                                                               |
| targetlevel   | [Level ID](#level-id) (Target)                                                                                                                                                                                                                                                                                                                                                                                                               |
| staffcount    | Required but not used. Enter value 0                                                                                                                                                                                                                                                                                     |
| selectionid   | Selection ID<br>Values: -1 (all selections), specific ID delimited by hyphen (-)                                                                                                                                                                                                                                                                                                                                                             |

## Email parameters

Email parameters are optional. If the email parameters are not configured, reports will only be available in the JobProcessor.

| Parameter  | Description                                                                                                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| em         | Employee IDs<br>Values: -1 (all), multiple IDs delimited by hyphen (-)                                                                                                                                                            |
| sendtoall  | Send a single email to the selected employees<br>Values: 1 (yes), 0 (no)                                                                                                                                                          |
| sendperemp | Send an individual email to the selected employee. Not available for all reports <!-- which? --><br>Values: 1 (yes), 0 (no)                                                                                                       |
| email      | Recipient email address. Multiple email recipients not supported. If needed, use an email distribution list that forwards internally to multiple recipients. The email parameter is not used when the em parameter specifies IDs. |
| emailtype  | Employee email address<br>Values: 1 (email 1), 3 (email 2), 2 (both). injixo Cloud versions does not support email 2.                                                                                                             |
| comments   | Optional text for the email message                                                                                                                                                                                               |

## Language ID

The **lid** parameter defines the language ID for the resulting report and supports the following IDs:

English US (1033)<br>
German (1031)<br>
French (1036)<br>
Italian (1040)<br>
Spanish modern (3082)<br>
Spanish standard (1034)<br>
Dutch (1043)<br>
Swedish (1053)<br>
English UK (2057)<br>
Polish (1045)

## Level ID

The **level** parameter defines the level from which data is read and supports the following IDs:

1000 (plan)<br>
3000 (current status)<br>
5000 (external system)<br>
4000 (time recording)<br>
2000 (request)<br>
2001 (alternative request)<br>
2002 (holiday/absence request)<br>
6000 (availability)<br>
6001 (on-call duty)<br>
4001 (correction)<br>
8000 (version 1)<br>
8001 (version 2)<br>
8002 (version 3)
