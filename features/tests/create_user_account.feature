# language: en

Feature: Create user account


Scenario: Create a user account with success
  Given i access the Coodesh plataform
  When type all mandatory personal data
  Then account was created
