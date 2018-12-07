Feature: Przykładowy scenariusz BDD
  Oto przykładowy scenariusz BDD, w celu ukazania zależności pomiędzy plikiem feature a testowym

  Scenario: Przykładowy scenariusz
    Given Mając <start> ogórków
    When Zjadłem <eat> ogórków
    Then Powinno mi zostać <left> ogórków

Examples:
| start | eat | left |
|  12   |  5  |  7   |
|  40   |  10 |  30  |