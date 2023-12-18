service: bims
runtime: python39

vpc_access_connector:
  name: projects/_PROJECT_ID/locations/europe-west2/connectors/vpcconnect

env_variables:
  PROJECT_ID: _PROJECT_ID

basic_scaling:
  idle_timeout: 60s
  max_instances: 1

handlers:
- url: /.*
  script: auto
  secure: always
  redirect_http_response_code: 301
