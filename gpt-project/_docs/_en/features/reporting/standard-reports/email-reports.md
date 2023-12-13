---
title: Send reports by email
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Deliver injixo reports via email.
---

Reports can easily be sent by email to specific groups or individual Employees. Before the actual report generation you can configure the email delivery options.

For injixo Classic users, the email server is already pre-configured and can send emails by default. injixo Enterprise users can send reports by email if an email server is configured. Read more about how to {% link_new customize email server settings | support/injixo-enterprise-on-premise/update-old-versions.md | #customize-email-server-settings %}.

After sending the email, you will receive a status report with an acknowledgement of receipt instead of the report.

## Send email report to

Configure if and how the report is sent by e-mail, the available options are:

- **No E-Mail**, selected by default.
- **Selected Recipients**, select the desired, available Employees as recipients. Select the email addresses of the employees or manually enter one or more email addresses. Each addressee receives an identical report.
- **Employees in the Employees list**, select employees from the selection list to send the report to their configured email address. This option is only available for daily and weekly schedule reports.
- **Each Employee Separately**, select employees to send a specific report to their configured email address. Each employee receives an individual report separately, which only contains the personal employee data. This option is available for the following reports:

  - Employee Work Schedule I (List)
  - Employee Work Schedule I (List) (without Breaks)
  - Employee Work Schedule II (List)
  - Employee Work Schedule III (Graph)
  - Weekly Schedule II (without Full-Day Activities)
  - Weekly Schedule II (without Breaks) (without Full-Day Activities)

## Email address

Here you can specify the e-mail address to which the report should be sent. Possible options are `injixo Login (E-Mail)`/`E-Mail 1`, `E-Mail 2` or `Both` e-mail addresses entered for an Employee under _WFM > Administration > Scheduling > Employee_{:.breadcrumbs}.

In injixo Enterprise on-premise the `injixo Login (E-Mail)` field is still named `E-Mail 1`.

## Anonymous report

Here you determine whether reports should be output anonymously. If the entry `Yes` is selected, no employee names and personnel numbers appear in the reports. They will be replaced by placeholders. The reports are then sorted by Employee ID.
