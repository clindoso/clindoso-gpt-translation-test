---
title: Xlink interface configuration examples
permalink: xlink-sample-configurations/
permalink_reason: article is used in injixo.com/downloads
product_label:
  - on-premise
description: Use a collection of Xlink sample configurations to help configure your Xlink installation.
---

<!-- vale off -->

The following configurations are samples for the external system section in the `isps_ul.ini` file of your Xlink installation to import _contact data_.

Create an external system in injixo. Make sure to name it using the name (in brackets) in the section of the sample file for your ACD.

There are different types, universal and standard interfaces:

- Standard interface means that you need to select the specific ACD from the list of external systems.
- Universal means that you need to select the Universal interface.

<!-- fix formatting with this hint box -->

> Hint
>
> Each non-CSV interface needs an odbc connection, see Xlink documentation for more details.

## Call data import (PhoneLink)

At least the _PhoneLink_ checkbox must be checked to run Xlink using those configurations.

### Basic CSV interface example

```
[CSV]
TimeZone=
Protocol=
Source=
Destination=
SeparatorCharacter=2
DeleteImportFiles=2
ColumnNames=
HeaderLines=
DateColumn=
TimeColumn=
DateOrder=
GroupColumn=3
Groups=x;y;z
AHTColumn=
```

### Basic IPFX CSV interface

CSV interface

```
[IPFX_CSV]
Groups=
ColumnNames=Data;Time;QueueID;CallsOffered;CallsAbandoned;AvgAnswerTime;AvgCallTime;AvgWrapupTime;SLA_percent
Interval=15
TimeZone=0
Protocol=0
LogFile=IPFX_CSV
DateColumn=1
TimeColumn=2
GroupColumn=3
DateOrder=mdy
HeaderLines=0
Source=
Destination=
SeparatorCharacter=2
DeleteImportFiles=2
ActivitySource=
ActivityDestination=
ActivitySeparatorCharacter=0
DeleteActivityImportFiles=0
```

### Cisco UCCX

Standard Cisco UCCX interface

```
[Cisco UCCX]
Source=
User=
Password=
Interval=30
TimeZone=0
Protocol=0
LogFile=SS_Cisco
ContactServiceQueueTable=ContactServiceQueue
ContactQueueDetailTable=ContactQueueDetail
ContactCallDetailTable=ContactCallDetail
AgentConnectionDetailTable=AgentConnectionDetail
QueueFilter=0
```

### Cisco ICM

Standard Cisco ICM interface

```
[Cisco ICM]
Source=
User=
Password=
Interval=
TimeZone=0
Protocol=0
LogDir=
LogFile=
CallDataTableName=t_Call_Type_Half_Hour
ImportWhenNoCallsRouted=1
AgentEventDetailTableName=Agent_Event_Detail
AgentTableName=Agent
ReasonCodeTableName=Reason_Code
AgentIdColumn=PersonID
OverNightActivity=1
```

### Avaya CMS

Standard Lucent CMS Interface

```
[Avaya CMS]
Source=
User=
Password=
Interval=
TimeZone=12
Protocol=0
IgnoreBreaks=0
ActivityDetails=0
IncludeWorkmodeForAgent=0
LoadAllAgentActivities=1
MinimumActivityDuration=0
LogDir=
LogFile=
SplitAdditionalFields=
SplitAdditionalFieldsSize=255
VDNAdditionalFields=
VDNAdditionalFieldsSize=255
#TimeZone_TimeLink=12
DisplayVDNValue=0
DeactivateTimelinkImportYesterday=0
UseOpenEndTime=1
```

### Avaya Aura/Nortel Symposium Universal

Universal interface

```
[Avaya Aura]
;universal connection - pre April 2018
Source=Avaya Aura
User=
Pwd=
Protocol=1
QueueSQL=select Name from Application order by Name
QueueMappingSQL=select Name, ApplicationID from Application order by Name
ValueTypes=CallsOffered;TalkTime;WaitTime;PostCallProcessingTime;CallsAnswered
TimeStampColumn=""Timestamp""
TimeStampType=2
QueueNameColumn=ApplicationID
QueueNameType=1
RetrieveValueTypesUsing=1
CallDataTable=iApplicationStat
```

### Avaya Aura/Nortel Symposium Standard interface

Standard Nortel Symposium interface

```
[Avaya Aura] Backup
Source=
User=
Password=
LogDir=
LogFile=
ApplicationStat=iApplicationStat
AgentApplicationStat=iAgentByApplicationStat
AgentPerformanceStat=iAgentPerformanceStat
SkillSetStat=iSkillsetStat
AgentLoginStat=eAgentLoginStat
NotReadyTime=NotReadyTime
Protocol=1
IntervalDuration=15
NotReadyTime=PostCallProcessingTime
TalkTime=TalkTime
AgentLoginStat=eAgentLoginStat
CdnStat=iCDNStat
AgentBySkillSetStat=AgentBySkillsetStat
```

### Avaya Aura/Nortel Symposium Standard interface TalkTime

Standard Nortel Symposium interface

```
[Avaya Aura]
Source=
User=
Password=
IntervalDuration=15
Protocol=0
LogDir=
LogFile=talktime
Timezone=0
QueueSQL=select distinct (convert(char(5),SkillsetID)+"="+Skillset)  from iSkillsetStat where ApplicationID > 10000
QueueMappingSQL=SELECT DISTINCT  (convert(char(5),SkillsetID)+"="+Skillset), SkillsetID FROM iSkillsetStat iSkillsetStat WHERE (iSkillsetStat.ApplicationID>10000)
QueueNameType=1
QueueNameColumn=SkillsetID
RetrieveValueTypesUsing=1
CallDataTable=iSkillsetStat
TimeStampColumn=Timestamp
TimeStampType=2
ValueTypes=TalkTime
```

### Avaya Aura AACC6

Standard Nortel Symposium interface

```
[Avaya Aura AACC6]
Source=
User=
Password=
LogDir=
LogFile=calldata
ApplicationStat=iApplicationStat
AgentApplicationStat=iAgentByApplicationStat
AgentPerformanceStat=iAgentPerformanceStat
SkillSetStat=iSkillsetStat
AgentLoginStat=eAgentLoginStat
NotReadyTime=NotReadyTime
Protocol=0
IntervalDuration=15
NotReadyTime=PostCallProcessingTime
TalkTime=TalkTime
AgentLoginStat=eAgentLoginStat
CdnStat=iCDNStat
AgentBySkillSetStat=AgentBySkillsetStat
Pwd=$$$:4cdNGNkbm9ydGVs
ActivityCodeStat=iActivityCodeStat
NIActivityCode=CCMS.NIActivityCode
AgentImportMode=0
IncludeNotReadyCodes=0
MaximumActivityDuration=0
SequenceNumberSupported=0
```

### Avaya Aura AACC6 TalkTime Universal

Universal interface

```
[Avaya Aura]
Source=
User=
Password=
IntervalDuration=15
Protocol=0
LogDir=
LogFile=talktime
Timezone=0
QueueSQL=select distinct( string(convert(varchar(5),SkillsetID),'=',Skillset) ) from iSkillsetStat where ApplicationID > 10000
QueueMappingSQL=select distinct( string(convert(varchar(5),SkillsetID),'=',Skillset) ),SkillSetID
QueueNameType=1
QueueNameColumn=SkillsetID
RetrieveValueTypesUsing=1
CallDataTable=iSkillsetStat
TimeStampColumn=iSkillsetStat.Timestamp
TimeStampType=2
ValueTypes=TalkTime;NotReadyTime
```

### Shoretel ODBC

Universal interface

```
[Shoretel ODBC]
Source=
User=
Password=
TimeZone=0
Interval=15
Protocol=1
CallDataTable=ecc.grp_dmno
QueueSQL=SELECT g_name FROM ecc.grp
QueueMappingSQL=SELECT g_name,group_id FROM ecc.grp
QueueNameColumn=group_id;g_name
QueueNameType=0;1
RetrieveValueTypesUsing=1
TimeStampColumn=(unix_timestamp(dmn_date)+(dmn_time*60))
TimeStampType=1
ValueTypes=dmn_offered_calls;dmn_grp_abndn;dmn_grp_answered;dmn_talk_time;dmn_wrap_up_time;dmn_hold_time
```

### VoltDelta/Oasis <= V10

Universal interface

```
[Voltdelta]
Source=
User=
Password=
TimeZone=0
Protocol=1
CallDataTable=wfm_s_vrQueueLog
QueueSQL=select distinct(cast(Name as varchar)) FROM prf_vrCallTypes;
QueueMappingSQL=select distinct(cast(Name as varchar)),cast(CallTypeId as int) from prf_vrCallTypes;
TimeStampColumn=PeriodStartDateTimeOrig
QueueNameColumn=cast(CallTypeId as int);Name
QueueNameType=1;0
RetrieveValueTypesUsing=1
ValueTypes=NumberCalls;NumberAbandoned;NumberAnswered;WrapUpDuration;CumQueuingDuration;CumActiveHandlingDuration
```

### VoltDelta/Oasis > V11

Universal interface

```
[Voltdelta]
Source=Oasis
User=xxx
Pwd=xxx
CallDataTable=wfm_s_vwQueueLog
QueueSQL=select distinct cast(QueueName as varchar) as a FROM wfm_s_vwQueueLog order by a asc;
TimeStampColumn=PeriodStartDateTimeOrig
QueueNameColumn=QueueName
ValueTypes=NumberCalls;NumberAbandoned;NumberAnswered;WrapUpDuration;CumQueuingDuration;CumActiveHandlingDuration
Interval=15
```

### Vocalcom

Standard Vocalcom interface

```
[Vocalcom]
Source=
User=
Password=
AdminSource=
AdminUser=
AdminPassword=
Interval=
CreateLogFiles=
LogFile=
LogDir=
CustomerID=
MinimumActivityDuration=
```

### Siemens Hipath

Standard Siemens Hipath interface

```
[Siemans HiPath]
Source=
User=
Password=
DataSourceType=
ACDVersion=
Interval=
TimeZone=
Protocol=
LogDir=
LogFile=
CallDataTableName=CallRecord
AgentDataTableName=AgentRecord
GroupingQueue=QDNIS
GroupingQueueType=1
FlexRoutingValue=1
AgentImportActivityType=0
UseDisconnectTime=0
```

### Mitel (cmdata V7 and V8)

Universal interface

Use the CMDATA database v7 and v8.

```
[Mitel]
; please
Source=
User=
Password=
Interval=15
TimeZone=0
Protocol=0
LogDir=c:\xlink
LogFile=Mitellog
QueueSQL=SELECT distinct QueueName FROM QueuePerformanceByPeriodStats
CallDataTable=QueuePerformanceByPeriodStats
ValueTypes=QueueOffered;QueueAnswered;QueueAbandoned;QueueTalkTimeTotal;QueueTimeToAnswerTotal;QueueTimeToAbandonTotal;QueueServiceCount;QueueShortAbandoned
TimeStampColumn=MidnightStartDate
TimeStampType=2
QueueNameColumn=QueueName
```

### Mitel (cmdata post V9)

Universal interface

Use the CMDATA database post v9 and newer.

```
[Mitel]
Source=
User=
Password=
Interval=15
TimeZone=0
Protocol=0
LogDir=c:\xlink
LogFile=Mitellog
QueueSQL=SELECT distinct QueueName FROM QueuePerformanceByPeriodStats
CallDataTable=QueuePerformanceByPeriodStats
ValueTypes=QueueOffered;QueueAnswered;QueueAbandoned;QueueTotalTalkTime;QueueTimeToAnswerTotal;QueueTimeToAbandonTotal;QueueServiceCount;QueueShortAbandoned
TimeStampColumn=MidnightStartDate
TimeStampType=2
QueueNameColumn=QueueName
```

### Mitel Non Voice (cmdata post V9)

Universal interface

Use CMDATA database post v9 and newer.

```
[Mitel Non Voice]
Source=
User=
Password=
Interval=15
TimeZone=00:00
Protocol=1
LogDir=c:\xlink
LogFile=Mitelnonvoicelog
QueueSQL=SELECT distinct [Name] FROM tblConfig_Queue
CallDataTable=tblData_MCC_QueuePerformanceByPeriod t1 LEFT OUTER JOIN tblConfig_Queue b ON t1.FKQueue = b.PKey
ValueTypes=Offered;DeliveredToQueue;ReadingCount;ReadingTimeToAnswer;ServiceCount;ReadingDuration;CompletedCount;CompletedTimeToAnswer;CompletedDuration;HoldCount;HoldDuration;RepliedTo;NoReplyNeeded;JunkCount;ContinuingCase
TimeStampColumn= convert(datetime,stuff(stuff(stuff(cast(concat(cast(t1.DateKey as varchar), case when len(t1.TimeKey) < 6 then concat('0',CAST(t1.TimeKey as varchar)) else CAST(t1.TimeKey as varchar) end) as varchar),13,0,':'), 11, 0, ':'),9,0,' '))
TimeStampType=2
```

### Mitel Non Voice (cmdata pre V7)

Universal interface

Use the CMDATA database v7 and v8.

```
[Mitel]
Source=
User=
Password=
Interval=15
TimeZone=0
Protocol=0
LogDir=c:\xlink
LogFile=Mitellog
QueueSQL=SELECT distinct QueueName FROM QueuePerformanceByPeriodStats
CallDataTable=QueuePerformanceByPeriodStats
ValueTypes=QueueOffered;QueueAnswered;QueueAbandoned;QueueTotalTalkTime;QueueTimeToAnswerTotal;QueueTimeToAbandonTotal;QueueServiceCount;QueueShortAbandoned
TimeStampColumn=MidnightStartDate
TimeStampType=2
QueueNameColumn=QueueName
```

### Interactive Intelligence

Standard Interactive Intelligence interface

```
[InIn]
Source=
User=
Password=
Interval=
TimeZone=12
Protocol=0
LogDir=c:\xlink\log
LogFile=xlinklog
CallDataTableName=IWrkgrpQueueStats
AgentActivityTableName=AgentActivityLog
AgentMappingFile=
```

### Alcatel

Standard Alcatel interface

```
[Alcatel]
LogDir=c:\xlink
LogFile=Alcatellog
AcdDataPath=(eneter here where the IEX reports are coming from - the directory)
AcdProtocol=(enter the path inc filename of the config file created above)
AcdReportFormat=0 (0=iex format)
```

### Asterisk

Universal interface

```
[AsteriskODBC]
Source=
User=
Password=
TimeZone=0
Protocol=0
QueueSQL=SELECT DISTINCT queue FROM queue_log
QueueNameColumn=(verb like "ENTERQUEUE") AND queue
TimeStampColumn=time_id
TimeStampType=1
ValueTypes=
ValueTypeFunctions=count
```

### Avaya IP Office

Universal interface

#### ApplicationLevel

```
[AvayaIPOffice ApplicationLevel]
Source=
User=
Password=
TimeZone=0
Protocol=1
CallDataTable=stat.NIiAppStat
QueueSQL=SELECT ccms.NIApplication."Name" FROM ccms.NIApplication order by ccms.NIApplication."Name"
QueueMappingSQL=SELECT ccms.NIApplication."Name", ccms.NIApplication.ApplicationID FROM ccms.NIApplication
QueueNameColumn= ApplicationID;"Name"
QueueNameType=0;1
RetrieveValueTypesUsing=1
TimeStampColumn=statTimestamp
TimeStampType=2
ValueTypes=CallsAbandoned;CallsAnswered;CallsOffered;WaitTime;TalkTime;PostCallProcessingTime
```

#### SkillLevel

```
[AvayaIPOffice SkillLevel]
Source=
User=
Password=
TimeZone=0
Protocol=1
CallDataTable=stat.NIiSkillsetStat
QueueSQL=SELECT "Name" FROM ccms.NISkillset order by "Name" asc
QueueMappingSQL=SELECT "Name", SkillSetID FROM ccms.NISkillset
QueueNameColumn= SkillSetID;"Name"
QueueNameType=0;1
RetrieveValueTypesUsing=1
TimeStampColumn=statTimestamp
TimeStampType=2
ValueTypes=SkillSetAbandoned;CallsAnswered;CallsOffered;WaitTime;TalkTime;PostCallProcessingTime
```

### Ctalk

Universal interface

```
[Ctalk]
Source=
User=
Password=
;TimeZone=00:00
Protocol=0
Interval=15
TimeZone=0
QueueSQL=select distinct (QueueID)  from QueueStats order by QueueID asc
Calldatatable=QueueStats
QueueNameColumn=QueueID
TimeStampColumn=DATEADD(minute,-15,CreatedDateTime)
TimeStampType=2
ValueTypes=Offered;AHT;Abandoned;GOS;HandledThisQueue
ActivitySQL=SELECT DISTINCT StatusDescription, StatusID FROM StatusDescription
ActivityTimeSpanType = 2
ActivityColumn=StatusID
AgentColumn=AgentID
ActivityStartTimeStampColumn=CreatedDateTime
ActivityStartTimeStampType=2
AgentActivityTable=AgentActivity
LogOffActivities=0
```

### Siemens Openscape

Universal interface

```
[Openscape]
Source=
User=
Password=
TimeZone=0
Protocol=0
QueueSQL=select calltypename from calltypes order by calltypename
QueueMappingSQL=select calltypename,calltypekey from calltypes order by calltypekey
QueueNameType=0;1
RetrieveValueTypesUsing=1
CallDataTable=calltypefifteenmin
ValueTypes=numreceived;numansweredprim;numabandoned;ansunderthreshold;abnunderthreshold;totanswaittime;totabanwaittime;totwaittime;totcontacttime;totdefertime;totpostprocessingcontacttime
ValueTypesSize=1024
TimeStampColumn=recordtimestamp
QueueNameColumn=calltypekey
```

### 8x8 ECN CSV interface

Universal interface

```
[8x8 ECN CSV]
Source=
Destination=
HeaderLines=1
DateColumn=1
DateOrder=ymd
TimeColumn=2
GroupColumn=3
Groups=Call Centre;Cancellations Team;Customer Complaints Team;E Validation;EWUK or Sales Complaints;New Registration Team;Revenue Protection;Sales Complaints;SMART;SMART Engineer Overflow;Smart Team;STANDARD
ColumnNames=Date;Interval;Queue;Offered;Answered;Abandoned;AHT;ASA;SLA
Interval=15
TimeZone=0
Protocol=0
LogFile=CSVlog
SeparatorCharacter=2
DeleteImportFiles=2
ActivitySource=
ActivityDestination=
ActivitySeparatorCharacter=2
DeleteActivityImportFiles=2
ActivityIdentifiers=1;2;3;4;5;6;7;8;9
ActivityDescriptions=Wrap;Wait;Call;TPT;Dial;Hold;Listen;Ringing;Preview
ActivityHeaderLines=1
ActivityTimeSpanType=1
ActivityColumn=2
AgentColumn=1
ActivityStartTimeStampColumn=3;4
ActivityStartTimeStampFormat=yyyy-mm-dd;HH:MM:SS
ActivityEndTimeStampColumn= 5;6
ActivityEndTimeStampFormat=yyyy-mm-dd;HH:MM:SS
```

### ipScape CSV interface

CSV interface

```
[ipScape]
Source=
Destination=
HeaderLines=1
ColumnNames=Date;Interval Start;Queue;Calls Offered;Calls Answered;Calls Abandoned;Average Handle Time;Average Speed of Answer;Service Level
DateColumn=1
DateOrder=ymd
TimeColumn=2
GroupColumn=3
Groups=
Interval=15
TimeZone=0
Protocol=0
LogFile=CSVlog
SeparatorCharacter=2
DeleteImportFiles=2
ActivitySource=
ActivityDestination=
ActivitySeparatorCharacter=2
DeleteActivityImportFiles=2
ActivityIdentifiers=1;2;3;4;5;6;7;8;9;10;11;12;13
ActivityDescriptions=Login;Waiting;Talk;Wrap;Pause;Logout;Preview;Dial;Manual Preview;Hold;Auto Logout;Email;Chat
ActivityHeaderLines=1
ActivityTimeSpanType=1
ActivityColumn=2
AgentColumn=1
ActivityStartTimeStampColumn=3;4
ActivityStartTimeStampFormat=yyyy/mm/dd;HH:MM:SS
ActivityEndTimeStampColumn=5;6
ActivityEndTimeStampFormat=yyyy/mm/dd;HH:MM:SS
```

### Rostrvm CSV interface

CSV interface

```
[Rostrvm]
Source=
Destination=
HeaderLines=1
ColumnNames=Date;Interval Start;Queue;Inbound Calls Offered;Inbound Calls Answered;Inbound Calls Abandoned;Inbound Average Handling Time;Inbound Average Speed of Answer;WebChat Calls Offered;WebChat Calls Answered;WebChat Calls Abandoned;WebChat Average Handling Time;WebChat Average Speed of Answer;Email Calls Offered;Email Calls Answered;Email Calls Abandoned;Email Average Handling Time;Email Average Speed of Answer;Outbound Contacts Offered;Outbound Non Successful Contacts;Outbound RP Connect Rate;Outbound RPC AHT;Outbound RPC Successful;Outbound WPC AHT;Outbound WPC Successful
DateColumn=1
DateOrder=dmy
TimeColumn=2
GroupColumn=3
Groups=
Interval=15
TimeZone=0
Protocol=0
LogFile=CSVlog
SeparatorCharacter=2
DeleteImportFiles=2
ActivitySource=
ActivityDestination=
ActivitySeparatorCharacter=2
DeleteActivityImportFiles=2
ActivityIdentifiers=0;1;2;3;4;5
ActivityDescriptions=not ready;ready;busy;wrap;preview;logoff
ActivityHeaderLines=1
ActivityTimeSpanType=1
ActivityColumn=2
AgentColumn=1
ActivityStartTimeStampColumn=3;4
ActivityStartTimeStampFormat=dd/mm/yyyy;HH:MM:SS
ActivityEndTimeStampColumn=5;6
ActivityEndTimeStampFormat=dd/mm/yyyy;HH:MM:SS
```

### Zeacom

Universal interface

```
[Zeacom]
Source=
User=
Password=
Interval=15
TimeZone=00:00
Protocol=1
LogDir=
LogFile=Zeacom
QueueSQL=Select distinct Queue from AUDITsummary
CallDataTable=AUDITCALLS
ValueTypes=(case when Resolution='Abandoned' OR Resolution='Queue Call' OR Resolution='Callback lodged' then 1 else null end);(case when Resolution='Queue Call' then 1 else null end);TalkTime;HoldTime
ValueTypeFunctions=count
TimeStampColumn=CallDateTime
TimeStampType=2
QueueNameColumn=QueueNumber
ActivitySQL=SELECT BreakReason,AgentID from (values('Coffee Break',1),('Lunch60',2),('Toilet',3),('Lunch30',4),('Supervisory',5),('Meeting',6),('2IC',7), ('Training',8), ('PC/Profile Issue',9) )  as x(BreakReason,AgentID)
ActivityTimeSpanType=0
ActivityColumn=BreakReason
AgentColumn=AgentID
ActivityStartTimeStampColumn=LoginDateTime
ActivityDurationColumn=Duration
ActivityEndTimeStampType=2
AgentActivityTable=LOGIN
```

## Agent Data Import (TimeLink)

The following configurations are samples for the external system section in the `isps_ul.ini` file of your Xlink installation to import _agent data_.

Create an external system in injixo which has the same name as the section in the corresponding example matching your ACD.

At least the _TimeLink_ checkbox must be checked to run Xlink using those configurations.

Each interface needs an odbc connection, see Xlink documenation for more details.

### Anywhere 365

```
[Anywhere365]
QueueSQL=select distinct skillChosen FROM UCC_CallSummary where len(skillChosen) > 0
CallDataTable= injixo_calls
ValueTypes=Offered;Accepted;HandleTime
TimeStampColumn=Timestamp
QueueNameColumn=Queue
TimeStampType=2
ActivitySQL=SELECT distinct ReasonCodeName, ReasonCode FROM injixo_presence where ReasonCode > 0
ActivityTimeSpanType=2
AgentColumn=sipmapid
ActivityColumn=ReasonCode
AgentActivityTable=injixo_presence
ActivityStartTimeStampType=2
ActivityStartTimeStampColumn=[time]
;ActivityDurationColumn=
;MinimumActivityDuration=0
LogOffActivities=10
```

**SQL views for Anywhere365**:

```
create view injixo_calls as
SELECT inqueuetime as Timestamp, IIF(inqueuetime > '2000-01-01 00:00:00',1,0) as Offered, IIF(accepted=1,1,0) as Accepted, IIF(handled=1,1,0) as Handled, IIF(mcRemoved=1,1,0) as Abandoned, skillChosen as Queue,IIF(acceptedtime > '2000-01-01 00:00:00',DateDiff(ss,acceptedtime,endtime),0) as HandleTime FROM UCC_CallSummary where ucc_id = 2
```

### BT - Cisco

Universal interface

```
BT - Cisco**
[BT_Cisco]
Interval=15
TimeZone=00:00
Protocol=0
QueueSQL = select distinct EnterpriseName from Call_Type order by EnterpriseName asc
QueueSQLSize=512
ValueTypes=a.CallsOfferedRouted;a.CallsAnswered;a.HandleTime
CallDataTable=Call_Type_SG_Interval a LEFT OUTER JOIN Call_Type b ON a.CallTypeID = b.CallTypeID
ValueTypeSize=512
TimeStampColumn=a.DateTime
QueueNameColumn= b.EnterpriseName
QueueMappingSQLSize=512
AgentActivityTable= Agent INNER JOIN Agent_Event_Detail ON Agent.SkillTargetID = Agent_Event_Detail.SkillTargetID
AgentColumn=PeripheralNumber
ActivityColumn=ReasonCode
ActivityStartTimeStampColumn=DateTime
ActivityStartTimeStampType=2
ActivitySQL=select ReasonText, ReasonCode FROM Reason_Code where Deleted = 'N'
ActivityTimeSpanType=2
LogOffActivities=0;19
```

### Cisco UCCX

Universal interface

```
[Cisco UCCX Agents]
Source=
User=
Password=
Interval=1
TimeZone=0
Protocol=0
LogOffActivities=2;7
ActivityTimeSpanType=2
AgentColumn=extension
AgentActivityTable= Resource INNER JOIN AgentStateDetail ON Resource.resourceID = AgentStateDetail.agentId
ActivityColumn=CONCAT(CAST(eventtype AS CHAR),reasoncode)
ActivityStartTimeStampColumn=eventdatetime
ActivityStartTimeStampType=2
ActivitySQL=SELECT DISTINCT(CONCAT(CAST(eventtype AS CHAR),reasoncode)),(CONCAT(CAST(eventtype AS CHAR),reasoncode)) FROM AgentStateDetail
```

### Cisco UCCX V2

Universal interface

```
[Cisco UCCX Agents]
Source=
User=
Password=
Interval=1
TimeZone=0
Protocol=1
LogOffActivities=2;7
ActivityTimeSpanType=2
AgentColumn=extension
AgentActivityTable= Resource INNER JOIN AgentStateDetail ON Resource.resourceID = AgentStateDetail.agentId
ActivityColumn=CONCAT(CAST(eventtype AS CHAR),reasoncode)
ActivityStartTimeStampColumn=eventdatetime
ActivityStartTimeStampType=2
ActivitySQL=SELECT DISTINCT(CONCAT(CAST(eventtype AS CHAR),reasoncode)),(CONCAT(CAST(eventtype AS CHAR),reasoncode)) FROM AgentStateDetail WHERE (EVENTDATETIME BETWEEN TODAY AND TODAY + 30 UNITS DAY) AND (reasoncode < 100)
```

### Avaya Aura/Nortel Symposium

Universal interface

```
[Avaya Aura]
;universal connection - pre April 2018
Source=Avaya Aura
User=
Pwd=
Protocol=1
QueueSQL=select Name from Application order by Name
QueueMappingSQL=select Name, ApplicationID from Application order by Name
ValueTypes=CallsOffered;TalkTime;WaitTime;PostCallProcessingTime;CallsAnswered
TimeStampColumn=""Timestamp""
TimeStampType=2
QueueNameColumn=ApplicationID
QueueNameType=1
RetrieveValueTypesUsing=1
CallDataTable=iApplicationStat
```

### CSV interface Agents

CSV interface

```
[CSV]
ActivitySource=
ActivityDestination=
ActivitySeparatorCharacter=2
DeleteActivityImportFiles=2
ActivityColumnNames=Agent;Activity;StartDate;StartTime;EndDate;EndTime;Duration
ActivityIdentifiers=
ActivityDescriptions=
ActivityHeaderLines=
AgentColumn=
ActivityColumn=
ActivityStartTimeStampColumn=3;4
ActivityEndTimeStampColumn=5;6
ActivityStartTimeStampFormat=mm/dd/yy;HH:MM:SS
ActivityTimeSpanType=1
```

### Avaya Aura/Nortel Symposium

Universal interface

```
[Avaya Aura]
Source=ConnectionName
User=
Pwd=
IntervalDuration=15
Protocol=1
TimeZone=12
LogFile=
ActivitySQL=SELECT EventType, ASCII(RIGHT(EventType, 1)) as EventType_ID from eAgentLoginStat group by EventType
ActivityTimeSpanType=2
Agentcolumn=AgentLogin
ActivityColumn='"EventType"'
ActivityStartTimeStampColumn='"Timestamp"'
AgentActivityTable=eAgentLoginStat
ActivityStartTimeStampType=2
ActivityStartTimeStampFormat=yyyy-mm-dd HH:MM:SS
```

### BT Cloud Cisco

Universal interface

```
[BT Cloud Cisco]
AgentActivityTable= Agent INNER JOIN Agent_Real_Time ON Agent.SkillTargetID = Agent_Real_Time.SkillTargetID
AgentColumn=PeripheralNumber
ActivityColumn=IIF(AgentState = 2, ReasonCode, (1000*AgentState))
ActivityStartTimeStampColumn=DateTime
ActivityStartTimeStampType=2
ActivitySQL=select * FROM (values ('LoggedOn',1000),('NotReady',2000),('Ready',3000),('Talking',4000),('Work Not Ready',5000),('WorkReady',6000),('Call on Hold',10000)) v(ReasonText,ReasonCode) union all (select ReasonText, ReasonCode FROM Reason_Code where Deleted = 'N')
ActivitySQLSize=1024
ActivityTimeSpanType=2
LogOffActivities=0;19
```

### Contivio

Universal interface

```
QueueSQL = SELECT DISTINCT queue_campaign_name,media_type_id FROM CallRecords WHERE record_id = 0 ORDER by queue_campaign_name,media_type_id
QueueMappingSQL = SELECT DISTINCT queue_campaign_name,media_type_id,call_status_id FROM CallRecords WHERE record_id = 0 ORDER by queue_campaign_name,media_type_id,call_status_id
QueueNameColumn = queue_campaign_name;media_type_id;call_status_id
QueueNameType = 0;0;0
ValueTypes = (case when call_status_id = 0 then 1 else null end);(call_status_id);convert(int,handling_duration)
ValueTypeFunctions = SUM;COUNT;SUM
TimeStampColumn = call_start_time_utc
CallDataTable = CallRecords
ActivitySQL = SELECT DISTINCT Description,AvailabilityID FROM AvailabilityCodes ORDER by Description,AvailabilityID
ActivityTimeSpanType = 2
ActivityColumn = AvailabilityCode
AgentColumn = AgentID
ActivityStartTimeStampColumn = EventTimeUTC
ActivityStartTimeStampType = 2
AgentActivityTable = AgentAvailability
LogOffActivities = -200;-20;-5;-2
```

### Plivo

Universal Interface

```
[Plivo]
Source=
User=
Password=
TimeZone=00:00
Protocol=0
Interval=15
TimeZone=0
QueueSQL=select distinct queue_name FROM manage_plivo_call_log where queue_name is not null and created_at > '2020-07-01' order by queue_name
Calldatatable=manage_plivo_call_log
QueueNameColumn=queue_name
TimeStampColumn=created_at
TimeStampType=2
ValueTypes=1;IF(duration > 0,1,0);duration
ActivitySQL =
ActivityTimeSpanType = 2
ActivityColumn =
AgentColumn =
ActivityStartTimeStampColumn =
ActivityStartTimeStampType = 2
AgentActivityTable =
LogOffActivities=0
```

### Twilio Connected

Universal Interface

```
[Twilio-Connected]
Source=
User=
Password=
TimeZone=00:00
Protocol=1
Interval=15
TimeZone=0
QueueSQL=select distinct caller_connected_queue FROM manage_twilio_call_log where caller_connected_queue is not null and date > '2020-07-01' order by caller_connected_queue asc
Calldatatable=manage_twilio_call_log
QueueNameColumn=caller_connected_queue
TimeStampColumn=date
TimeStampType=2
ValueTypes=IF(call_type="INBOUND",1,0);IF(call_type="INBOUND" AND call_status= "ANSWERED-CALL-COMPLETED",1,0);call_duration
ActivitySQL =
ActivityTimeSpanType = 2
ActivityColumn =
AgentColumn =
ActivityStartTimeStampColumn =
ActivityStartTimeStampType = 2
AgentActivityTable =
LogOffActivities=0
```

### Twilio-Selected

Universal Interface

```
[Twilio-Selected]
Source=
User=
Password=
TimeZone=00:00
Protocol=0
Interval=15
TimeZone=0
QueueSQL=select distinct caller_selected_queue FROM manage_twilio_call_log where caller_selected_queue is not null and date > '2020-07-01' order by caller_selected_queue asc
Calldatatable=manage_twilio_call_log
QueueNameColumn=caller_selected_queue
TimeStampColumn=date
TimeStampType=2
ValueTypes=IF(call_type="INBOUND",1,0);IF(call_type="INBOUND" AND call_status= "ANSWERED-CALL-COMPLETED",1,0);call_duration
ActivitySQL =
ActivityTimeSpanType = 2
ActivityColumn =
AgentColumn =
ActivityStartTimeStampColumn =
ActivityStartTimeStampType = 2
AgentActivityTable =
LogOffActivities=0
```

## Agent Data Import (TimeLink RealTime)

The following configurations are samples for real time interfaces, those come along with their own executable and configuration file.

### Avaya CMS

Executable name: avayacms.exe
Configuration file: iwfm_avayacms.cfg

```
[RTA]
Username=xlink@xxxxxx
Password=
PortNumber=9669
; From Injixo, Admin > System > External Systems
ExternalSystem=avaya
ImportToLevel=5000
; available values
; 0(unknown), 20(avail), 30(acd), 40(ACW), 50(AUX), 60(DACD), 70(DACW), 80(RING), 220(other)

DetailedWorkmodes=30,40,50
AuxReasons=1:Lunch,2:Break,3:Meeting
Splits=11:Billing,12:Helpdesk,13:TechSup
LogFileDir=c:\xlink
; avaiable values
; Critical, Error, Warning, Notice, Info, Debug
LogLevel=critical
LogMaxSize=262144
BufferMaxSize=
TroubleRestarts=1
TroubleWaitTime=30000
```

### Cisco ICM RTA

Executable name: ciscorta.exe
Configuration file: iWFM_CiscoICM.cfg

```
[RTA]

Username = xlink@xxxx.com
Password = xxxxxxxx

PeripheralGateways= "PGone,PGtwo"
PGone = **IP Address here**
PGtwo = **IP Address here**

ExternalSystem = Cisco
ImportToLevel = 5000

CiscoClientId =
CiscoPassword =

LogFileDir = c:\xlink
LogLevel = debug
LoggingEnabled = 1
LogMaxSize = 262144
BufferMaxSize = 10240

TroubleRestarts = 1
TroubleWaitTime = 30000

AuxReasons = 0:Undefined,1:Break,2:Lunch,3:Authorised By Manager,4:Meeting, 5:Escalations,6:Offline Work,7:Live Chat,8:Coaching,9:Development,16:Outbound Call
```

### Twilio

```
[Twilio-RTA]
Source=
User=
Password=
TimeZone=00:00
Protocol=0
ActivitySQL=SELECT 'Idle',1 as Value UNION SELECT 'Offline',2 as Value UNION SELECT 'Reserved',3 as Value UNION SELECT 'Busy',4;
ActivityTimeSpanType=2
AgentColumn=b.id
ActivityStartTimeStampColumn=a.time_status_changed
AgentActivityTable= manage_twilio_agent_live_status a INNER JOIN manage_users b ON a.worker_sid = b.worker_sid
ActivityColumn=IF(a.activity_status = 'Idle',1,IF(a.activity_status = 'Offline',2,IF(a.activity_status = 'Reserved',3,IF(a.activity_status = 'Busy',4,0 ))))
```

<!-- vale on -->
