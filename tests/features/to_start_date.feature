Feature: Live Date

  Scenario: I can create a TO Start date for an instrument
    When I POST "tostartdate/test123" with the payload:
      """
      {
        "tostartdate": "2021-06-23"
      }
      """
    Then datastore should contain:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    And the response code should be "201"
    And the response should be:
      """
      {
        "location": "http://localhost/tostartdate/test123"
      }
      """

  Scenario: I receive a 400 error when posting without a tostartdate
    When I POST "tostartdate/test123" with the payload:
      """
      {
        "blah": "23/06/2021"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "tostartdate is required, in format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when posting with a date in the incorrect format
    When I POST "tostartdate/test123" with the payload:
      """
      {
        "tostartdate": "23-06-2021"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Date is not in the required format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when posting without a payload
    When I POST "tostartdate/test123" with the payload:
      """
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Requires JSON format"
      }
      """

  Scenario: I receive a 400 error when posting without a valid payload
    When I POST "tostartdate/test123" without a json payload:
      """
        undefined
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Requires JSON format"
      }
      """

  Scenario: I can create a TO start date for an instrument
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I POST "tostartdate/test123" with the payload:
      """
      {
        "tostartdate": "2021-06-25"
      }
      """
    Then the response code should be "409"
    And the response should be:
      """
      {
        "Already Exists": "test123 already has a TO start date {'tostartdate': '2021-06-23T00:00:00'}. Please use the Patch end point to update the TO start date"
      }
      """

  Scenario: I can get a TO Start date for an instrument
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Get "tostartdate/test123":
    Then the response code should be "200"
    And the response should be:
      """
      {
        "tostartdate": "2021-06-23T00:00:00"
      }
      """

  Scenario: There is no data stored against an instrument called
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Get "tostartdate/test456":
    Then the response code should be "404"
    And the response should be:
      """
      {
        "Not Found": "No data found for test456"
      }
      """

  Scenario: I can delete a TO start date for an instrument
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Delete "tostartdate/test123":
    Then the response code should be "204"
    And datastore should contain:
      | key | tostartdate | questionnaire |

  Scenario: I cannot delete a TO start date for an instrument that does not exist
    Given datastore contains:
      | key | tostartdate | questionnaire |
    When I Delete "tostartdate/test123":
    Then the response code should be "404"
    And the response should be:
      """
      {
        "Not Found": "No data found for test123"
      }
      """

  Scenario: I can Update a TO start date for an instrument
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tostartdate/test123" with the payload:
      """
      {
        "tostartdate": "2021-06-25"
      }
      """
    Then datastore should contain:
      | key | tostartdate | questionnaire |
      | test123 | 25-06-2021 | test123 |
    And the response code should be "200"
    And the response should be:
      """
      {
        "location": "http://localhost/tostartdate/test123"
      }
      """

  Scenario: I cannot Update a TO start date for an instrument which does not exist
    Given datastore contains:
      | key | tostartdate | questionnaire |
    When I PATCH "tostartdate/test123" with the payload:
      """
      {
        "tostartdate": "2021-06-25"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "No data found for test123, please use the create end point"
      }
      """

  Scenario: I receive a 400 error when patching without a TO start date
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tostartdate/test123" with the payload:
      """
      {
        "blah": "2021-06-25"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "tostartdate is required, in format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when patching with a date in the incorrect format
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tostartdate/test123" with the payload:
      """
      {
        "tostartdate": "23-06-2021"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Date is not in the required format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when patching without a payload
    Given datastore contains:
      | key | tostartdate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tostartdate/test123" with the payload:
      """
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Requires JSON format"
      }
      """