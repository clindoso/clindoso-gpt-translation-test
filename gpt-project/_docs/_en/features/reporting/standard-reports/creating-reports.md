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

In this article, you will learn:

- how to create reports based on different parameters and filters.
- how reports display time zones.

Reports contain different data, e.g. scheduled shifts from different levels or configuration data. Learn more about {% link_new planning unit reports | features/reporting/standard-reports/planning-unit-reports.md %} and {% link_new employee reports | features/reporting/standard-reports/employee-reports.md %}. You can create reports in HTML or PDF format.

> Some reports are based on selections. These reports only display content if you add at least one {% link_new selection | features/administration/selections.md %} to your employees.

## Create reports

1. Go to _WFM > Monitoring > Reports_{:.breadcrumbs}.
2. Select a **Start Date** and **End Date**.

3. Use the **Filter** section to select what is displayed in your report:

   - **Standard Filter**: Select a **Planning Unit**, **Contract**, or **Selection** to narrow down the employee list. To select multiple entries, press **CTRL** or **Shift** while clicking.

     {{ 2 | image: 'Standard Filter', '90%' }}

   - **Employee Filter**: Select an {% link_new employee filter | features/administration/employee-filter.md %} to create a custom employee list, e.g. based on skills. To create a new filter, click **Filter Editor**.

     <br>Check the checkbox **Use filter date range as report date range** to overwrite the start and end date selected in the report user interface.

     {{ 3 | image: 'Employee Filter', '60%' }}

     Employee filters are not available in injixo Essential WFM.

4. Click _Apply_{:.doc-button}.

5. (Optional) In the **Employees** section, select single **Employees**.

   {{ 5 | image: 'Employees section', '60%' }}

6. In the **Parameters** section, you can:

   - select the **Level** from which you want to extract data.
   - set the data output **Format** (PDF or HTML).
   - choose to {% link_new send reports by email | features/reporting/standard-reports/email-reports.md %} to specific users.
   - anonymize employee names and personal numbers.

   {{ 4 | image: 'Report parameters', '30%' }}

7. In the sections **Planning Unit Report** or **Employee Report** on the right, select a report name.

   {{ 6 | image: 'List of reports with sections', '50%' }}

   <br>
   The document icons next to the report names show for which period you can create a report:
   - _![icon showing a single file](/assets/img/common/report-icon-single-file.png)_{:.doc-button-icon}: maximum period of one month
   - _![icon showing multiple files](/assets/img/common/report-icon-multiple-files.png)_{:.doc-button-icon}: maximum period of one year

A JobProcessor window opens. The requested report will be created and displayed.

You can create more reports with the same parameters. If you change a filter or date, click _Apply_{:.doc-button}.

## Time zones in reports

The times in a report refer to the local time of the planning unit. The report header shows the time difference between the planning unit's time zone and UTC, as well as between the planning unit's time zone and local user time.

Example: An employee in New York starts their shift at 8:30 a.m. A report uses the local time of Manchester (UK), the planning unit location. The time difference is +05:00. The employee must deduct this time difference from the displayed time to know when the shift starts. The shift would start at 3:30 a.m. at New York local time.
