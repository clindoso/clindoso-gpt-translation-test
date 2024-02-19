---
title: Default user roles
description: Learn about the access rights of default user roles in injixo.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /user-roles-in-detail/
redirect_reason: Updated filename on 05 December 2022
---

## Default user roles

In each role category, injixo provides one default user role with pre-defined access rights. In injixo Advanced and Enterprise WFM, you can customize the default user roles and/or {% link_new add your own user roles | getting-started/configure-user-roles.md %}. Note: The Other role category does not have a default user role.

| **Role category**     | **Default access rights**                                                                                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent                 | Access to injixo Me, i.e., view shifts, request time off, bid on shifts, swap shifts.                                                                                                        |
| Planner               | Full access to all functionalities relevant to forecasting, scheduling, intraday management, and configuration data.                                                                         |
| Supervisor (basic)    | Read-only access to the Schedule level in {% link_new Schedules                                                                                                                              | features/scheduling/schedules/schedules-overview.md %} and {% link_new Shift Center | features/scheduling/shiftcenter/shift-center-overview.md %}. Access to {% link_new Exchange overview | features/scheduling/view-approve-shift-swap-requests.md %} and {% link_new Time Off | features/scheduling/time-off/vacation-absences-management.md %} to manage shift swaps and time-off requests. No access to configuration data. |
| Supervisor (advanced) | All functionalities of Supervisor (basic), full access to Shift Center and Schedules, permission to change schedules in intraday management, and full access to specific configuration data. |
| Trainer               | Access to Academy to facilitate training on injixo Me.                                                                                                                                       |
| Finance               | Access to user and billing information, as well as invoices for injixo services.                                                                                                             |

Note: The tables in this article list components and features for relevant default user roles. The green checkmark icon <i class="fa fa-check" style="color:#1cb396"></i> indicates full (read and write) access. Because your WFM plan also determines available functionality, you may not have access to every item listed.

## Access to components and features

Access the components in the main navigation and features with related functionalities under each menu item, both in bold below.

Note: injixo Classic contains all scheduling-related features under _Scheduling > SchedulePro_{:.breadcrumbs}. Refer to the [Access to features under WFM](#access-to-features-in-wfm) section for more injixo Classic features.

<div class="table__wrapper table__with-subsections" markdown="1">

|                                         |          Admin          |         Planner         |  Supervisor (advanced)  |   Supervisor (basic)    |
| --------------------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Forecast**                            |                         |                         |                         |                         |
| **Forecast**                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |        Read only        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Intraday**                            |                         |                         |                         |                         |
| **Real-Time Adherence**                 | <i class="fa fa-check"> |        Read only        |        Read only        |        Read only        |
| **Intraday Adherence**                  | <i class="fa fa-check"> |        Read only        |        Read only        |        Read only        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Plan**                                |                         |                         |                         |                         |
| **Schedules**                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |
| **Shift Center**                        | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |
| **Scheduling Periods**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Generate Shifts                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Start Shift Lottery                     | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Assign Shifts                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Adjust Shift Generation                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| **Scheduling Actions**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Insert Shift Sequences                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Create Optimized Schedule               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Job Optimization                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Optimize Breaks                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Schedule Extra Activities               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Replace Activities                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Empty Levels                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Copy Level Content                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Approve shift swaps                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |        Read only        |
| **Meetings**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Time Off**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |
| Time-Off Periods                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Edit Entitlement                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| **Configuration**                       |                         |                         |                         |                         |
| Skills                                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| --------------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Analyze**                             |                         |                         |                         |                         |
| **Dashboards**                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

## Access to account, user, and integration-related information

Click _Account_{:.menu-item} in the main navigation to access the features below.

<div class="table__wrapper table__with-subsections" markdown="1">

|                    |          Admin          |         Planner         |         Finance         |
| ------------------ | :---------------------: | :---------------------: | :---------------------: |
| **Account**        |                         |                         |                         |
| **User**           | <i class="fa fa-check"> |                         |                         |
| **User roles**     | <i class="fa fa-check"> |                         |                         |
| **Billing**        |                         |                         |                         |
| Subscription       | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Invoices           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Contacts           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Details            | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| **Administration** |                         |                         |                         |
| Company Details    | <i class="fa fa-check"> |                         |                         |
| **Integrations**   | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Security**       | <i class="fa fa-check"> |                         |                         |

</div>

## Access to features in WFM

Click _WFM_{:.menu-item} in the main navigation to access the features below.

Note: In injixo Advanced and Enterprise WFM, **Monitoring** and **Administration** are available. All other scheduling-related functionalities under _Scheduling > SchedulePro_{:.breadcrumbs} have been moved to _Plan > Schedules_{:.breadcrumbs} and _Plan > Time Off_{:.breadcrumbs}. Learn more in [Access to components and features](#access-to-components-and-features).

<div class="table__wrapper table__with-subsections" markdown="1">

|                                      |          Admin          |         Planner         |  Supervisor (advanced)  |   Supervisor (basic)    |
| ------------------------------------ | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Scheduling**                       |                         |                         |                         |                         |
| **SchedulePro**                      |                         |                         |                         |                         |
| Shift Center                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |
| Optimization                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Planning Periods                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Meeting Planner                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Insert Shift Sequences               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Shift Requirement                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Exchange Overview                    | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |        Read only        |
| **TimeManager**                      |                         |                         |                         |                         |
| Target Work Accounts                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Vacation Entitlement                 | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Monitoring**                       |                         |                         |                         |                         |
| Reports                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Administration**                   |                         |                         |                         |                         |
| **Scheduling**                       |                         |                         |                         |                         |
| Skills                               | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Activities                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Day Models                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Week Time Patterns                   | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Work Time Pattern Models             | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Shift Sequences                      | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Day Types                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Planning Units                       | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Planning Calendar                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Selections                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Contracts                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| Employees                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Read only        |                         |
| **Forecasting**                      |                         |                         |                         |                         |
| Event Types                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Queues                               | <i class="fa fa-check"> |        Read only        |                         |                         |
| **System**                           |                         |                         |                         |                         |
| Scheduling Rules                     | <i class="fa fa-check"> |        Read only        |                         |                         |
| Settings                             | <i class="fa fa-check"> |                         |                         |                         |
| External Systems                     | <i class="fa fa-check"> |                         |                         |                         |
| Role Authorization                   | <i class="fa fa-check"> |                         |                         |                         |
| User Authorization                   | <i class="fa fa-check"> |                         |                         |                         |
| JobProcessor                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |

</div>

## Access to injixo Me

Users with the Agent role can click _Me_{:.menu-item} in the main navigation to see their calendar, request time off and swap shifts. Only **My Calendar** is accessible by default.

Users with Admin access can click _Me_{:.menu-item}, and {% link_new configure injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} to allow users with the Agent role to access additional features.
