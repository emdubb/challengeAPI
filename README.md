# FitChallenge API

[Overview](#overview) | [Endpoint Reference](#endpoint) | [Data Model](#data)

<a name="overview"></a>

### Overview

##### Technologies Used

- [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [PIP](https://pip.pypa.io/en/stable/)

##### Dependencies

- [Python](https://www.python.org/)
- MySQL
- Pthon Packages
  - [Django](https://www.djangoproject.com/)
  - [Django REST Framework](http://www.django-rest-framework.org/)
  - [Pillow](http://pillow.readthedocs.io/en/3.4.x/index.html)

<a name="endpoint"></a>

### Endpoint Reference

<a name="data"></a>

### Data Model

- [User Model](#userModel)
- [Competition Model](#competitionModel)
- [Challenge Model](#challengeModel)

<a name="userModel"></a>

##### User Model

| Key          | Value Type | Value Description |
| ------------ | ---------- | ----------------- |
| fname        | CharField  | *Required.*       |
| lname        | CharField  | *Required.*       |
| email        | EmailField | *Required.*       |
| password     | CharField  | *Required.*       |
| profile_url  | ImageField | *Optional.*       |
| username     | CharField  | *Required.*       |
| device_model | CharField  | *Optional.*       |
| device_type  | CharField  | *Optional.*       |
| timezone     | CharField  | *Optional.*       |

<a name="competitionModel"></a>

##### Competition Model

| Key       | Value Type | Value Description |
| --------- | ---------- | ----------------- |
| members   |            | *Required.*       |
| challenge |            | *Required.*       |

<a name="challengeModel"></a>

##### Challenge Model

| Key   | Value Type   | Value Descripion |
| ----- | ------------ | ---------------- |
| days  | IntegerField | *Required.*      |
| teams | IntegerField | *Required.*      |

