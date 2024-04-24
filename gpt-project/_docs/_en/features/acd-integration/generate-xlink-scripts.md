---
title: Create Xlink scripts
product_label:
  - on-premise
description: Configure Xlink to correctly process contact data prior to import.
---

Import scripts determine how Xlink handles the data to be imported.

When mapping call data, you can automatically create scripts that sum up all associated ACD metrics and write them to the associated _WFM_{:.menu-item} queue value type combination.

Import scripts are created in the _BASIC_ programming language. The Xlink supports the dialect "Enable Basic".

Sometimes it may be necessary to create special scripts, e.g. for weekday or time dependent results or the calculation of averages. These cannot be created automatically and have to be customized by you.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## Create your own scripts

To create your own import script, you should always use _Create_{:.doc-button}. The script template is an ideal starting point for your own scripts.

### Example for a standard script with an assigned key figure

```
Dim Result As Long
Dim Weekday As Long
Dim Minutes As Long
Dim Para1 As Long

Sub Main()
  Result = Para1 * 100
End Sub
```

## Procedure area

You start the procedure area with the line `Sub Main()` and end the procedure with `End Sub`. Within the procedure area, you can freely program within the framework of the possibilities available in the Enable Basic scripting language.

## Variables

In the declaration area (lines beginning with `Dim`) all variables used within the script are defined. By defining, the variables are "made known" to the system.

### Predefined variables

There are a few predefined variables described below, whose names must not be changed, otherwise the Xlink cannot evaluate the result of the script procedure.

#### Result

The result of the script procedure is assigned here. To save storage space in the database, the variable can only contain integer values. Decimal places are not considered, but truncated. The result is multiplied by 100 before saving to _WFM_{:.menu-item} (`Result = Para1 * 100`). In this way, values such as "80,23" are converted to "8023" and can be stored as integers.

#### Para... (Para1, Para2 etc.)

Here, the values of the ACD metrics are assigned for the time interval for which the script is executed. This is done in the exact order in which ACD metrics are assigned to the WFM value type. The number of para-variables must be equal to the number of assigned ACD metrics.

#### Weekday

This variable is filled by the Xlink with a numerical value that represents the day of the week of the imported date. The counting of the weekdays starts at Sunday with 1. With these variables you can realize weekday dependent evaluations; so you can e.g. make the formula for the evaluation of the assigned ACD key figures dependent on the weekday.

##### Example for weekday-dependent calculation:

```
Dim Result As Long
Dim Weekday As Long
Dim Minutes As Long
Dim Para1 As Long
Dim Para2 As Long

Sub Main ()
  If (weekday = 2) Then
    Result = Para1 * 100
  else
    If (weekday = 3) Then
      Result = Para2 * 100
    else
      Result = (Para1 + Para2) * 100
    End If
  End If
End Sub
```

- Monday, the result is only the first key figure assigned.
- Tuesday, the result is only the second assigned key figure.
- On all other days, the result is the sum of the two key figures.

#### Minutes

This variable is filled by the Xlink with the start time of the interval for which the ACD key figures are imported. The time specification is "minutes since midnight" (i.e. 0 for 00:00, 60 for 01:00, etc.). The name of the variable is predefined and must not be changed by you. With this variable you can realize time-dependent evaluations. For example, you can ignore calls received outside a certain time window in the evaluation.

##### Example for minute-dependent calculation:

```
Dim Result As Long
Dim Weekday As Long
Dim Minutes As Long
Dim Para1 As Long

Sub Main ()
  If (minutes < 360) or (minutes >= 1200) Then
    Result = 0
  else
    Result = Para1 * 100
  End If
End Sub
```

- The result of the assigned key figure is used between 6 am and 8 pm.
- Before 6 a.m. and after 8 p.m., the result is 0.

#### Other examples

##### Example for threshold values

Threshold values can be used e.g. not to display certain volumes, or to perform a certain calculation for a certain number of calls, in the example below 20% will be added.

```
Sub Main ()
  If Para1 < 10 Then
    Result = 0
  else
    If Para1 > 1000
      Result = Para1 * 100 * 1.2
    else
      Result = Para1 * 100
    End If
  End If
End Sub
```

##### Average talk times

This type of calculation is usually used when the total talk time is available. The total talk time is divided by the number of calls processed.

> Using Division in Scripts
>
> If you use divisions, make sure not to divide by zero. This can be achieved by an if-then query. Attempting to divide by zero during script execution would cause the import process to terminate and possibly lead to a paradox in the space-time continuum!
>
> ```
> Sub Main ()
>   If Para2 = 0 Then
>     Result = 0
>   else
>     Result = (Para1/Para2) * 100
>   End If
> End Sub
> ```

### Custom variables

Of course you can also define your own variables, e.g. to save intermediate results or similar. You start the declaration with the keyword `Dim`, e.g. (`Dim intermediate result As Long`) The variable name must begin with a letter, may contain numbers beside letters and may not be identical with a reserved word of the programming language BASIC. Details about the available variable types can be found in the language reference of Enable Basic.

## Syntax check

By clicking the _Test_{:.doc-button} button you can perform a syntax check on the script you have created. The script is only checked for syntactic correctness, there is no check for mathematically invalid actions such as division by zero.

> Concluding notes
>
> Clamp replacement
>
> When using mixed additions, subtractions, multiplications and divisions, you must pay special attention to correct parentheses. The statement `Result = Para1 + Para2 * 100` will lead you to a different result than e.g. `Result (Para1 + Para2) * 100`.
>
> Script output used in test only
>
> When a dialog or hint window appears, the script execution and thus the import is stopped until the user confirms it and only continued afterwards.
