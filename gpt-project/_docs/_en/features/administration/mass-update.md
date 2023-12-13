---
title: Mass update
product_label:
  - advanced
  - enterprise
  - classic
---

Use mass update to edit configuration data assignments for multiple people at the same time.
You can use the mass update functionality for the following configuration elements:

- Contracts
- Skills
- Planning units
- Selections
- Shift sequences
- Work time pattern models

## Prerequisites

Before you can use the mass update functionality, you need to {% link_new set up your base configuration | getting-started/set-up-base-configuration.md %}.

## Start mass update

> Note
>
> You cannot revert or undo a mass update. Start another mass update to overwrite the wrongly mass-updated data, or change the data for each person individually.  

To start a mass update, follow these steps: 

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. To select the employees whose configuration data you want to edit, choose a selection or click the employee filter icon {% icon employee-filter | icon-only %}.
3. In the action bar, click the mass update icon {% icon mass-update | icon-only %}.<br>The mass update page opens. 
4. In the **Parameters** section, use the **Master data** drop-down menu to select the configuration element you want to edit for multiple employees at once.<br>(Optional): Use the **From** and **To** fields to limit how long the mass update will be effective.
5. Select an **Action**.
6. Depending on your selection, the following sections appear on the right: **Existing Assignments**, **New Assignment**, or **New Validity Period**. In the sections, select the elements you want to add, delete, or replace.
7. To start the mass update, click **OK**.<br>The job processing screen opens.<br>A results page of your mass update results opens.

| Question                                                                          | Answer                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Why do my people have contracts assigned to them for a shorter period than before, following a mass update?                              | If you assign a configuration item to a person that exceeds the processing period, there may be periods without assignment.<br>Example: An employee has a contract assignment from 1 March to 31 May You enter a new validity period from 1 March to 15 April. After the mass update, there will be no assignment between 16 April and 31 May.                                                                                                                                           |


