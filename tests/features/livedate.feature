Feature: Live Date

  Scenario: I can create a live date for an instrument
    When I POST "livedate/test123/create" with the payload:
      """
      {
        "livedate": "23/06/2021"
      }
      """
    Then datastore should contain:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    And the response code should be "201"
    And the response should be:
      """
      {
        "test123": "2021-06-23T00:00:00"
      }
      """

  Scenario: I receive a 400 error when posting without a livedate
    When I POST "livedate/test123/create" with the payload:
      """
      {
        "blah": "23/06/2021"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "error": "livedate is required, in format dd/mm/yyyy"
      }
      """

  Scenario: I receive a 400 error when posting without a payload
    When I POST "livedate/test123/create" with the payload:
      """
      {
        "livedate": "23-06-2021"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "error": "Date is not in the required format dd/mm/yyyy"
      }
      """

  Scenario: I receive a 400 error when posting with a date in the incorrect format
    When I POST "livedate/test123/create" with the payload:
      """
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "error": "Requires JSON format"
      }
      """

  Scenario: I can get a live date for an instrument
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Get "livedate/test123":
    Then the response code should be "200"
    And the response should be:
      """
      {
        "livedate": "2021-06-23T00:00:00"
      }
      """

  Scenario: I can delete a live date for an instrument
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Delete "livedate/test123/delete":
    Then the response code should be "204"
    And datastore should contain:
      | key | livedate | questionnaire |