---
title: Configure Time Off
description: Learn how to configure the time off that your employees can request.
product_label:
  - essential
  - advanced
  - enterprise
beta-feature: true
beta-feature: true
---

Time-off types and periods are prerequisites for people to create time-off requests in injixo Me.

A time-off type is an absence category. Your organization needs to use time-off types to distinguish between absences due to different reasons, such as sickness, vacation, or parental leave. For example, if your organization offers one day of leave per year for volunteering at an NGO, you can add the time-off type Volunteering leave.

A time-off period is a time period during which people can request time off. Time-off periods require a time-off type. Time-off types include entitlement periods, e.g. a vacation time-off type can have an entitlement period for each year. 

To set up your time off configuration, go to _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span> and click _Time-off configuration_{:.doc-button}.

## Create a time-off type

1. Click *New time-off type*{:.doc-button} on the right.
2. Enter the following information:
 - **Name**
 - **Paid**: Check this checkbox if people should get paid when they take this type of time off (e.g. sickness). 
     Depending on national legislation, some time-off types must be paid. 
 - **Time unit**: Select whether you want to calculate the time off taken in hours or days. 
     Depending on national legislation, it might be mandatory to calculate time off in hours or days.
 3. Click **Add entitlement period**.
 4. Select a **Start Date** and an **End Date**.
 5. Click *Create time-off type*{:.doc-button}.

> You cannot change the time unit after creating the time-off type.

## Edit a time-off type

1. Click the time-off type that you want to edit.
2. Edit the information.
3. Click *Save changes*{:.doc-button}.
   
## Delete a time-off type

1. Click the time-off type that you want to delete.
   You can only delete unused time-off types. If a person has already created a request using the time-off type, you cannot delete it.
2. Click _Delete time-off type_{:.doc-button}.

## Create a time-off period

A time-off period is a time period during which people can request time off. Time-off periods require a time-off type.

1. Click **Time-off Periods** on the left.
2. Click *Create time-off period*{:.doc-button}.
3. Configure the elements for the time-off period:
 - Select a **Planning Unit**. The planning unit cannot be edited later.
 - (Optional) Choose a **Selection**.
 - Select an **Activity**. <!-- time-off type... -->
 - Select a **Date range**.
 - Choose the **Deadline** until which people can request time off.
 - Set the **Status** of the time-off period:
      People can only request time off for time-off periods with the status **Published**.
4. Click *Save*{:.doc-button}.

## Edit a time-off period

1. Click **Time-off Periods** on the left.
2. Hover over one time-off period and click the {% icon pencil %} on the right.
3. Edit the information you want to change and click *Save*{:.doc-button}.

## Delete a time-off period

1. Click **Time-off Periods** on the left.
2. Select the time-off period that you want to delete.
3. Click *Delete entries*{:.doc-button}.

> If you delete a time-off period for which requests already exist, the existing requests will remain. 
>
>You can still approve or reject these requests.

## Personal balances

For each person, you must define a yearly entitlement for each time-off type you offer. To define personal balances for your people, you first need to configure at least one time-off type, and that time-off type must have at least one entitlement period.

1. Go to _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span>.
2. Click _Personal balances_{:.doc-button}.
3. Select or search for the person whose balance you want to edit.
    Make sure you have selected the planning unit to which the person belongs.
4. Select a **Time-off type** and an **Entitlement period**.
5. In the **Remaining** panel on the right, click the {% icon pencil %} next to **Entitlement**.
6. Enter a number for the **New entitlement** and a **Reason for the change**.
7. Click _Save change_{:.doc-button}.
   All changes and reasons will be recorded in the table overview.

If you need to edit a person's taken time off, click the {% icon pencil %} next to **Taken** in the **Remaining panel**.
Editing a person's taken time off may be necessary for technical reasons or if you accidentally granted too much time off.
