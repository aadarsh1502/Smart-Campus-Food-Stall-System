Smart Campus Food Stall System

A Django-based web application that allows students to pre-order food during campus break hours and helps shopkeepers manage orders efficiently.

This system reduces long queues, improves order management, and streamlines food distribution during peak break times.

Project Overview

During short class breaks, campus food stalls often experience heavy rush. Students waste valuable time waiting in lines, and shopkeepers struggle to handle sudden order spikes.

The Smart Campus Food Stall System solves this problem by allowing:

Students to pre-order food in advance

Students to select a preferred break time (time slot)

Shopkeepers to view and manage all orders efficiently

Features
Student Features

User registration and login

View available food items

Select quantity

Choose preferred time slot (break timing)

Place food orders

View order history

Automatic total price calculation

Shopkeeper Features (Admin/Staff Access)

View all placed orders

Orders sorted by latest

Manage food item availability

Manage time slots from Django Admin

Access to shopkeeper dashboard is restricted using Django’s staff_member_required decorator.

Tech Stack

Python

Django

SQLite

HTML

Bootstrap

Django Authentication System

Django Admin Panel

Database Models
TimeSlot

Stores break timings:

Start time

End time

FoodItem

Stores food menu data:

Name

Price

Availability status

Order

Stores order details:

Student (linked to Django User)

Food item

Time slot

Quantity

Timestamp

Includes a method to calculate total price:
Food price × Quantity

System Workflow
Student Flow

Register or login

Browse available food items

Select food item and quantity

Choose preferred break time slot

Place order

View order history

Shopkeeper Flow

Login as staff/admin user

Access all orders

Prepare orders according to time slots

Manage food items via admin panel

Installation Guide

Clone the repository:

git clone <your-repo-link>
cd smart-campus-food-stall-system

Create virtual environment:

python -m venv env

Activate environment:

Windows:

env\Scripts\activate

Mac/Linux:

source env/bin/activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Create superuser:

python manage.py createsuperuser

Run server:

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
Future Improvements

Order status tracking (Pending, Preparing, Ready, Completed)

Online payment integration

Time-slot order limits

Email or SMS notifications

Admin analytics dashboard (sales, peak times, revenue)

Mobile-friendly UI optimization

Learning Outcomes

This project helped me understand:

Role-based access control in Django

Relational database modeling

Authentication and user management

Clean backend logic structuring

Practical problem-solving using web applications

Project Status

Basic functional version completed.
Future upgrades planned.
