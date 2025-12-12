# rr-qa-automation-assignment
Automation Assignment for RR

---Testing Strategy
The testing strategy focuses on validating both API correctness and UI functionality for the movie listing application.
1. Ensure that API responses (e.g., popular, trending/movie/week) are accurate and consistent
2. Verify UI displays the correct data reflected from the API
3. Prioritize high-value test scenarios covering functional, data validation, and regression areas

---Test Cases Generated
Validate “Popular Movies” category
Validate results match trending/movie/week
Search Functionality
Movie Details Validation
Error Handling Scenarios

---Why the above cases selected?
They represent core workflows used by most users
They ensure data accuracy between API & UI
They focus on regression risks
They cover positive, negative, and validation scenarios

---The automation framework consists of:
1. Language: Python
2. Test Runner: pytest
3. HTTP / API Library: requests
4. Reporting: pytest-html or console output
5. Logging: Python standard logging
6. Utilities:
  Config management: Consists of reusable data/ variables
  api_client: Consists of customized Rest API libraries
  logger: Consists of logging handles

---How to Run Tests
1. Prerequisites: Python 3.9+ and pip installed
2. Install dependencies: <pip install -r requirements.txt>
3. Run all tests: <pytest>
4. Run tests with HTML report: <pytest --html=report.html>
5. Run a specific test: <pytest tests/test_trending_movies.py::test_status_code_200>

---Test Design Techniques Used
1. Equivalence Partitioning – choosing valid/invalid categories
2. Boundary Testing – validating page/rating/etc counts, first/last items
3. Positive & Negative Testing – successful data fetch vs. API error
4. API Schema Validation – validating required fields (id, title, poster, popularity)
5. Data Consistency Testing – comparing UI results with API response
6. Use Case Testing – validating end-to-end workflows such as viewing trending movies

---Pattern Used
1. Page Object Model/ API Object Pattern: separated API clients instead of mixing logic into tests
2. Modular Test Structure
3. Reusable Helper Functions
4. Avoid duplicated code across tests

---Bugs found
1. Page Refresh gives error
2. Popular movie - Max page count is invalid/ throws error
3. Top Rated movie - Max page count is invalid/ throws error
4. Newest Movie - Max Page count shows higher upon adding rating filter (errored upon clicking)
5. Data integrity: Popular vs Trending data sets for overlap
6. Data integrity: Top Rated vs Discover/Search(with genre) Top Rated results are mismatching
7. Validate sort consistency across multiple calls

---CI/CD Approach
1. Configure a Jenkins agent/VM with Python and all required prerequisites preinstalled
2. Store sensitive values like API_KEY and BASE_URL as Jenkins environment variables or credentials so the same job can run across multiple environments
3. Create a Jenkins Pipeline job that checks out the repo, installs dependencies, and executes the pytest suite with HTML reporting
4. Optionally schedule the pipeline (nightly/weekly) or trigger it manually as needed
5. Keep a dedicated VM/agent available to ensure consistent and reliable execution of the test suite
