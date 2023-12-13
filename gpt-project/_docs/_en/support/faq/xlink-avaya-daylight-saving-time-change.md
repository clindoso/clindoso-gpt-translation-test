---
title: Correct the time offset after time changes (Avaya)
description: Your contact volumes or agent data are shifted due to the time change in spring and autumn? Correct the time zone offset used for the data import.
product_label:
  - on-premise
---

injixo displays data from your Avaya telephony system with a time delay after the time switch to summer or winter time, after the time change in autumn one hour too early, in spring one hour too late.

The examples used in the article are valid for Germany. The deviation from Coordinated Universal Time (UTC) is one hour (UTC+1) in winter and two hours (UTC+2) in summer.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

> Note
>
> The article refers exclusively to the Lucent/Avaya CMS interface and the problem described here only appears if your CMS database is set to UTC and time is not adjusted automatically.

## Cause

Your Avaya CMS system stores the data as follows:

- Call data in the local time zone from the PBX location.
- Agent data in UTC, regardless of winter or summer time and the location of the telephony system.

Call data is always correctly displayed. A time zone change automatically happens in the telephony system. Changing the TimeZone parameter to correct an offset is not required. However, the agent data must be shifted to the local time.

The Xlink parameter 'TimeZone' represents the offset in hours from UTC. In the Avaya interface, a value of 12 means no offset, a value of 11 represents an offset of one hour (UTC+1), 10 corrects an offset of two hours (UTC + 2).

If you only change the 'TimeZone' value to correct the agent data, your previously correct call data will be incorrectly shifted.

## Solution

Use the parameter 'TimeZone_TimeLink' instead of 'TimeZone'.
This works in the same way as 'TimeZone', but only applies to the import of agent data.
Add `TimeZone_TimeLink` to your isps_ul.ini if it is not available.

### Adjust the Xlink configuration

#### Daylight savings time

```
[Avaya_CMS]
...
TimeZone=12
TimeZone_TimeLink=10
...
```

#### Wintertime

```
[Avaya_CMS]
...
TimeZone=12
TimeZone_TimeLink=11
...
```

## Subsequent data correction

If the parameter 'TimeZone_TimeLink' is not changed until some time after the actual time change, imported data needs to be corrected for a certain period.

Unfortunately, this problem is pretty common, because the time changeover always happens on a weekend.

> Attention
>
> If data is not available before a certain date, a re-import as described below irreversably overwrites the data with zeros. If incorrect data is detected after a long period of time (> 30 days), make sure that your ACD still has data for the import period before re-importing.

Correct data that has already been incorrectly imported as follows:

1. Correct the parameter `TimeZone_TimeLink`.
2. Activate the option _Write zero values_ via isps_ul.ini; set `WriteAlways=1`.
3. Restart the _ISPS Xlink_ service.
4. Re-import data for the period showing wrong data, see the preceding note.
5. Deactivate _write zero values_ again via isps_ul.ini; set `WriteAlways=0`.
6. Restart the _ISPS Xlink_ service.

If _Write Zero Values_ remains activated, there is a risk that already imported data may be accidentally overwritten with zero values during future imports.
