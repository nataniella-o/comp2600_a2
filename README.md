# Creating & Hosting a Resume Website for Dummies
## Purpose
This document serves as a comprehensive guide to formatting and hosting a resume using **Pelican** and **GitHub Pages**. It is intended for students, developers, and technical writers looking to learn how to create and publish a static site efficiently. 

In addition to providing step-by-step instructions, this README connects **technical writing principles** from *Modern Technical Writing* by Andrew Etter to real-world implementation. It follows best practices for clear, concise, and structured documentation.

By following this guide, you will:  
✔️ Format a resume using **Markdown**  
✔️ Generate a static website with **Pelican**  
✔️ Host the resume **for free** on **GitHub Pages**  
✔️ Learn about **technical writing best practices** from *Modern Technical Writing*

## Prerequisites
Before moving forward, we need to make sure that you have the following things installed:  
- **A GitHub account** (for hosting the site)
- **Basic knowledge of Markdown** (for formatting the resume)
- **A computer with Python 3 installed** (for running Pelican)
- **An internet connection** (for deploying the site)

## Step-by-Step Instructions
### Step 1: Setting Up Your Project
Before publishing a resume, we must create a structured project using **Pelican**.

1. Create a project folder and navigate into it:
   ```sh
   mkdir my-resume && cd my-resume
2. Create a virtual environment & activate it:
    ```sh 
    python3 -m venv pelican-env
    source pelican-env/bin/activate
3. Install Pelican and Markdown support:
    ```sh
    pip install pelican markdown

### Step 2: Creating Your Resume in Markdown
Instead of using Microsoft Word, you can write your resume in Markdown, a lightweight text format. 

4. Create a file named resume.md inside the content/ folder:
    ```sh
    mkdir content
    touch content/resume.md
5. Write your resume in Markdown and save it

### Step 3: Initialize Pelican
6. Run the code below:
    ```sh
    pelican-quickstart
7. Answer the prompts
8. Place your resume markdown file in the "content/" directory.

### Step 4: Generating the Static Website
9. To generate the site, run:
    ```sh
    pelican content
10. To preview locally:
    ```sh
    pelican --listen
Then Open http://localhost:8000 in a browser.

### Step 5: Delploying the Resume to Github Pages
GitHub Pages requires the generated HTML files to be stored in the repository.  

11. Move the generated files to the root:
    ```sh
    mv output/* .
    rm -r output
12. Go to Github, login & create a new repository
13. Copy the link for the repo (e.g. https://github.com/yourusername/my-resume.git)
14. Initialize a Git repository and push:
    ```sh
    git init
    git add .
    git commit -m "Initial commit: Hosted resume using Pelican"
    git branch -M main
    git remote add origin https://github.com/yourusername/my-resume.git
    git push -u origin main
15. Enable GitHub Pages:
    - Go to GitHub Repository → Settings → Pages.
    - Select main branch as the source.
    - Save changes.  

    Visit the generation link given at the top of the page.  
    Congratulations! You should see your resume published on the website. 

## Further Resources & Readings
1. [Pelican Documentation](https://docs.getpelican.com)
2. [Markdown Syntax Guide](https://www.markdownguide.org)
3. [GitHub Pages Guide](https://pages.github.com)
4. [Andrew Etter’s Modern Technical Writing](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.amazon.ca/Modern-Technical-Writing-Introduction-Documentation-ebook/dp/B01A2QL9SS&ved=2ahUKEwjfutm3pvaLAxXkGzQIHVERIIsQFnoECB0QAQ&usg=AOvVaw0yVQfjJ42Dn0-liR2DWbD7)

## Frequently Asked Questions
### Q1: Why is Markdown better than writing raw HTML?
- Markdown is simpler, more readable, and can be converted into HTML easily. Unlike Word documents, Markdown files can be used to generate a website without worrying about formatting issues.
It follows Etter’s principle of minimalism, allowing users to focus on content rather than complex syntax.

### Q2: Why doesn’t my website update when I edit resume.md?
- You need to regenerate the website and push the changes:  
    ```sh
    pelican content
    git add .
    git commit -m "Updated resume"
    git push origin main
### Q3: Can I change the website's theme?
Yes, you can!
- Install and apply a new theme:
    ```sh
    git clone https://github.com/getpelican/pelican-themes.git
    pelican-themes --install pelican-themes/Flex
- Then modify the pelicanconf.py:
    ```sh
    THEME = "pelican-themes/Flex"
- Rebuild the site:
    ```sh
    pelican content
Technical Writing Principle (Etter): Use FAQ sections to preemptively address common user problems.

## Credits
- Created by Nataniella Ogogo
- Reviewed by Tofunmi Layi-Babatunde & Kikiola Ojuko
