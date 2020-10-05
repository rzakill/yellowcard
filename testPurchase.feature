Feature: Login to the Yellow Card app
	Registered user decides to access their account on the yellow card app,
	he is required to input correct login credentials in the login form

Scenario: User Signin
     Given user is able to access the yellow card app
     When user logs in with correct credentials
     Then user is able to buy bitcoin from wallet
