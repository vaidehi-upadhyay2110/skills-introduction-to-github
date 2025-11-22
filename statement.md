Project Overview: Movie Recommender and Expense Manager

This document summarizes the core aspects of both the Simple Content-Based Movie Recommendation System and the Real-Time Personal Expense Tracker.
Aspect-
    1.Movie Recommendation System (CLI) :
         Problem Statement - Consumers experience "choice paralysis" and spend excessive time browsing streaming libraries, often defaulting to previously watched 
         content. The gap in this instance is the need for a targeted filter that reduces friction.
         Individuals do not have an immediate, reliable, and secure system that allows them to log, categorize, and monitor their day-to-day spendings,
         and this results in a poor view of their financial status and control.
    2.Scope of the Project :
         The project will be focused solely on implementing the Content-Based Filtering logic, using static in-memory genre data and calculating the similarity scores.
         Excluded from the scope of this project include consuming external APIs, persistent storage, user profiles or other graphical interface.
         The project will focus on the full CRUD cycle (Create, Read, Update, Delete) for their expense data, with real-time updates, using fireStore, 
         as well as user specific data isolation. Excluded from this project will be, reporting, budgeting or advanced visualization methodologies.
    3.Target Users :
         Target users for the movie recommendation system are students and developers who are learning about recommendation algorithms, specifically for simple 
         and easily traceable implementations useful for students, or demonstrative implementations in front of guests, etc.
         Target users for the expense tool will be individuals, freelancers, or small households needing a simple and secure tool that is persistent and updated 
         on their financial transactions, on a small scale (or for themselves) in real-time.
    4.High-Level Features :
         1. Genre Similarity Scoring: Ranks movies based on how closely related the movies are in genre. 
         2. CLI Interface: Simple in and out via command line. 
         3. Basic error handling.
