# LockersProject


In this project I want:

- To have lockers which can be accessed, opened, closed by user
- To have feature for user to check available sizes of lockers
- To have feature for user to sent his luggage sizes and get best option
- To work with multiple sites
- Discounts system?

DB:
- Addresses table
    - id
    - country
    - city
    - street
    - house_number
    - zip_code

- Locations table
    - id
    - location name
    - location slug
    - address_id
    - phone_number
    - email
    - description
    - is_active
    - API_URL
  
- Locker sizes table
    - id
    - width
    - height
    - depth
    - hourly_rate
    - size_name
  
- Lockers table
    - id
    - size_id
    - location_id
    - locker_number
    - is_available
    - is_locked

- Rental table
    - Start time
    - End time
    - user_id
    - locker_id
    - is_rented
    - duration
    - total_sum


- Users table
    - id
    - email
    - username
    - mobile_phone

- User billing address
    - id
    - user_id
    - country
    - city
    - street
    - house_number
    - zip_code

- User billing info
    - id
    - user_id
    - billing_address_id
    - card_number
    - expiration_year
    - expiration_month
    - cvv


Endpoints:

"/" - Homepage (GET)

"/locations" - Locations list (GET)

"/locations/<location_slug>" - Location page with Available locker sizes on-site (GET)

"/locations/<location_slug>/selection/<locker_size_id>" - Select locker size (GET, POST)


"/<rental_id>" - Rental page (GET)

"/<rental_id>/close?size_id" - Close chosen locker (POST)

"/<rental_id>/open?size_id" - Open chosen locker (POST)

"/<rental_id>/end" - End rent (GET)


"/user" - user page (GET)

"/user/login" - Login page (GET, POST)

"/user/logout" - Logout (GET)

"/user/register" - Register page (GET, POST)

"/user/rented_lockers" - Rented lockers by user (GET)

"/user/billing_address" - Get/add billing address (GET, POST)

"/user/billing_address/delete/<billing_address_id>" - Delete billing address (POST)

"/user/billing" - Get/add billing info (GET, POST)

"/user/billing/delete/<billing_id>" - Delete billing info (POST)