# Profiles REST API - beginner course

This repository includes source code for the Profiles REST API project.

## What I learned

Below are listed things I learned while following course:

* Creating Vagrant image and customizing it
    * Binding ports between host and guest machines to successfully synchronise all files from local project
    * Booting up and configuring Vagrant image using ssh
* Creating custom User model for database
    * Custom user model extends AbstractBaseUser and UserPermissionMixin
    * Creating and customizing UserProfileManager which extends BaseUserManager 