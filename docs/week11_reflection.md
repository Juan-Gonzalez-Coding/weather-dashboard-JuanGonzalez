Field 	Your Entry
Name 	Juan Gonzalez   
GitHub Username Juan-Gonzalez-Coding
Preferred Feature       Track Data / Visual / Interactive / Smart
Team Interest 	Yes / No    Yes: Project Owner or Contributor is ok.
✍️ Section 1: Week 11 Reflection

Answer each prompt with 3–5 bullet points:

    Key Takeaways: What did you learn about capstone goals and expectations?
    - Working on a different aspect everyweek. Learning how to organize your work and prepare the foundation before
    you start buidling the app. 

    Concept Connections: Which Week 1–10 skills feel strongest? Which need more practice?
    - I feel the week of algorithms where we learned recursive algorithmns was a bit difficult. The week I feel strongest is tkinter and calling API. 
    Early Challenges: Any blockers (e.g., API keys, folder setup)?
    -So far there has not been any blockers for me. 
    Support Strategies: Which office hours or resources can help you move forward?
    -Office hours will be a good resource for me if I get stuck. If not I can always reachout in slack or to the fellows.

🧠 Section 2: Feature Selection Rationale

List three features + one enhancement you plan to build.
# 	Feature Name 	Difficulty (1–3) 	Why You Chose It / Learning Goal
1 	City Comparison             1       I would like to compare temperatures from cities either in different states or countries.
2 	Weather History Tracker     1		Learn how to track data and display it.    
3 	Simple Statistics           1		Learn simple stats and how to analyze it.
Enhancement 		– 	Weather Poetry 

    🧩 Tip: Pick at least one “level 3” feature to stretch your skills!

🗂️ Section 3: High-Level Architecture Sketch

Source: Gemini AI Assistance with outline 

Add a diagram or a brief outline that shows:

    Core modules and folders

    Feature modules

    Data flow between components
    Here's the revised Section 3, explicitly mentioning the .env file for API keys.

The weather app will follow a modular architecture, separating concerns into core functionalities, feature-specific modules, and a clear data flow.

Architecture Outline:

Core Modules and Folders:

    app.py: Main entry point for the application, orchestrating feature requests and overall flow.

    .env: (New) This file (not version controlled) will securely store sensitive information like API keys.

    config/:

        settings.py: Stores general application configurations such as default locations, units of measurement, and other non-sensitive parameters. It will load API keys from the .env file.

    utils/:

        api_helper.py: Manages all external API interactions (e.g., fetching current weather, historical data). It will retrieve the necessary API keys via settings.py.

        data_parser.py: Transforms raw API responses and CSV data into a consistent, application-wide data format (e.g., dictionaries or custom objects).

        validation.py: Contains functions for input validation (e.g., city names, date ranges, number of cities).

        file_manager.py: Handles reading from and writing to local data files (e.g., weather_history.csv).

    data/:

        weather_history.csv: Stores historical weather data.

Feature Modules:

    city_comparison/:

        logic.py: Handles fetching weather data for multiple cities and preparing it for comparison.

        display.py: Renders the comparison results in a user-friendly format (e.g., side-by-side temperatures).

    weather_history_tracker/:

        logic.py: Manages reading from and writing to data/weather_history.csv, including adding new entries and retrieving past data.

        display.py: Presents historical weather data, potentially with filtering options.

    simple_statistics/:

        logic.py: Implements the statistical calculations (e.g., min/max temperature, average, trends) based on historical or current data. This will involve more complex data manipulation and algorithms.

        display.py: Visualizes or presents the calculated statistics.

    weather_poetry/ (Enhancement):

        logic.py: Contains the logic for generating weather-related poetry based on current weather conditions (e.g., "It's sunny, so a joyful verse..."). This module might integrate with external language model APIs or use rule-based generation.

        display.py: Presents the generated poem to the user.

    user_interface/ (or cli/ if a command-line app):

        main_view.py: Coordinates the overall user experience, presenting menus and displaying outputs from various feature modules.

        input_handler.py: Manages user input (e.g., prompts for city names, date ranges, comparison selections).

Data Flow between Components:

    Application Startup: app.py initializes the application, including loading configurations from config/settings.py. settings.py will, in turn, load sensitive API keys from the .env file.

    User Input: The user_interface/input_handler.py module captures user requests (e.g., "Compare London and Paris," "Show history for Berlin," "Generate stats for New York," "Tell me a weather poem").

    Request Routing: app.py receives the user request and routes it to the appropriate feature module's logic.py (e.g., city_comparison/logic.py, weather_history_tracker/logic.py, simple_statistics/logic.py, weather_poetry/logic.py).

    API Call / Data Retrieval:

        For current data (e.g., for City Comparison, Weather Poetry, and possibly for adding new history entries): The respective logic.py module uses utils/api_helper.py to make calls to external weather APIs. api_helper.py will access the necessary API keys securely loaded via settings.py.

        For historical data (e.g., for Weather History Tracker, Simple Statistics): The logic.py module uses utils/file_manager.py to read data from data/weather_history.csv.

    Data Parsing and Validation:

        Raw API responses are passed to utils/data_parser.py for transformation into a standardized application-wide data model.

        CSV data read from weather_history.csv is also parsed by utils/data_parser.py into usable structures.

        User inputs are validated by utils/validation.py to ensure correctness before processing.

    Data Processing / Feature Logic: The logic.py modules within each feature process the parsed data according to their specific functions (e.g., comparing temperatures for city_comparison, performing aggregations for simple_statistics, generating text for weather_poetry).

    Data Storage (Historical): When new current weather data is retrieved and relevant, the weather_history_tracker/logic.py module (via utils/file_manager.py) appends this data to data/weather_history.csv.

    Data Display: The processed results from the logic.py modules are then passed to their corresponding display.py modules (e.g., city_comparison/display.py, simple_statistics/display.py) to be formatted and rendered by the user_interface/main_view.py for presentation to the user.

📊 Section 4: Data Model Plan

Source: Gemini AI assistance in planning file type
Fill in your planned data files or tables:
File/Table Name 	Format (txt, json, csv, other) 	Example Row
weather_history.json    json   {"date": "2025-06-09", "city": "Los Angeles", "temperature_fahrenheit": 78, "condition": "Sunny",}
user_settings.json      json    {"default_city": "New York", "temperature_unit": "fahrenheit", "forecast_days": 5} 

		
📆 Section 5: Personal Project Timeline (Weeks 12–17)

Customize based on your availability:
Week 	Monday 	Tuesday 	Wednesday 	Thursday 	    Key Milestone
12 	API setup 	Error handling Buffer day Tkinter shell Basic working app
13 	Feature 1 start			                    Integrate 	Feature 1 complete
14 	Feature 2 start                      Review & test 	Finish Feature 2 complete
15 	Feature 3 	Polish UI 	Error passing 	Refactor 	All features complete
16 	Enhancement 	Docs 	Tests 	Packaging 	Ready-to-ship app
17 	Rehearse 	Buffer 	Showcase 	– 	Demo Day
⚠️ Section 6: Risk Assessment

Identify at least 3 potential risks and how you’ll handle them.
Risk 	Likelihood (High/Med/Low) 	Impact (High/Med/Low) 	Mitigation Plan
API Rate Limit 	Medium 	Medium 	Add delays or cache recent results
Weather API Downtime Low High   Only show saved weather from last 7 days or use offline data
Data Storage Maintenance Low    Med     Clean the saved historical data after a certain period of time like 3 months
Lack of Haiku Poems     Low     Low      Generate 30 Haiku Poems for each type of weather

			
			
🤝 Section 7: Support Requests

What specific help will you ask for in office hours or on Slack/Discord?
Bug fixes or any possible feedback of feature implmentations.

✅ Section 8: Before Monday (Start of Week 12)

Complete these setup steps before Monday:

    Push main.py, config.py, and a /data/ folder to your repo

    Add OpenWeatherMap key to .env (⚠️ Do not commit the key)

    Copy chosen feature templates into /features/

    Commit and push a first-draft README.md

    Book office hours if you're still stuck on API setup

📤 Final Submission Checklist (Due Friday 23:59):

✅ Week11_Reflection.md completed
✅ File uploaded to GitHub repo /docs/
✅ Repo link submitted on Canvas