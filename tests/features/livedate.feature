Feature: Live Date

  Scenario: I can create a live date for an instrument
    When I POST "livedate/test123/create" with the payload:
      """
      {
        "livedate": "2021-06-23"
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
        "Bad Request": "livedate is required, in format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when posting with a date in the incorrect format
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
        "Bad Request": "Date is not in the required format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when posting without a payload
    When I POST "livedate/test123/create" with the payload:
      """
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Requires JSON format"
      }
      """

  Scenario: I can create a live date for an instrument
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I POST "livedate/test123/create" with the payload:
      """
      {
        "livedate": "2021-06-25"
      }
      """
    Then the response code should be "409"
    And the response should be:
      """
      {
        "Already Exists": "test123 already has a live date {'livedate': '2021-06-23T00:00:00'}. Please use the Patch end point to update the livedate"
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

  Scenario: There is no data stored against an instrument called
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Get "livedate/test456":
    Then the response code should be "404"
    And the response should be:
      """
      {
        "Not Found": "No data found for test456"
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


  Scenario: I cannot delete a live date for an instrument that does not exist
    Given datastore contains:
      | key | livedate | questionnaire |
    When I Delete "livedate/test123/delete":
    Then the response code should be "404"
    And the response should be:
      """
      {
        "Not Found": "No data found for test123"
      }
      """


  Scenario: I can Update a live date for an instrument
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "livedate/test123/update" with the payload:
      """
      {
        "livedate": "2021-06-25"
      }
      """
    Then datastore should contain:
      | key | livedate | questionnaire |
      | test123 | 25-06-2021 | test123 |
    And the response code should be "200"
    And the response should be:
      """
      {
        "test123": "2021-06-25T00:00:00"
      }
      """

  Scenario: I cannot Update a live date for an instrument which does not exist
    Given datastore contains:
      | key | livedate | questionnaire |
    When I PATCH "livedate/test123/update" with the payload:
      """
      {
        "livedate": "2021-06-25"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "No data found for test123, please use the create end point"
      }
      """

  Scenario: I receive a 400 error when patching without a livedate
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "livedate/test123/update" with the payload:
      """
      {
        "blah": "2021-06-25"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "livedate is required, in format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when patching with a date in the incorrect format
    Given datastore contains:
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "livedate/test123/update" with the payload:
      """
      {
        "livedate": "23-06-2021"
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
      | key | livedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "livedate/test123/update" with the payload:
      """
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Requires JSON format"
      }
      """