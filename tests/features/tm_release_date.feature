Feature: Live Date

  Scenario: I can create a new TM Release date for an instrument
    When I POST "tmreleasedate/test123" with the payload:
      """
      {
        "tmreleasedate": "2021-06-23"
      }
      """
    Then datastore records for Totalmobile should contain:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    And the response code should be "201"
    And the response should be:
      """
      {
        "location": "http://localhost/tmreleasedate/test123"
      }
      """

  Scenario: I receive a 400 error when posting without a tmreleasedate
    When I POST "tmreleasedate/test123" with the payload:
      """
      {
        "blah": "23/06/2021"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "tmreleasedate is required, in format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when posting with a date in the incorrect format
    When I POST "tmreleasedate/test123" with the payload:
      """
      {
        "tmreleasedate": "23-06-2021"
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
    When I POST "tmreleasedate/test123" with the payload:
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
    When I POST "tmreleasedate/test123" without a json payload:
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

  Scenario: I can change a TM Release date for an instrument
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I POST "tmreleasedate/test123" with the payload:
      """
      {
        "tmreleasedate": "2021-06-25"
      }
      """
    Then the response code should be "409"
    And the response should be:
      """
      {
        "Already Exists": "test123 already has a TM Release date {'tmreleasedate': '2021-06-23T00:00:00'}. Please use the Patch end point to update the TM Release date"
      }
      """

  Scenario: I can get a TM Release date for an instrument
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Get "tmreleasedate/test123":
    Then the response code should be "200"
    And the response should be:
      """
      {
        "tmreleasedate": "2021-06-23T00:00:00"
      }
      """

  Scenario: There is no data stored against an instrument called
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Get "tmreleasedate/test456":
    Then the response code should be "404"
    And the response should be:
      """
      {
        "Not Found": "No data found for test456"
      }
      """

  Scenario: I can delete a TM Release date for an instrument
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I Delete "tmreleasedate/test123":
    Then the response code should be "204"
    And datastore records for Totalmobile should contain:
      | key | tmreleasedate | questionnaire |

  Scenario: I cannot delete a TM Release date for an instrument that does not exist
    Given datastore contains Totalmobile information:
      | key | tomreleasedate | questionnaire |
    When I Delete "tmreleasedate/test123":
    Then the response code should be "404"
    And the response should be:
      """
      {
        "Not Found": "No data found for test123"
      }
      """

  Scenario: I can Update a TM Release date for an instrument
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tmreleasedate/test123" with the payload:
      """
      {
        "tmreleasedate": "2021-06-25"
      }
      """
    Then datastore records for Totalmobile should contain:
      | key | tmreleasedate | questionnaire |
      | test123 | 25-06-2021 | test123 |
    And the response code should be "200"
    And the response should be:
      """
      {
        "location": "http://localhost/tmreleasedate/test123"
      }
      """

  Scenario: I cannot Update a TM Release date for an instrument which does not exist
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
    When I PATCH "tmreleasedate/test123" with the payload:
      """
      {
        "tmreleasedate": "2021-06-25"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "No data found for test123, please use the create end point"
      }
      """

  Scenario: I receive a 400 error when patching without a TM Release date
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tmreleasedate/test123" with the payload:
      """
      {
        "blah": "2021-06-25"
      }
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "tmreleasedate is required, in format yyyy-mm-dd"
      }
      """

  Scenario: I receive a 400 error when patching with a date in the incorrect format
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tmreleasedate/test123" with the payload:
      """
      {
        "tmreleasedate": "23-06-2021"
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
    Given datastore contains Totalmobile information:
      | key | tmreleasedate | questionnaire |
      | test123 | 23-06-2021 | test123 |
    When I PATCH "tmreleasedate/test123" with the payload:
      """
      """
    Then the response code should be "400"
    And the response should be:
      """
      {
        "Bad Request": "Requires JSON format"
      }
      """