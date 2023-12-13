---
title: Use injixo API
redirect_from: /injixo-api-faq/
product_label:
  - advanced
  - enterprise
promote-service: enhanced-reporting
description: Generate an access token to request data from injixo using the API. Learn what data is available and how to request it.
---

In this article, you will learn:

- where you can find the documentation of the endpoints.
- how to generate a personal access token.
- how the authorization works.
- how you request data.
- which errors can occur.

The injixo API provides access to WFM-related data, such as employees, planning units, schedules, staffing or staff requirements.

If you are not familiar with the REST API concept or BI tools, share this link with the API specialists in your IT department.

> URL change: This API is now accessible via legacy-api.injixo.com
>
> The URL of this API has been changed to **legacy-api.injixo.com**. The old URL remains valid for now, giving you enough time to change your current API queries. The new injixo API documentation is available at [https://api.injixo.com](https://api.injixo.com).

## API reference: Available endpoints

The API reference [legacy-api.injixo.com](https://legacy-api.injixo.com) describes all available endpoints and associated parameters. To learn more about the query parameters and return values, select an endpoint and click the green bar in the middle. To show the full URL, click the **text field showing the endpoint** in the upper right.

{{ 1 | image: "injixo API v1 endpoints" }}

## Authorization: Personal access token

injixo API uses a Bearer Token for Authorization.

> By default, only users with _Admin access_ can create Personal Access Tokens.
>
> To give this permission to other user roles, {% link_new edit the user role | getting-started/configure-user-roles.md %}. In the **Permissions** section, go to _Modules > My Profile > Personal access tokens_{:.breadcrumbs} and check the checkbox.

Create your Personal Access Token in your **user profile**:

1. Click your **name on the start page**, to get into your **user profile**.
2. Select the _Personal Access Tokens_{:.menu-item} menu item
3. Click _Generate new token_{:.doc-button}
4. Enter a description for your Personal Access Token
5. Click _Generate new token_{:.doc-button}
6. Copy your generated token
7. Click _Done_{:.doc-button}

{{ 2 | image: "copy token", '40%' }}

The token is only displayed once during generation, and cannot be accessed again. Store it in a safe place.

All of your tokens are invalidated immediately if your user account is deleted/locked, or if your user's _Admin access_ is removed.

## Requesting data

Use two request headers for each data query:

- `content-Type: application/json`
- `authorization: Bearer {your-personal-access-token}`

The following screenshot shows the two headers in [Advanced Rest Client](https://install.advancedrestclient.com/install) (ARC):

{{ 3 | image: 'ARC example GET Request - Endpoint `/v1/planning_units` Planning unit with ID 1001' }}

### Path and query parameters

The request URL needs further parameters that determine which data is requested and what the result looks like.

- **Path parameters are required**.  
  These often contain IDs or a start date and refer to entities from the WFM area. Use injixo to determine the correct ID. Date parameters always have the format _YYYY-MM-DD_, e.g. `/v1/planning_units/1001/planning_units/2020-01-01`.

- **Query parameters are optional**.  
  They can restrict or extend the result of a query, e.g. the length of a period via _length_ or _end_date_. Use **?** for the first and **&** for all other parameters, e.g. `?end_date=2020-03-31&paid=true`.

  {{ 4 | image: 'Query and Path parameter example', '75%' }}

### Display= parameter

Normally, the query result contains all available fields (which can differ per endpoint). To return only certain fields, use the **display=** parameter, e.g. `activities?display=activity_id,name,paid` will only return three fields.

### Access data in levels

Some endpoints support the parameter `level=` or `levels=` to return data from specific [scheduling levels](/tips-on-shift-center-usage/#tip-9-working-with-different-levels). 

For example, a request to `/v1/planning_units/:planunit_id/schedule/:start_date` returns data for the Schedule level by default. With the additional parameter `levels=final,plan`, it returns data from both the Actual and Schedule level in one request.

The API expects different names than displayed in Shift Center and Schedules:

| injixo API         | injixo                                                          |
| ------------------ | --------------------------------------------------------------- |
| plan               |  Schedule                                                       |
| final              |  Actual                                                         |
| wishes             |  Request                                                        |
| alternative_wishes |  Alternative Request                                            |
| absence_wishes     |  Time-off request (Schedules), _Absence Request_ (Shift Center) |
| acd                |  External System                                                |
| time_recording     |  Time Recording                                                 |
| availabilities     |  Availability                                                   |
| backup             |  Version 1                                                      |
| backup_version_2   |  Version 2                                                      |
| backup_version_3   |  Version 3                                                      |

### Response formats

By default, the injixo API returns the data in JSON, but additionally supports CSV and XML. To use a different response format, add an extension to your URL next to the endpoint, e.g. `/planning_units/1001/contracts/2018-12-31.csv?length=7`.

### Timeouts

The fixed default timeout is 25 seconds. Query execution times can vary depending on the selected parameters and date range. If a query times out, try to limit the requested amount of data per query, e.g. by using shorter date ranges or different query parameters.

## Troubleshooting

A successful query returns the status `200`. The most common causes for a different status are missing data, wrong query parameters, or a wrong authorization header.

| Status | Message                                         | Reason                                                                                                                                                                |
| ------ | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 404    | `"id": "not_found"` or `"message": "not_found"` | The requested ID does not exist, no data available for the requested period, or your user has insufficient rights. Repeat the query for an ID or another time period. |
| 401    | `"message": "Invalid token"`                    | Invalid/wrong Personal Access Token. Check/correct the token used in the Authorization header. Renew it if necessary.                                                 |

## Request example with cUrl

Example query (line starting with _curl_) and corresponding response for JSON and CSV:

```
curl -H "Content-Type: application/json" -H "Authorization: Bearer MmU5OTM4MTAzMWfakeVjYWU4NjViOGRhZWU3ZTU2NTc=" https://legacy-api.injixo.com/v1/employees

{
   "employees":[
      {
         "birth_date":"1900-01-01",
         "birth_place":"",
         "color":13026816,
         "current_identification":"",
         "deleted":false,
         "employee_id":1001,
         "last_name":"Mustermann",
         "first_name":"Max",
         "personnel_number":"1001",
         "schedule_position":0,
         "automated_shift_assignment":true
      }
   ]
}
```

```
curl -H "Content-Type: application/json" -H "Authorization: Bearer MmU5OTM4MTAzMWfakeVjYWU4NjViOGRhZWU3ZTU2NTc=" https://legacy-api.injixo.com/v1/employees.csv

automated_shift_assignment;birth_date;birth_place;color;current_identification;deleted;employee_id; first_name;last_name;personnel_number;schedule_position
true;1900-01-01;"";13026816;"";false;1001;Max;Mustermann;1001;0
```

## Your own report

Understand how your business data is structured in injixo. The injixo API simply follows the structure of the injixo data model. This means configuration items, such as skills, activities, day models, contracts, employees are related to each other. Read our hints about {% link_new configuring injixo | getting-started/set-up-base-configuration.md %} to understand these relationships. Employees are grouped in planning units and selections. Schedules, requirements and many more items are associated with planning units.

Example: If you want to know which/how many agents are available in a certain time frame, query `/schedules` to get all activities and shifts. To replace the displayed IDs with item names, also query `/activities` and `/employees` and combine the results.

Creating a report:

1. Define the scope of your report.
2. Determine the data relevant to you. Typically, you may need to collect data from several endpoints to get all relevant information.
3. Find the right endpoints in the API reference.
4. Query the data.
5. Process the data, e.g. in Excel or with a programming language of your choice. Run calculations on the raw results to convert headcount, hours, or group data for monthly statistics reports.
