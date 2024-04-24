---
title: Create reports
redirect_from:
  - /reports/
  - /available-reports/
redirect_reason: The first redirect is pretty old. The second is for an article deleted in April, 2022.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Generate standard reports in HTML or PDF format with different parameters.
promote-service: enhanced-reporting
toc: false
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/email-reports.md
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/planning-unit-reports.md
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/employee-reports.md
---

In _WFM > Monitoring > Reports_{:.breadcrumbs}, you can create reports based on {% link_new planning unit | features/reporting/standard-reports/planning-unit-reports.md %} and {% link_new employee | features/reporting/standard-reports/employee-reports.md %} data.

Depending on the parameters and filters you use, reports can display various information, e.g. scheduled shifts from different levels or employee configuration data. You can create reports in HTML or PDF format.

> Note
>
> Reports based on selections only display content if you assign at least one {% link_new selection | features/administration/selections.md %} to your people.

## Create reports

1. Select a **Start Date** and an **End Date**.
2. In the **Filter** section, select what is displayed in your report:
   - If **Standard Filter** is activated: The option **[All]** is selected in all boxes by default. To narrow down the list of people, select one or several planning units, contracts, and/or selections.
   - If **Employee Filter** is activated: Select an {% link_new employee filter | features/administration/employee-filter.md %} to create a custom employee list, e.g. based on skills. To overwrite the start and end date selected in the Reports user interface, check the checkbox **Use filter date range as report date range**.
3. In the **Employees** section, click _Apply_{:.doc-button}.
4. (Optional) In the **Employees** section, select individual people to generate reports specifically about them.
5. In the **Parameters** section, configure your report:
   - **Level**
   - **Format**
   - **E-Mail Report to**: From the drop-down menu, select an option to define if and how {% link_new reports are emailed | features/reporting/standard-reports/email-reports.md %} to specific users.
   - **Anonymous Report**: To anonymize employee names and personnel numbers, select **Yes** .
6. Select a report type:
    - To generate a planning unit report, choose from the {% link_new **Planning Unit Reports** | features/reporting/standard-reports/planning-unit-reports.md %} list.
    - To generate an employee report, click on {% link_new **Employee Reports** | features/reporting/standard-reports/employee-reports.md %} and choose from the list.<br>
      Reports with a single-file icon {% icon report-icon-single-file | icon-only %} before the report name cover a maximum period of one month.<br>
      Reports with a icon representing multiple files {% icon report-icon-multiple-files | icon-only %} cover a maximum period of one year.


## Time zones in reports

The times displayed in a report are based on the planning unit's configured time zone. The report header shows the time difference between the planning unit's time zone and UTC, as well as between the planning unit's time zone and local user time.
