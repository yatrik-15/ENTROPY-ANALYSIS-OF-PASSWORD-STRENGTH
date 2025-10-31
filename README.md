🔑 Password Entropy Analyzer

A web-based dashboard that performs a mathematical analysis of password strength using Shannon Entropy. This project was built for the "Innovative Assignment" in the Mathematical Foundation for Computer Science (MFCS) course.

Screenshot

<img width="1919" height="1079" alt="Screenshot 2025-10-31 205105" src="https://github.com/user-attachments/assets/87b1cac8-b831-47b0-8dce-f7571adaacc4" />


1. About This Project

In cybersecurity, "password strength" is often enforced with simple, arbitrary rules like "must have 8 characters and one symbol." These rules don't capture the true, mathematical essence of security: predictability.

This project moves beyond those simple rules to provide a quantitative, data-driven analysis of password lists. It's a web-based dashboard that allows a user to:

Paste in a list of passwords.

Upload a large password file (like rockyou.txt).

The application then performs a complete mathematical analysis and presents the results in a clean dashboard, showing the true randomness (or lack thereof) of the dataset.

2. Features

Dual Input Modes: Analyze data by pasting text directly or by uploading large local files.

Shannon Entropy Calculation: The core of the project. It calculates the true information entropy of the character set in "bits per character."

Strength Rating: Provides a user-friendly rating (from "Very Weak" to "Very Strong") based on the entropy score.

Character Set Analysis: A detailed breakdown of the unique characters found, categorized into:

a-z (Lowercase)

A-Z (Uppercase)

0-9 (Numbers)

!@# (Symbols & Extended ASCII)

Frequency Visualization: Generates a dynamic bar chart (using Chart.js) to visualize the Top 30 most frequent characters, providing clear visual proof of predictability.

Modern UI: A clean, responsive, single-page application built with Tailwind CSS.

3. The Mathematical Foundation: Shannon Entropy

The entire analysis is based on the Shannon Entropy formula, which measures the average level of "information," "surprise," or "uncertainty" in a set of data.

$$H(X) = -\sum_{i=1}^{n} p(x_i) \log_2(p(x_i))$$

Here's what that means in this project:

H(X): The final Entropy Score in "bits." A higher score means more uncertainty and a stronger, less predictable password list.

p(x_i): The probability of a single character (x_i) appearing. We calculate this by:
p('a') = (Total times 'a' appears) / (Total number of all characters)

What it tells us: A low entropy score (e.g., 2.5 bits) proves that the password list is highly predictable. A high score (e.g., 5.0 bits) proves it is very random. The rockyou.txt file, for example, has a very low entropy, and this tool can prove it mathematically.

4. How to Use

This is a single-file static web application. No installation is required.

Clone or Download:

git clone [https://github.com/YourUsername/Your-Repo-Name.git](https://github.com/YourUsername/Your-Repo-Name.git)


(Or just download the index.html file).

Open in Browser:
Navigate to the project folder and double-click the index.html file.

Use the App:

Click the "Paste Text" tab and paste in your data, then click "Analyze Text."

Click the "Upload File" tab, select a .txt file (like rockyou.txt), and click "Analyze File."

5. Technologies Used

HTML5: For the core structure of the application.

Tailwind CSS: For all styling, layout, and the responsive, dark-mode design.

JavaScript (ES6+): For all application logic, including:

File reading (FileReader)

The calculateEntropy() and analyzeData() functions.

DOM manipulation.

Chart.js: For rendering the beautiful "Top 30 Character Frequency" bar chart.
