# she_codes_deployment

# Project Title: Meet My Idol
by {{ MW }}
She Codes crowdfunding project - DRF Backend.

## About
 "MeetMyIdol" is a crowdfunding website that helps talented people raise funds to meet their idols and learn from them.
 The target audience is people who are passionate about a certain field or industry and want to meet their idols who are experts or celebrities in that field or industry.

## Features
* [x] user accounts
* [x] project creation
* [x] pledge creation        
* [x] token authentication
* [x] permissions
* [x] status codes
* [x] error handling

### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish your MVP }}

* [] Stretch goal one
* [] Stretch goal two
* [] Stretch goal three

## API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |

## Database Schema
{{ Insert your database schema }}

![Wireframe_Home](Images/Wireframe_Home.png)

## Wireframes
{{ Insert your wireframes }}

![Wireframe_Project_List](Images/Wireframe_ProjectList.png)

## Colour Scheme
{{ Insert your colour scheme }}
![Color Scheme](Images/Color_Scheme.png)

![Wireframe_Project](Images/Wireframe_Project.png)

## Fonts
{{ outline your heading & body font(s) - TBC}}

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)