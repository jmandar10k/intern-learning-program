# Data dictionary: members.csv

Extract taken on **2025-01-01**. One row per member (but see the brief: the extract is messy).

| Column | Meaning |
|---|---|
| `member_id` | Unique member id |
| `signup_date` | Date the membership started (YYYY-MM-DD) |
| `plan` | `basic`, `plus` or `premium` |
| `monthly_fee` | Current monthly fee |
| `age` | Member age in years |
| `visits_last_30d` | Gym check-ins in the 30 days before extraction |
| `visits_prev_30d` | Gym check-ins in the 30 days before that |
| `classes_booked_90d` | Group classes booked in the last 90 days |
| `pt_sessions_90d` | Personal-training sessions in the last 90 days |
| `days_since_last_complaint` | Days since the member's last complaint; blank if they never complained |
| `payment_method` | `card`, `direct_debit` or `cash` |
| `cancellation_reason` | Reason given in the cancellation form; blank if the member did not cancel |
| `churned_next_month` | 1 if the member cancelled in January 2025 (**target**) |
