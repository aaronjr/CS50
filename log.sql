-- Keep a log of any SQL queries you execute as you solve the mystery.
.table
.schema
.schema crime_scene_reports;
SELECT * FROM crime_scene_reports WHERE day = 28 AND mONth = 7 AND year = 2020;
--295 | 2020 | 7 | 28 | Chamberlin Street | Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse. Interviews were cONducted today with three witnesses who were present at the time — each of their interview transcripts mentiONs the courthouse.
SELECT * FROM interviews WHERE transcript like '%courthouse%' AND day = 28 AND mONth = 7 AND year = 2020;
-- id | name | year | mONth | day | transcript
-- 161 | Ruth | 2020 | 7 | 28 | Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse parking lot AND drive away. If you have security footage FROM the courthouse parking lot, you might want to look for cars that left the parking lot in that time frame.
-- 162 | Eugene | 2020 | 7 | 28 | I dON't know the thief's name, but it was someONe I recognized. Earlier this morning, before I arrived at the courthouse, I was walking by the ATM ON Fifer Street AND saw the thief there withdrawing some mONey.
-- 163 | RaymONd | 2020 | 7 | 28 | As the thief was leaving the courthouse, they called someONe who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the persON ON the other end of the phONe to purchase the flight ticket.

--to find license plate
SELECT * FROM courthouse_security_logs WHERE day = 28 AND mONth = 7 AND year = 2020 AND hour = 10 AND minute < 30;
-- 260 | 2020 | 7 | 28 | 10 | 16 | exit | 5P2BI95
-- 261 | 2020 | 7 | 28 | 10 | 18 | exit | 94KL13X
-- 262 | 2020 | 7 | 28 | 10 | 18 | exit | 6P58WS2
-- 263 | 2020 | 7 | 28 | 10 | 19 | exit | 4328GD8
-- 264 | 2020 | 7 | 28 | 10 | 20 | exit | G412CB7
-- 265 | 2020 | 7 | 28 | 10 | 21 | exit | L93JTIZ
-- 266 | 2020 | 7 | 28 | 10 | 23 | exit | 322W7JE
-- 267 | 2020 | 7 | 28 | 10 | 23 | exit | 0NTHK55

-- find atm
SELECT * FROM people JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate WHERE day = 28 AND mONth = 7 AND year = 2020 AND hour = 10 AND minute < 30 order by activity;
--325548 | BrANDON | (771) 555-6667 | 7874488539 | R3G7486 | 258 | 2020 | 7 | 28 | 10 | 8 | entrance | R3G7486
--745650 | Sophia | (027) 555-1068 | 3642612721 | 13FNH73 | 259 | 2020 | 7 | 28 | 10 | 14 | entrance | 13FNH73
--221103 | Patrick | (725) 555-4692 | 2963008352 | 5P2BI95 | 260 | 2020 | 7 | 28 | 10 | 16 | exit | 5P2BI95
--686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X | 261 | 2020 | 7 | 28 | 10 | 18 | exit | 94KL13X
--243696 | Amber | (301) 555-4174 | 7526138472 | 6P58WS2 | 262 | 2020 | 7 | 28 | 10 | 18 | exit | 6P58WS2
--467400 | Danielle | (389) 555-5198 | 8496433585 | 4328GD8 | 263 | 2020 | 7 | 28 | 10 | 19 | exit | 4328GD8
--398010 | Roger | (130) 555-0289 | 1695452385 | G412CB7 | 264 | 2020 | 7 | 28 | 10 | 20 | exit | G412CB7
--396669 | Elizabeth | (829) 555-5269 | 7049073643 | L93JTIZ | 265 | 2020 | 7 | 28 | 10 | 21 | exit | L93JTIZ
--514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE | 266 | 2020 | 7 | 28 | 10 | 23 | exit | 322W7JE
--560886 | Evelyn | (499) 555-9472 | 8294398571 | 0NTHK55 | 267 | 2020 | 7 | 28 | 10 | 23 | exit | 0NTHK55

-- find phONe call, atm AND number plate
SELECT * FROM people JOIN bank_accounts ON people.id = bank_accounts.persON_id JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate JOIN phONe_calls ON people.phONe_number = phONe_calls.caller WHERE courthouse_security_logs.day = 28 AND courthouse_security_logs.mONth = 7 AND courthouse_security_logs.year = 2020 AND courthouse_security_logs.hour = 10 AND courthouse_security_logs.minute < 30 AND phONe_calls.duratiON < 60 order by activity;
--id     | name    | phONe_number   | passport_nu| license_| account_n| pers id| creat| id  | year | mONth | day| hr | min| acti | license | id | caller          |       receiver | year | m | da | duratiON
--686048 | Ernest  | (367) 555-5533 | 5773159633 | 94KL13X | 49610011 | 686048 | 2010 | 261 | 2020 | 7     | 28 | 10 | 18 | exit | 94KL13X | 233 | (367) 555-5533 | (375) 555-8161 | 2020 | 7 | 28 | 45
--514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE | 26013199 | 514354 | 2012 | 266 | 2020 | 7     | 28 | 10 | 23 | exit | 322W7JE | 255 | (770) 555-1861 | (725) 555-3243 | 2020 | 7 | 28 | 49

--find people at ATM
SELECT * FROM atm_transactiONs WHERE day = 28 AND mONth = 7 AND year = 2020 AND atm_locatiON = 'Fifer Street';
--246 | 28500762 | 2020 | 7 | 28 | Fifer Street | withdraw | 48
--264 | 28296815 | 2020 | 7 | 28 | Fifer Street | withdraw | 20
--266 | 76054385 | 2020 | 7 | 28 | Fifer Street | withdraw | 60
--267 | 49610011 | 2020 | 7 | 28 | Fifer Street | withdraw | 50
--269 | 16153065 | 2020 | 7 | 28 | Fifer Street | withdraw | 80
--275 | 86363979 | 2020 | 7 | 28 | Fifer Street | deposit  | 10
--288 | 25506511 | 2020 | 7 | 28 | Fifer Street | withdraw | 20
--313 | 81061156 | 2020 | 7 | 28 | Fifer Street | withdraw | 30
--336 | 26013199 | 2020 | 7 | 28 | Fifer Street | withdraw | 35

-- find people AND accounts at atm -- checked ernest account number above with data here
SELECT * FROM atm_transactiONs JOIN bank_accounts ON atm_transactiONs.account_number = bank_accounts.account_number WHERE day = 28 AND mONth = 7 AND year = 2020 AND atm_locatiON = 'Fifer Street';
id    | account_number | year | mONth | day | atm_locatiON | transactiON_type | amount | account_number | persON_id | creatiON_year
--246 | 28500762 | 2020 | 7 | 28 | Fifer Street | withdraw | 48 | 28500762 | 467400 | 2014
--264 | 28296815 | 2020 | 7 | 28 | Fifer Street | withdraw | 20 | 28296815 | 395717 | 2014
--266 | 76054385 | 2020 | 7 | 28 | Fifer Street | withdraw | 60 | 76054385 | 449774 | 2015
--267 | 49610011 | 2020 | 7 | 28 | Fifer Street | withdraw | 50 | 49610011 | 686048 | 2010
--269 | 16153065 | 2020 | 7 | 28 | Fifer Street | withdraw | 80 | 16153065 | 458378 | 2012
--275 | 86363979 | 2020 | 7 | 28 | Fifer Street | deposit | 10 | 86363979 | 948985 | 2010
--288 | 25506511 | 2020 | 7 | 28 | Fifer Street | withdraw | 20 | 25506511 | 396669 | 2014
--313 | 81061156 | 2020 | 7 | 28 | Fifer Street | withdraw | 30 | 81061156 | 438727 | 2018
--336 | 26013199 | 2020 | 7 | 28 | Fifer Street | withdraw | 35 | 26013199 | 514354 | 2012

SELECT * FROM flights WHERE day = 29 AND mONth = 7 AND year = 2020 order by hour;
-- id | origin_airport_id | destinatiON_airport_id | year | mONth | day | hour | minute
-- 36 | 8                 | 4                      | 2020 | 7 | 29       | 8   | 20

SELECT * FROM flights JOIN airports ON destinatiON_airport_id = airports.id  WHERE day = 29 AND mONth = 7 AND year = 2020 order by hour;
--id | origin_airport_id | destinatiON_airport_id | year | mONth | day | hour | minute | id | abbreviatiON | full_name | city
--36 | 8 | 4 | 2020 | 7 | 29 | 8 | 20 | 4 | LHR | Heathrow Airport | LONdON
--43 | 8 | 1 | 2020 | 7 | 29 | 9 | 30 | 1 | ORD | O'Hare InternatiONal Airport | Chicago
--23 | 8 | 11 | 2020 | 7 | 29 | 12 | 15 | 11 | SFO | San Francisco InternatiONal Airport | San Francisco
--53 | 8 | 9 | 2020 | 7 | 29 | 15 | 20 | 9 | HND | Tokyo InternatiONal Airport | Tokyo
--18 | 8 | 6 | 2020 | 7 | 29 | 16 | 0 | 6 | BOS | Logan InternatiONal Airport | BostON

SELECT * FROM flights JOIN airports ON destinatiON_airport_id = airports.id JOIN passengers ON flights.id = passengers.flight_id  WHERE day = 29 AND mONth = 7 AND year = 2020 AND hour = 8 AND minute = 20 AND city = 'LONdON' AND passport_number = 5773159633 or passport_number = 3592750733;
--18 | 8 | 6 | 2020 | 7 | 29 | 16 | 0 | 6 | BOS | Logan InternatiONal Airport | BostON | 18 | 3592750733 | 4C
--24 | 7 | 8 | 2020 | 7 | 30 | 16 | 27 | 8 | CSF | Fiftyville RegiONal Airport | Fiftyville | 24 | 3592750733 | 2C
--36 | 8 | 4 | 2020 | 7 | 29 | 8 | 20 | 4 | LHR | Heathrow Airport | LONdON | 36 | 5773159633 | 4A -                    THIS IS ERNEST
--54 | 8 | 5 | 2020 | 7 | 30 | 10 | 19 | 5 | DFS | Dallas/Fort Worth InternatiONal Airport | Dallas | 54 | 3592750733 | 6C

SELECT * FROM people WHERE phONe_number = "(375) 555-8161 ";
-- id | name | phONe_number | passport_number | license_plate
-- 864400 | Berthold | (375) 555-8161 |  | 4V16VO0
