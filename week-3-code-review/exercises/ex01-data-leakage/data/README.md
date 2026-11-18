# Data dictionary: customers.csv

One row per subscription customer, extracted at the end of the month. `churned` is whether the
customer cancelled during the **following** month.

| Column | Meaning |
|---|---|
| `customer_id` | Unique id |
| `region` | Sales region |
| `contract` | `monthly`, `annual` or `two_year` |
| `tenure_months` | Months since sign-up |
| `monthly_charges` | Current monthly bill |
| `support_tickets_90d` | Support tickets opened in the last 90 days |
| `logins_30d` | App logins in the last 30 days |
| `payment_failures_90d` | Failed payments in the last 90 days |
| `retention_offer_sent` | 1 if the retention team sent a discount offer. Offers are sent when a customer opens a cancellation request in the app |
| `churned` | 1 if the customer cancelled in the following month (**target**) |
