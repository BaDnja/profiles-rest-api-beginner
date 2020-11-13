# Profiles REST API - beginner course

This repository includes source code for the Profiles REST API project.
This repository is based on beginner REST API course on Udemy.
Link to course: [Build a Backend REST API with Python & Django - Beginner](https://www.udemy.com/course/django-python/)

## What I learned

Below are listed things I learned while following course:

* Creating **Vagrant image** and customizing it
    * Binding ports between host and guest machines to successfully synchronise all files from local project
    * Booting up and configuring Vagrant image using ssh
* Creating **custom User model** for database
    * Custom user model extends AbstractBaseUser and UserPermissionMixin
    * Creating and customizing UserProfileManager which extends BaseUserManager 
* Working with *API View* and *API ViewSet* for accomplishing different types of functionality
    * Adding different *methods* to API View and API ViewSet
    * Working with **serializers** and overriding default user model methods
    * Working with **ModelViewSet** for direct communication with database users
        * Creating **authentication** class for token authentication
        * Managing **permissions** using rest framework permissions and extending user BasePermission
        * Adding **filters** for searching profiles using built in rest framework filters.
* Creating authorization restrictions on API so that *only authenticated users can access* API data.