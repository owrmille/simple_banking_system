# simple_banking_system
SQL + Python for imitating banking system


STAGE 1/4

You should allow customers to create a new account in our banking system.
Once the program starts, you should print the menu:

1. Create an account
2. Log into account
0. Exit

If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. A PIN code is a sequence of any 4 digits. PIN should be generated in a range from 0000 to 9999.
If the customer chooses ‘Log into account’, you should ask them to enter their card information. Your program should store all generated data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin. You can use an array to store the information.
After all information is entered correctly, you should allow the user to check the account balance; right after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

STAGE 2/4

Luhn Algorithm in action.
The Luhn algorithm is used to validate a credit card number or other identifying numbers, such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10, checks the sum of the digits in the card number and checks whether the sum matches the expected result or if there is an error in the number sequence. 
After working through the algorithm, if the total modulus 10 equals zero, then the number is valid according to the Luhn method.
While the algorithm can be used to verify other identification numbers, it is usually associated with credit card verification. The algorithm works for all major credit cards.

You should allow customers to create a new account in our banking system.

Once the program starts you should print the menu:

1. Create an account
2. Log into the account
0. Exit

If the customer chooses ‘Create an account’, you should generate a new card number that satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.
If the customer chooses ‘Log into account’, you should ask to enter card information.
After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

STAGE 3/4

It's very upsetting when the data about registered users disappears after the program is completed. To avoid this problem, you need to create a database where you will store all the necessary information about the created credit cards. We will use SQLite to create the database.
SQLite is a database engine. It is a software that allows users to interact with a relational database. In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. This allows for greater accessibility: copying a database is no more complicated than copying the file that stores the data, and sharing a database implies just sending an email attachment.
You can use the sqlite3 module to manage SQLite database from Python. You don't need to install this module. It is included in the standard library.

In this stage, create a database named card.s3db with a table titled card. It should have the following columns:

id INTEGER
number TEXT
pin TEXT
balance INTEGER DEFAULT 0

Pay attention: your database file should be created when the program starts if it hasn’t yet been created. And all created cards should be stored in the database from now.
Do not forget to commit your DB changes right after executing a query!

STAGE 4/4

You have created the foundation of our banking system. Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.

Now your menu should look like this:

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

If the user asks for Balance, you should read the balance of the account from the database and output it into the console.

Add income item should allow us to deposit money to the account.

Do transfer item should allow transferring money to another account. You should handle the following errors:

If the user tries to transfer more money than he/she has, output: Not enough money!
If the user tries to transfer money to the same account, output the following message: You can't transfer money to the same account!
If the receiver's card number doesn’t pass the Luhn algorithm, you should output: Probably you made a mistake in the card number. Please try again!
If the receiver's card number doesn’t exist, you should output: Such a card does not exist.
If there is no error, ask the user how much money they want to transfer and make the transaction.
If the user chooses the Close account item, you should delete that account from the database.

Do not forget to commit your DB changes right after executing a query!
