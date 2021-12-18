# part1 description:
In part1, I want to make a visual bank system to replicate real system like ATM machine.
I create three pages to illustrate how it works. I want let users create their account(saving or credit) first in first page, then login in their account to transfer, withdraw,deposit money and check the transaction deatails. Also, to protect every account,there are security functions like lock, unlock, change password and logout.
Create account. Users need to anwser key questions about your details to make sure their truth. In the end, users get their card number which random create with seven digits and four digits PIN number must be saved.
On saving account, there is a function called transfer. The first step you should check target account exist and then transfer money to it. I add new varible in class to make sure class can access the data frome txt file. And, transaction fee adds in class when users transfer money.
On credit account, there is interest fee when you overdue.
For security, I add serveal functions lock, unlock and change password. You need remember the key information when you create account. You must use these information to unlock account and change password.
