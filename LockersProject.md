# LockersProject


In this project I want:

- To have lockers which can be accessed, opened, closed by user
- To have feature for user to check available sizes of lockers
- To have feature for user to sent his luggage sizes and get best option
- To work with multiple sites
- Discounts system?

DB:

- Sites table
    - id
    - city
    - street
    - site_name
- Locker sizes table
    - id
    - width
    - height
    - length
    - hourly_rate
    - size_name
- Lockers table
    - id
    - size_id
    - site_id
    - status_id?
- Locker status table ?
    - id
    - status_name

- Users table
    - id
    - email
    - username
    - mobile_phone
- User billing address
- User billing info
- UserLocker table
    - Start time
    - End time
    - user_id
    - locker_id

Endpoints:

"/" - Homepage (GET)

"/<site_name>" - Site page (GET)

"/<site_name>/available" - Available locker sizes on-site (GET)

"/<site_name>/close?size_id" - Close chosen locker and start rent (POST)

"/<site_name>/open?size_id" - Open chosen locker and finish rent (POST)

"/<site_name>/selection" - Get proposal based on luggage sizes (GET)

"/user" - user page (GET)

"/user/my_lockers" - Rented lockers (GET)

"/user/billing" - Get/add billing info (GET, POST)