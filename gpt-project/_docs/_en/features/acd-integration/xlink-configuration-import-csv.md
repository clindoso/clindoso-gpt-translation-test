---
title: Import CSV files
product_label:
  - on-premise
description: Set up CSV imports of contact data and agent status changes in Xlink.
---

This article describes how to set up a CSV interface in Xlink. Before, you should have already {% link_new installed Xlink | features/acd-integration/xlink-installation-configuration.md %} and created an {% link_new external system | features/acd-integration/new-external-system.md %}

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## File format

The format of your CSV file depends on what data you want to import.

For the import of calls, e-mails, etc. (PhoneLink) you need at least one column per line in the CSV file for

- the name of the source
- the date
- the time
- each value to import (e.g. one column each for offered calls and AHT)

To import agent status data (login, logout and breaks) (TimeLink), you need at least one column per line in the CSV file for

- the activity
- the agent identifier
- the date
- the start time of the activity
- the end time of the activity

You can also specify a start time and duration or only a start time.
Date and time can also be combined in a DateTime field. There are more examples below.

## Supported time and date formats

The interface automatically recognizes the time format.

Examples for valid formats:

- 9:50 AM, 12:00 PM, 01:34 AM
- 9:50:34 AM, 12:00:00 PM, 01:34:12 AM
- .5, 8.5, 12,7
- 08:48:00, 8:48:00
- 08:48, 8:48
- 084800, 84800
- 0848, 848

The date format requires the parameter _DateOrder_. This determines the order of day, month, and year. Possible separators for the date are `.`, `-` or `/`.

Examples for valid formats (exemplary for parameter _DateOrder_ with value `mdy`):

- 02/09/2019, 02/09/19, 2/9/19, 2/9/2019, 020919, 02092019

Additionally supported are DateTime timestamps in a single field for date and time.

- 02/09/2019T01:08:40
- 02/09/2019T01:08:40Z
- 02/09/2019T01:08:40+00:00
- 02/09/2019 01:08:40
- 02/09/2019 01:08:40Z
- 02/09/2019 01:08:40+00:00

## General settings

The interface allows to configure a few general settings for the CSV import via the Xlink interface.

General settings for PhoneLink and TimeLink in the user interface:

{{ 1 | image: 'Configuration CSV Interface', '75%' }}

Proceed as follows to configure these settings:

1. Open the file 'isps_ul.exe
2. Right-click the external system. Choose _configuration_{:.menu-item}.
   Alternatively, click _Settings > ACD_{:.breadcrumbs} on the toolbar.
3. Select the folder where the CSV files are stored with _Data - Directory_.
4. Set in _Timezone - UTC offset_ if necessary, the time offset between the time in the CSV file and the local time
5. Define in _CSV separator_ the CSV separator you wish to use
6. Activate the {% link_new Logging | features/acd-integration/xlink-log-files.md %} within _Log - Options_ (optional)
7. Simply click _Ok_{:.doc-button} in the dialog to save the settings.

After saving, the values are stored in parameters within the `isps_ul.ini` file in the Xlink directory.

Below a table that lists and explains these parameters:

| Parameter                  | Details                                                                                                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source                     | Source directory for PhoneLink on the Xlink server itself.                                                                                                             |
| Destination                | Destination directory for PhoneLink. Only used if DeleteImportFiles is configured accordingly                                                                          |
| SeparatorCharacter         | separator for PhoneLink, enter 2 for comma, 3 for semicolon                                                                                                            |
| DeleteImportFiles          | PhoneLink data remains in directory (value 0), is moved (value 1) or is deleted (value 2), file move/delete actions are recorded in a log file (DeleteImportFiles.log) |
| ActivitySource             | Source directory for TimeLink on the Xlink server itself.                                                                                                              |
| ActivityDestination        | PhoneLink destination directory. Only used if DeleteActivityImportFiles is configured accordingly.                                                                     |
| ActivitySeparatorCharacter | Separator for TimeLink, enter 2 for comma, 3 for semicolon                                                                                                             |
| DeleteActivityImportFiles  | TimeLink data remains in the directory (value 0), is moved (value 1) or is deleted (value 2). Actions for 1 and 2 are recorded in DeleteImportFiles.log file           |
| TimeZone                   | Value for the time offset, permitted formats e.g. -2, 2, -3.5, 3.5, -08:00 or 06:30                                                                                    |
| Protocol                   | Turn logging on (value 1) or off (value 0) to see which values are read                                                                                                |

## Import of calls, emails and chats

PhoneLink can import countable data like calls, emails, chats, documents, etc. The interface recognizes the format of the CSV file via additional parameters.

### Required parameters

| Parameter       | Details                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HeaderLines     | Number of header lines that are not read and imported                                                                                                                              |
| DateColumn      | Column position of the date column, see also TimeStampColumn                                                                                                                       |
| TimeColumn      | Column position of the time column                                                                                                                                                 |
| GroupColumn     | Column position of the channel/queue name/phone number                                                                                                                             |
| Groups          | All queue names available in the file. Separated with semicolon                                                                                                                    |
| ColumnNames     | Names for all columns available in the file. use the file header or custom names, separated by semicolon, e.g. Queue;Date;Time;CallsOffered;CallsHandled;AHT                       |
| Interval        | Interval in minutes in which the ACD aggregates the data, usually 15, 30 or 60 minutes                                                                                             |
| DateOrder       | Order of day, month and year in the date or date part of a timestamp. Any existing separators such as ".", "-" or "/" are automatically recognized. Valid values: dmy, mdy and ymd |
| AHTColumn       | Position of the column for the average processing time (AHT). If this value is not defined, the values are imported without conversion as whole numbers without decimal places     |
| TimeStampColumn | Position of the column with a DateTime timestamp, overwrites DateColumn (if configured)                                                                                            |

### Optional parameters

| Parameter      | Details                                                                                                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LogFile        | Addition for the default name of the log file                                                                                                                               |
| SubGroups      | All subordinate queue names available in the file, e.g. necessary if the group defines the location and there is a second column for the queue name, separated by semicolon |
| SubGroupColumn | Position of a queue name for more than one grouping level in the source file                                                                                                |

### Creating your configuration

After saving the general settings, the `isps_ul.ini` contains a new section with the name you defined for the external system. Add the parameters manually below the general parameters you have already entered. The parameters are entered with an equal sign and a value, e.g. HeaderLines=1.

It is best to proceed as follows:

1. Count the columns of your CSV file, starting with 1, to determine the column positions for the queue names, the date and the time. Configure these as _GroupColumn_, _DateColumn_ and _TimeColumn_. In case you use a datetime field, use _TimeStampColumn_.
2. Configure the parameters _HeaderLines_, _ColumnNames_, _Groups_, _DateOrder_, _AHTColumn_ and _Interval_.
3. Save the configuration.
4. Restart the 'ISPS XLink' service to apply the changes.
5. Open the Xlink interface 'isps_ul.exe' again.

A tree structure should now appear in the part of the user interface. This is generated from groups and the configured column positions. Start now to create the mapping<!--link ? -->, which is necessary for the first import.

## Import of agent status data

TimeLink imports data on agents such as logins and logouts, skills, and breaks. The interface recognizes the format of the CSV file via additional parameters.

### Required parameters

| Parameter                    | Details                                                                                                                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ActivityIdentifiers          | Activity IDs occurring in the file, separated by semicolon                                                                                                                                                                                                   |
| ActivityDescriptions         | Display names for the IDs defined in ActivityIdentifiers, separated by semicolon                                                                                                                                                                             |
| ActivityHeaderLines          | Number of header lines that are not read and imported                                                                                                                                                                                                        |
| ActivityTimeSpanType         | The import can be done with start time and duration (value 0), start and end time (value 1) or only with the start time (value 2) In the latter case, the next activity ends the previous one. With value 0 the parameter ActivityDurationColumn is required |
| ActivityColumn               | Column Position Activities ID                                                                                                                                                                                                                                |
| AgentColumn                  | Column Position Agent ID                                                                                                                                                                                                                                     |
| ActivityDateOrder            | Order of day, month and year in the date or date part of a timestamp. Any existing separators like ".", "-" or "/" are automatically recognized. Valid values: dmy, mdy and ymd                                                                              |
| ActivityStartDateColumn      | Column Position Start Date (with separate columns for date and time)                                                                                                                                                                                         |
| ActivityStartTimeColumn      | Column Position Start Time (with separate columns for date and time)                                                                                                                                                                                         |
| ActivityEndDateColumn        | Column Position End Date (with separate columns for date and time)                                                                                                                                                                                           |
| ActivityEndTimeColumn        | Column position end time (with separate columns for date and time)                                                                                                                                                                                           |
| ActivityStartTimeStampColumn | Column position start time and date (for common DateTime field)                                                                                                                                                                                              |
| ActivityEndTimeStampColumn   | Column position end time and date (for common DateTime field)                                                                                                                                                                                                |
| ActivityColumnNames          | names for all columns available in the file. Header can be used. Otherwise freely selectable. Separated by semicolon, e.g. AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT                                                                        |

### Creating your configuration

After saving the general settings, the `isps_ul.ini` contains a new section with the name you defined for the external system. Add the parameters manually below the general parameters you have already entered. The parameters are entered with an equal sign and a value, e.g. ActivityHeaderLines=1.

It is best to proceed as follows:

1. Count the columns of your CSV file, starting with 1, to determine the column positions for the activity and the agent ID. Configure them as _ActivityColumn_ and _AgentColumn_.
2. Configure _ActivityStartDateColumn_ and _ActivityEndDateColumn_ When using a DateTime field, use _ActivityStartTimeStampColumn_ and _ActivityEndTimeStampColumn_.
3. Configure _ActivityDateOrder_, _ActivityColumnNames_, _ActivityIdentifiers_ and \*ActivityDescriptions
4. Check if your file contains a column for start time and end time, start time and duration or just start time.
5. Configure _ActivityStartTimeColumn_, _ActivityEndTimeColumn_ and/or _ActivityDurationColumn_ according to point 4 When using DateTime fields, use _ActivityStartTimeStampColumn_ and/or _ActivityEndTimeStampColumn_.
6. Configure _ActivityTimeSpanType_.
7. Save the configuration.
8. Restart the 'ISPS Xlink' service to apply the changes.

The _Present_ activity (ID 1) will display new external activities in the _External System_ section.

## Examples

Below are some examples of CSV files and configurations.

### Call data (PhoneLink)

```
Queue;Date;Time;CallsOffered;CallsHandled;AHT
UHD_DE_IN;23.12.2014;08:00;1;0;0
UHD_DE_IN;23.12.2014;08:15;1;1;180
UHD_EN_IN;23.12.2014;08:30;1;1;150
UHD_EN_IN;23.12.2014;08:45;1;1;160
```

> Avoid importing multiple files containing the same data
>
> If your file contains a single line for each call, e.g. for 08:00, 08:01, 08:05, and 08:14, this data is written to the 08:00 interval because Xlink aggregates this raw data to intervals. Multiple files in a single import that contain the same data will result in unusually high values. To correct this, remove the duplicates or only import one file at a time by moving or deleting the import file after each import using the parameter _DeleteImportFiles_.

```
GroupColumn = 1
DateColumn = 2
TimeColumn = 3
SubGroupColumn = 0
SubGroups =
HeaderLines = 1
Interval = 15
AHTColumn = 6
ColumnNames = Queue;Date;Time;CallsOffered;CallsHandled;AHT
Groups = UHD_DE_IN;UHD_EN_IN;
DateOrder = dmy
```

### Agent data (TimeLink) with dateTime field

```
AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
1002;1;29/01/2014 08:00:00;29/01/2009 09:00:00;360
1006;2;29/01/2014 08:00:00;29/01/2009 09:00:00;370
1002;2;29/01/2014 09:00:00;29/01/2009 09:30:00;180
1006;1;29/01/2014 09:00:00;29/01/2009 10:00:00;210
```

```
ActivityHeaderLines=1
ActivityColumn=2
AgentColumn=1
ActivityStartTimeStampColumn=3
ActivityEndTimeStampColumn=4
ActivityTimeSpanType=1
ActivityIdentifiers=1;2
ActivityDescriptions=Activity_1;Activity_2
ActivityDateOrder=dmy
ActivityColumnNames=AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
```

### Agent Data with separate date and time

```
AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
1002;1;29/01/2014;08:00:00;29/01/2009;09:00:00;360
1006;2;29/01/2014;08:00:00;29/01/2009;09:00:00;370
1002;2;29/01/2014;09:00:00;29/01/2009;09:30:00;180
1006;1;29/01/2014;09:00:00;29/01/2009;10:00:00;210
```

```
ActivityHeaderLines=1
ActivityColumn=2
AgentColumn=1
ActivityStartDateColumn=3
ActivityStartTimeColumn=4
ActivityEndDateColumn=5
ActivityEndTimeColumn=6
ActivityTimeSpanType=1
ActivityIdentifiers=1;2
ActivityDescriptions=Activity_1;Activity_2
ActivityDateOrder=dmy
ActivityColumnNames=AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
```

### Complete configuration template

Finally, the complete configuration with all general settings and PhoneLink and TimeLink for copying:

```
Source=
Destination=
ActivitySource=
ActivityDestination=
Interval=15
TimeZone=0
Protocol=1
SeparatorCharacter=
ActivitySeparatorCharacter=
DeleteImportFiles=0
DeleteActivityImportFiles=0
HeaderLines=
ActivityHeaderLines=
GroupColumn=
DateColumn=
TimeColumn=
SubGroupColumn=
SubGroups=
HeaderLines=
Interval=
AHTColumn=
ColumnNames=Queue;Date;Time;CallsOffered;CallsHandled;AHT
Groups=
DateOrder=
ActivityColumn=
AgentColumn=
ActivityStartDateColumn=
ActivityStartTimeColumn=
ActivityEndDateColumn=
ActivityEndTimeColumn=
ActivityTimeSpanType=
ActivityIdentifiers=
ActivityDescriptions=
ActivityDateOrder=
ActivityColumnNames=AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
```

## Further steps

Before your first working data import, a further step called mapping is required, which is described in two separate articles:

- {% link_new PhoneLink mapping | features/acd-integration/xlink-mapping-telephony.md %}
- {% link_new TimeLink mapping | features/acd-integration/xlink-mapping-activities.md %}
