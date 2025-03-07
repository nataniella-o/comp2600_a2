# Creating & Hosting a Resume Website for Dummies

## Purpose

This document serves as a comprehensive guide to formatting and hosting a resume using **Pelican** and **GitHub Pages**.  
It is intended for **students, developers, and technical writers** looking to learn how to create and publish a static site efficiently.  

By following this guide, you will:  
✔️ Format a resume using **Markdown**  
✔️ Generate a static website with **Pelican**  
✔️ Host the resume **for free** on **GitHub Pages**  
✔️ Learn about **technical writing best practices** from *Modern Technical Writing* by Andrew Etter  

Technical writing principles encourage **automation, accessibility, and simplicity** in documentation. This guide follows Etter’s recommendations on **leveraging static site generators** to create structured, maintainable documentation.

---

## Prerequisites
Before moving forward, ensure you have the following installed:  

- **A GitHub account** (for hosting the site)
- **Basic knowledge of Markdown** (for formatting the resume)
- **A computer with Python 3 installed** (for running Pelican)
- **An internet connection** (for deploying the site)
- **Git installed** (for version control and pushing changes to GitHub)  

Take a look at the `Further Resources & Readings` section for help with any of these steps

### Why Markdown?  

Markdown is a **lightweight** formatting language that is **easier to use** than HTML. It allows for **quick edits, better readability, and seamless conversion** into HTML without requiring extensive technical knowledge.

Example:
- **Markdown:**  
  ```markdown
  # Work Experience
  - Managed financial reports  
  - Improved budgeting efficiency by 20%
  ```
- **Equivalent HTML:**  
  ```html
  <h1>Work Experience</h1>
  <ul>
    <li>Managed financial reports</li>
    <li>Improved budgeting efficiency by 20%</li>
  </ul>
  ```
Using Markdown aligns with Etter’s principle of **keeping documentation simple** and **avoiding unnecessary complexity**.

### Why a Static Website?  
Static websites **load faster**, require **less maintenance**, and are **more secure** compared to dynamic websites. This follows Etter’s recommendation that **documentation should be hosted in a way that requires minimal manual intervention**.

**Advantages of static websites:**
- No databases or server-side processing
- Quick page load speeds
- Secure hosting through GitHub Pages
- Automated deployments via version control

Using **Pelican**, a **static site generator**, automates the transformation of Markdown into a fully formatted website.

---

## Step-by-Step Instructions
### **Step 1: Setting Up Your Project**
1. **Create a project folder `my-resume` and navigate into it:**
   ```sh
   mkdir my-resume 
   cd my-resume
   ```
2. **Create a virtual environment & activate it:**
   ```sh 
   python3 -m venv pelican-env
   source pelican-env/bin/activate
   ```
   **Why use a virtual environment?**  
   Virtual environments **prevent dependency conflicts** by isolating packages needed for this project.

3. **Install Pelican and Markdown support:**
   ```sh
   pip install pelican markdown
   ```
   **Etter’s principle of automation** applies here. By using tools like Pelican, we avoid manual HTML writing.

---

### **Step 2: Creating Your Resume in Markdown**
4. **Create a `content/` folder and add your resume:**
   ```sh
   mkdir content
   touch content/resume.md
   ```
5. **Write your resume in Markdown.**  
Make sure to include a header at the beginning of each markdown file:
   ```markdown
   Title: John Doe
   Date: 2025-03-06  
   Category: Resume  
   Author: John Doe  
   Summary: Experienced software engineer with expertise in Python and web development.  
   ```
This approach follows Etter’s advice to **use structured content formats**, making resumes easy to edit and maintain.

---

### **Step 3: Initializing Pelican**
6. **Run Pelican’s quickstart command:**
   ```sh
   pelican-quickstart
   ```
7. **Answer the prompts:**
   - **Site title**: `"Your Name's Resume"`  
   - **Default language**: `"en"`  
   - **Use a simple theme**: `"Yes"`  
8. **Place your Markdown resume file in the `content/` directory.**

By automating content generation, Pelican reduces **manual HTML maintenance**, aligning with best practices in modern technical writing.

---

### **Step 4: Generating & Previewing the Static Website**
9. **Generate the website:**
   ```sh
   pelican content
   ```
10. **Preview the site locally:**
    ```sh
    pelican --listen
    ```
11. **Open in a browser:**  
    Navigate to **`http://localhost:8000`**.

Previewing the site before deployment ensures **quality control**, a core technical writing principle.

---

### **Step 5: Deploying to GitHub Pages**
12. **Move the generated files to the root:**
    ```sh
    mv output/* .
    rm -r output
    ```
13. **Create a GitHub repository and copy its URL.**
14. **Initialize a Git repository and push the files:**
    ```sh
    git init
    git add .
    git commit -m "Initial commit: Hosted resume using Pelican"
    git branch -M main
    git remote add origin https://github.com/yourusername/my-resume.git
    git push -u origin main
    ```
15. **Enable GitHub Pages:**
    - Go to **GitHub Repository → Settings → Pages**.
    - Select **main branch** as the source.
    - Save changes.

Your resume is now accessible at:  
**`https://yourusername.github.io/my-resume/`**

This approach follows Etter’s **recommendation of using cloud-based documentation hosting** for accessibility.

---

## Further Resources & Readings

1. **[Pelican Documentation](https://docs.getpelican.com)**
2. **[Markdown Syntax Guide](https://www.markdownguide.org)**
3. **[GitHub Pages Guide](https://pages.github.com)**
4. **[Andrew Etter’s *Modern Technical Writing*](https://www.amazon.ca/Modern-Technical-Writing-Introduction-Documentation-ebook/dp/B01A2QL9SS)**

Technical writing best practices encourage **providing additional resources** to support learning.

---

## Frequently Asked Questions (FAQ)

### **Q1: Why is Markdown better than writing raw HTML?**
Markdown is **easier to read, write, and maintain** than raw HTML. Instead of opening and closing tags (`<h1>Title</h1>`), Markdown simplifies the syntax (`# Title`). It also converts automatically into HTML, reducing the chance of errors.

### **Q2: I changed my resume Markdown file, but the website didn't update. Why?**
Changes do not automatically appear on the website. You must **regenerate and push the updated content**:
```sh
pelican content
git add .
git commit -m "Updated resume"
git push origin main
```
If changes do not appear, try **clearing the browser cache** (`Ctrl + Shift + R`).

### **Q3: Can I use a different theme for my site?**
Yes, to install and apply a new theme:
```sh
git clone https://github.com/getpelican/pelican-themes.git
pelican-themes --install pelican-themes/Flex
```
Modify `pelicanconf.py`:
```python
THEME = "pelican-themes/Flex"
```
Rebuild the site:
```sh
pelican content
```

### **Q4: What should I do if I get a 404 error after deploying my resume site?**  
A **404 error** on GitHub Pages usually means:  
1. **The website deployment is still in progress.** GitHub Pages may take a few minutes to process changes. Wait a few minutes and refresh the page.  
2. **The site is being served from the wrong branch.** Ensure GitHub Pages is set to serve from the `main` branch:
   - Go to **GitHub Repository → Settings → Pages**.
   - Under **Branch**, select `main`.
   - Click **Save**.  
3. **Your `index.html` file is missing.** Run:
   ```sh
   pelican content
   mv output/* .
   rm -r output
   git add .
   git commit -m "Rebuilt site"
   git push origin main
   ```
   Then refresh the page.  

### **Q5: How can I add images to my resume website?**  
Pelican allows you to **add images** for a more professional website.

**Adding Images:**
1. Create a folder for images:
   ```sh
   mkdir content/images
   ```
2. Place your images inside the `images/` folder.
3. Add an image to your Markdown resume using:
   ```markdown
   ![My Profile Picture](images/profile.jpg)
   ```

### **Q6: Do I need to repeat all the setup steps every time I update my resume?**  
No, once your website is set up, you only need to **update your Markdown file** and **regenerate the site**.  
Steps to update your resume:  
1. **Edit `resume.md`** in the `content/` folder.  
2. **Rebuild the site:**
   ```sh
   pelican content
   ```
3. **Push the updated files to GitHub:**
   ```sh
   git add .
   git commit -m "Updated resume"
   git push origin main
   ```
Your website will update automatically after a few minutes.

### **Q7: What if I don’t want to use GitHub Pages? Are there other options?**  
Yes, you can host your Pelican website on other platforms, such as:  
- **Netlify** – Supports static site hosting with automated deployment.  
- **GitLab Pages** – Similar to GitHub Pages but hosted on GitLab.  
- **Cloudflare Pages** – Offers fast static site hosting with global caching.  

To use these platforms, check their documentation for instructions on setting up static sites.

---

## Credits
### **Contributors**  
- **Nataniella Ogogo** – Author, project setup, and technical writing.  
- **Tofunmi Layi-Babatunde** – Peer reviewer, technical feedback, FAQ and content edits.  
- **Kikiola Ojuko** – Peer reviewer, technical feedback, FAQ and content edits.  

### **Third-Party Content**  
- **Pelican** – Static site generator ([Pelican Project](https://getpelican.com/)).  
- **GitHub Pages** – Hosting platform ([GitHub Pages](https://pages.github.com/)).  
- **Pelican Themes** – Website themes ([Pelican Themes Repository](https://github.com/getpelican/pelican-themes)).  
- **Markdown Guide** – Formatting reference ([Markdown Guide](https://www.markdownguide.org/)).  
- **Modern Technical Writing** – Reference book ([Amazon Listing](https://www.amazon.ca/Modern-Technical-Writing-Introduction-Documentation-ebook/dp/B01A2QL9SS)).  
