# language: en

Feature: Login with a existent account and search for open jobs


Scenario: Search for open jobs through name company
  Given i access the Coodesh plataform with a valid user account
  When inform the company name
  Then open jobs company are show in screen search
